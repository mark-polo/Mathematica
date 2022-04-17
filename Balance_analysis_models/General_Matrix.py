import numpy as np

class general_matrix:
    def __init__(self, b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31):
        self.B = np.array([
            [b11, b12, b13],
            [b21, b22, b23],
            [b31, b32, b33]
        ])

        self.X = np.array([
            [x11],
            [x21],
            [x31]
        ])

        self.Y = np.array([
            [y11],
            [y21],
            [y31]
        ])

        self.E = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

    def calculation_A_matrix(self):
        A = self.B / self.X
        return A

    def calculation_D_matrix(self):
        D = self.E - self.calculation_A_matrix()
        return np.linalg.inv(D)