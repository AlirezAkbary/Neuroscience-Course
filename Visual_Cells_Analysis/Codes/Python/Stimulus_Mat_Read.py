from scipy import io
import numpy as np


def main():
    stimulus = io.loadmat("msq1D.mat")
    return np.array(stimulus["msq1D"])

