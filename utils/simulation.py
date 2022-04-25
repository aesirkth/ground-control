import matplotlib.pyplot as plt
import utils.fc as protocol
from time import time, sleep
from math import pi, sqrt, cos, sin
from threading import Thread
from numpy.random import normal
from utils.definitions import *


def white_noise(scale=1):
	"""Normal white noise"""
	# For uniform distribution, random.random can be used
	return normal(0, scale)

def pressure_ratio_from_mach(M):
	gamma = 1.4 # Heat capacity ratio
	if M > 1: # Rayleigh formula
		ratio = (gamma + 1)**2 * M**2 / (4*gamma*M**2 - 2 * (gamma - 1))
		ratio **= gamma/(gamma-1)
		ratio *= (1-gamma + 2*gamma*M**2) / (gamma+1)
		return ratio
	else:
		ratio = 1 + (gamma-1)/2 * M * M
		ratio **= gamma/(gamma-1)
		return ratio


class Simulator(object):
	"""Simulation of the rocket"""
	def __init__(self, tm, real_time=True):
		self.tm = tm
		self.real_time = real_time
		self.t = None
		self._must_stop = False
		self.next_data = b""
		self.current_data = []
		self.pointer = 0
		self.tm.open_simulation(self)

	def launch(self):
		self.t = Thread(target = self._simu)
		self.t.start()

	def stop(self):
		self._must_stop = True

	def read(self,size=1):
		if self.pointer == 0:
			self.current_data = self.next_data
			self.next_data = b""

		if self.current_data == b"":
			return self.current_data

		size = min(size, len(self.current_data)-self.pointer)
		data = self.current_data[self.pointer:self.pointer+size]
		self.pointer += size
		if self.pointer >= len(self.current_data):
			self.pointer = 0
		# print("Simu :", data)
		return data

	def send_data(self, x, y, z, v_x, v_y, v_z):
		altitude = z
		latitude, longitude = 67.85, 20.24
		latitude += x * 180 / (pi*6371e3)
		mach_number = sqrt(v_x*v_x + v_y*v_y + v_z*v_z) / 340 # Assume air speed cst = 340 m/s
		# print(mach_number)
		pressure_ratio = pressure_ratio_from_mach(mach_number)

		data = b""
		msg_checksum = 0

		# 85 = position
		class_id = 85
		fc_encoder = protocol.id_to_message_class(class_id)
		fc_encoder.set_altitude(altitude)
		fc_encoder.set_longitude(longitude)
		fc_encoder.set_latitude(latitude)
		buf = fc_encoder.build_buf()

		data += bytes([class_id]) + buf

		# 86 = differential_pressure (but pressure ratio here)
		class_id = 86
		fc_encoder = protocol.id_to_message_class(class_id)
		fc_encoder.set_differential_pressure(pressure_ratio)
		buf = fc_encoder.build_buf()
		msg_checksum = 0

		data += bytes([class_id]) + buf

		# Compute the checksum
		for v in data:
			msg_checksum += (v&240)>>4
			msg_checksum = (msg_checksum + (v&15)) % 16

		info = (msg_checksum << 4) + 2
		data = bytes([SEPARATOR[0], info]) + data

		self.next_data = data

	def _simu(self):
		gamma0 = 89 # angle between the horizon and the rocket (°) 

		h = 0.01

		times = [14]
		trusts = [3.3e3]

		g0 = 9.81 # g at sea-level

		# Rocket's characteristics
		m_dry = 30 # kg (~21 kg propulsion system)
		m_prop = 31.2 # kg (28.1 kg nitrous oxide oxidizer mass + 3.1 kg paraffin+carbon fuel)
		ISP = 214 # ~ 214-221
		CD = 0.3 # Drag coefficient
		rho0 = 1.2 # Air density at T = 25°C
		S = 0.0314 # Cross section surface

		# Position
		x = 0
		z = 0
		v_x = 1
		v_z = 0
		gamma = gamma0 * pi / 180

		# Debug
		X = [x]
		Z = [z]
		Vx = [v_x]
		Vz = [v_z]
		print("/!\\ For the moment it is not the differential pressure which is return but the pressure ratio /!\\")
		print("Phase 1")
		empty_tank = False

		phase = 0
		T = trusts[phase]
		t = 0
		t0 = time()
		while z >= 0 and not self._must_stop:
			if self.real_time:
				last_t = t
				t = time() - t0
				h = t - last_t
			if m_prop > 0:
				if phase < len(times):
					if t >= times[phase]:
						phase += 1
						if phase < len(times):
							print("Phase", phase + 1)
							T = trusts[phase]
						else:
							print("End of propulsion")
							print("Propellant remaining:", m_prop)
							T = 0
			else:
				if not empty_tank:
					empty_tank = True
					print("No more propellant")
				T = 0
				if m_prop < 0:
					m_prop = 0

			m = m_dry + m_prop
			rho = rho0
			g = g0 # Assuming g cst
			m_dot = T / (ISP * g0) # T = Isp * g * m_dot
			D = 1/2 * CD * rho * S * (v_z**2 + v_x**2) # Drag force (isothermal atmosphere)

			v_x = v_x + (T - D) * cos(gamma) / m * h
			v_z = v_z + ((T - D) * sin(gamma) / m - g) * h
			x = x + v_x * h
			z = z + v_z * h
			m_prop = m_prop - m_dot * h
			gamma = gamma - g * cos(gamma) / sqrt(v_x**2 + v_z**2) * h

			if not self.real_time:
				t += h
			else:
				self.send_data(x, 0, z, v_x, 0, v_z)
				sleep(0.05) # Decrease the accuracy, but increase the FPS of the controller/dashboard

		if self.real_time:
			self.send_data(x, 0, z, 0, 0, 0)
