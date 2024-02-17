import numpy as np
from scipy.linalg import inv, det


class BaseOperator:

    def __init__(self, **kwargs ):
        self.matrix = kwargs['matrix']
        self._validate_operator()

    def _validate_operator(self):
        """
        Unitary matrix checks.
        :return: None
        """
        assert np.isclose(det(self.matrix), 1.0)
        assert np.allclose(self.matrix.I, self.matrix.H)


class TrivialRotation(BaseOperator):
    """
    Rotation is real?
    """

    def __init__(self, theta, **kwargs):
        self.theta = theta
        matrix = np.array([[np.cos(self.theta), np.sin(self.theta)],
                           [-np.sin(self.theta), np.sin(self.theta)]])
        super().__init__(matrix=np.matrix(matrix))