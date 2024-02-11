import numpy as np


def qubit_norm(state: np.array):
    return np.sum(np.square(np.absolute(state)))


class QubitCartesian:

    def __init__(self, zero: np.complex_, one: np.complex_):

        self.zero = zero
        self.one = one
        self.state = np.array([self.zero, self.one], dtype=np.complex_)
        self._validate_state()

    def _validate_state(self):
        if not np.isclose(qubit_norm(self.state), 1.0):
            raise ValueError('state definition does not have unit norm')

    def to_euler(self):
        global_phase = -np.angle(self.zero)                  # global phase rotation to achieve purely real |0>
        theta = 2 * np.arccos(np.absolute(self.zero))        # length of |0> determines theta
        phi = 0                                              # default value for phi when state equals |0>
        if theta != 0.0:                                     # i.e. state is not exactly |0>
            phi = np.angle(self.one) + global_phase          # phi is original complex angle of |1> minus global phase
        return QubitEuler(theta=theta, phi=phi)


class QubitEuler:

    def __init__(self, theta: float, phi: float ):

        self.theta = theta
        self.phi = phi
        self.state = np.array((np.cos(theta/2),
                               np.sin(theta/2)*(np.cos(phi)+np.sin(phi)*1j)),
                              dtype=np.complex_)

    def to_cartesian(self):
        zero = self.state[0]
        one = self.state[1]
        return QubitCartesian(zero=zero, one=one)