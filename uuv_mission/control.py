import numpy as np
import pandas as pd


class Controller():
    def __init__(self, Kp = 0.15, Kd = 0.6, T = 1):
        self.Kp = Kp
        self.Kd = Kd
        self.T = T
        self.prev_error = 0
        self.prev_time = 0

    def step(self, measurement, reference):
        dt = self.T
        error = reference - measurement
        derivative = (error - self.prev_error) / dt
        control = self.Kp * error + self.Kd * derivative
        self.prev_error = error
        return control
    