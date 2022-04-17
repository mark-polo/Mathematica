import numpy as np
from Balance_analysis_models.General_Matrix import general_matrix


class Task_two:
    def __init__(self, b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31, v1 , v2 , v3):
        self.g_m = general_matrix(b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31)
        self.V = np.array([
            [v1],
            [v2],
            [v3]
        ])

    def calculation_P_matrix(self):
        D_transpose = self.g_m.calculation_D_matrix().transpose()
        return D_transpose.dot(self.V)