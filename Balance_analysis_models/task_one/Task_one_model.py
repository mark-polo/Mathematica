import numpy as np
from Balance_analysis_models.General_Matrix import general_matrix


class Task_one:
    def __init__(self, b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31, n):
        self.n = n / 100
        self.g_m = general_matrix(b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31)

    def calculation_A_matrix(self):
        A = self.g_m.B / self.g_m.X
        return A

    def calculation_D_matrix(self):
        D = self.g_m.E - self.calculation_A_matrix()
        return np.linalg.inv(D)

    def calculation_X_matrix(self):
        X = self.calculation_D_matrix().dot(self.g_m.Y)
        return X

    def final_calculation(self):
        new_demand = self.n * self.g_m.Y[2][0]
        transport_data = self.calculation_D_matrix()[:,-1]
        return transport_data.dot(new_demand)