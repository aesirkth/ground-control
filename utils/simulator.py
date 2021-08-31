import time

class Quaternion:
    w = 0
    x = 0
    y = 0
    z = 0

class Vector:
    def __init__(self, _x = 0, _y = 0, _z = 0):
        self.x = _x
        self.y = _y
        self.z = _z

    def __add__(self, b):
        c = Vector()
        c.x = self.x + b.x
        c.y = self.y + b.y
        c.z = self.z + b.z
        return c

    def __sub__(self, b):
        c = Vector()
        c.x = self.x - b.x
        c.y = self.y - b.y
        c.z = self.z - b.z
        return c

    def __truediv__(self, b):
        c = Vector()
        c.x = self.x / b
        c.y = self.y / b
        c.z = self.z / b
        return c

    def __mul__(self, b):
        c = Vector()
        c.x = self.x * b
        c.y = self.y * b
        c.z = self.z * b
        return c

    def __rmul__(self, b):
        c = Vector()
        c.x = self.x * b
        c.y = self.y * b
        c.z = self.z * b
        return c
    
    def __str__(self):
        return f"x: {self.x} y: {self.y} z: {self.z}"

class Body:
    def __init__(self):
        self._position = Vector()
        self._velocity = Vector()
        self._acceleration = Vector()

        self._heading = Vector()
        self._angular_velocity = Vector()
        self._angular_acceleration = Vector()

        self._com = Vector() # center of mass
        self._mass = 1
        self._dt = 0
        self._t = 0

    def apply_force(self, where, force): # pos, N
        self._acceleration += force * self._mass
        #dis to hard
        #_angular_acceleration += 
    
    def apply_angular_momentum(momentum):
        return

    def get_rotation():
        return

    def update(self, dt):
        self._velocity += self._acceleration * dt
        self._position += self._velocity * dt
        
        self._angular_velocity += self._angular_acceleration * dt
        self._heading += self._angular_velocity * dt

        self._acceleration = Vector(0, 0, 0)
        self._angular_acceleration = Vector(0, 0, 0)

    def set_mass(self, mass):
        self._mass = mass


class World:
    _start_time = 0

    def __init__(self, setup, before, after, bodies):
        self._setup = setup
        self._before_func = before
        self._after_func = after
        self._bodies = bodies
        
    def start(self, step_length):
        self._setup()
        start_time = time.time()
        last_time = time.time() - start_time
        current_time = time.time() - start_time
        while True:
            current_time = time.time() - start_time
            dt = current_time - last_time
            self._before_func(current_time, dt)
            for body in self._bodies:
                body.update(dt)
            self._after_func(current_time, dt)
            last_time = current_time
            sleep_length = step_length - (time.time() - last_time)

            if (sleep_length > 0):
                time.sleep(step_length - (time.time() - last_time))