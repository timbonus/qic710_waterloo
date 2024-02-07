import numpy as np


def qubit_norm(state: np.array):
    return np.sum(np.square(np.absolute(state)))


class QubitCartesian:

    def __init__(self, bra: np.complex_, ket: np.complex_):

        self.bra = bra
        self.ket = ket
        self.state = np.array([self.bra, self.ket], dtype=np.complex_)
        self._validate_state()

    def _validate_state(self):
        if qubit_norm(self.state) != 1.0:
            raise ValueError('state definition does not have unit norm')

    def to_euler_angles(self):
        global_phase = -np.angle(self.bra)
        standard_bra = self.bra * np.sin(global_phase) + np.cos(global_phase) * 1j
        standard_ket = self.ket * np.sin(global_phase) + np.cos(global_phase) * 1j
        theta = 2 * np.arccos( standard_bra )
        phi = np.angle(standard_ket / (2 * theta))
        return QubitEuler(theta=theta, phi=phi)


class QubitEuler:

    def __init__(self, theta: float, phi: float ):

        self.theta = theta
        self.phi = phi
        self.state = np.array((np.cos(theta/2),
                               np.sin(theta/2)*(np.cos(phi)+np.sin(phi)*1j)),
                              dtype=np.complex_)
        self._validate_state()

    def _validate_state(self):
        if qubit_norm(self.state) != 1.0:
            raise ValueError('state definition does not have unit norm')

    def to_cartesian(self):
        bra = self.state[0]
        ket = self.state[1]
        return QubitCartesian(bra=bra, ket=ket)