import numpy as np


def quantum_state_norm(state: np.array):
    return np.sum(np.square(np.absolute(state)))


class QubitCartesian:

    def __init__(self, zero: 'complex', one: 'complex'):

        self.zero = zero
        self.one = one
        self.global_phase = -np.angle(self.zero)  # global phase rotation to achieve purely real |0>
        self.state = np.array([self.zero, self.one], dtype='complex' )
        self._validate_state()

    def _validate_state(self):
        if not np.isclose(quantum_state_norm(self.state), 1.0):
            raise ValueError('state definition does not have unit norm')

    def to_bloch(self):
        theta = 2 * np.arccos(np.absolute(self.zero))  # length of |0> determines theta
        phi = 0  # default value for phi when state equals |0>
        if theta != 0.0:  # i.e. state is not exactly |0>
            phi = np.angle(self.one) + self.global_phase  # phi is original complex angle of |1> minus global phase
        return QubitBloch(theta=theta, phi=phi, global_phase=self.global_phase)


class QubitBloch:

    def __init__(self, theta: float, phi: float, global_phase: float = None):

        self.theta = theta
        self.phi = phi
        self.global_phase = global_phase if global_phase else 0.0
        self.bloch = np.array((np.sin(theta) * np.cos(phi),
                               np.sin(theta) * np.sin(phi),
                               np.cos(theta/2)),
                              dtype=float)

    def to_cartesian(self):
        zero = np.cos(self.theta/2)
        one = np.sin(self.theta/2) * (np.cos(self.phi)+np.sin(self.phi)*1j)
        if self.global_phase != 0:
            euler_rotation = np.cos(self.global_phase)+np.sin(self.global_phase)*1j
            zero = zero * euler_rotation
            one = one * euler_rotation
        return QubitCartesian(zero=zero, one=one)


# now have way of representing qubits need to:
# - define requirements for determining optimal separation
#    - unitary operators
#    - some kind of optimisation procedure
#    - full bloch state view?
#    - some visualisations that will help clarify this all
# - code up ability to combine qubits into higher dimensional states
