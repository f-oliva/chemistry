"""Engine to run the physical part of the simulation"""
import numpy as np

dt = 0.1 # timestep

class Particle:
    """Class for the particles
    """
    def __init__(self, charge: int, mass: float, px: float, py: float, pz: float, vx: float, vy: float, vz: float, ax: float, ay: float, az: float, radius: float) -> None:
        self.charge = charge
        self.mass = mass
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az
        self.r = radius
    
    def update_velocity(self) -> None:
        """Update the velocity of a particle
        """
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.vz += self.az * dt

    def update_positions(self, p: float, v: float, a: float) -> None:
        """Update the position of a particle
        """
        self.px += self.vx * dt
        self.py += self.vy * dt
        self.pz += self.vz * dt
    
    def get_position(self) -> np.array:
        """Provides the position in a numpy array

        :return: The numpy array with the position
        """
        return np.array([self.px, self.py, self.pz])

    def get_velocity(self) -> np.array:
        """Provides the velocity in a numpy array

        :return: The numpy array with the velocity
        """
        return np.array([self.vx, self.vy, self.vz])
