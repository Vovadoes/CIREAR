import math

# from Charts import *

# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


class Calculation:
    def __init__(self, d, n):
        self.d = d
        self.n = n
        self.i = None

    def simple(self):
        self.i = (self.d / 100) / (1 - self.n * (self.d / 100))

    def difficult(self):
        self.i = self.d / (100 * (1 - (self.d / 100)))


if __name__ == "__main__":
    d = 20
    n = 0.5
    calculation = Calculation(d, n)
    calculation.simple()
    print(calculation.i)
    calculation.difficult()
    print(calculation.i)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
