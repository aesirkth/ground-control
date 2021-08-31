import matplotlib.pyplot as plt
from time import time, sleep
from math import pi, sqrt, cos, sin
from threading import Thread
from numpy.random import normal

def send_data():
	print(".", end="")
	return


def white_noze(scale=1):
	"""Normal white noze"""
	# For uniform distribution, random.random can be used
	return normal(0, scale)


class Simulator(object):
	"""Simulation of the rocket"""
	def __init__(self, tm, real_time=True):
		self.tm = tm
		self.real_time = real_time
		self.t = None
		self._must_stop = False

	def launch(self):
		self.t = Thread(target = self._simu)
		self.t.start()

	def stop(self):
		self._must_stop = True

	def _simu(self):
		gamma0 = 89 # angle between the horizon and the rocket (°) 

		h = 0.01

		times = [10, 20, 30]
		trusts = [5e3, 5e3, 5e3]

		g0 = 9.81 # g at sea-level

		# Rocket's characteristics
		m_dry = 50 # kg
		m_prop = 50 # kg
		ISP = 250 # ~ solid or liquid fuel
		CD = 0.3
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

		phase = 0
		t = 0
		t0 = time()
		while z >= 0 and not self._must_stop:
			if self.real_time:
				last_t = t
				t = time() - t0
				h = t - last_t
			if phase < len(times) and m_prop > 0:
				if t >= times[phase]:
					phase += 1
					print("Phase", phase + 1)
				if phase < len(times):
					T = trusts[phase]
				else:
					T = 0
			else:
				T = 0
				if m_prop < 0:
					m_prop = 0

			m = m_dry + m_prop
			rho = rho0
			g = g0 # Assuming g cst
			m_dot = T / (ISP * g0) # T = Isp * g * m_dot
			D = 1/2 * CD * rho * S * (v_z**2 + v_x**2) # Drag force (isothermal atmostphere)

			v_x = v_x + (T - D) * cos(gamma) / m * h
			v_z = v_z + ((T - D) * sin(gamma) / m - g) * h
			x = x + v_x * h
			z = z + v_z * h
			m_prop = m_prop - m_dot * h
			gamma = gamma - g * cos(gamma) / sqrt(v_x**2 + v_z**2) * h

			if not self.real_time:
				t += h

			send_data()
