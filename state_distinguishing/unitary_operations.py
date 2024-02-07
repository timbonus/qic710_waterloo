import numpy as np


def rotation_x(qbit_state: np.array, angle: int) -> np.array:
    """

    :param qbit_state: a numpy array of shape (2, ), with dtype np.imag. The two elements are the amplitudes of the
                       state in the two basis vectors |0> and |1>, where the amplitude of |0> is real and non-negative
                       (there exist global rotations for all possible states that allow this assumption to be true). 


    :param angle: int, degrees of rotation in th
    :return:
    """
    rotation_matrix = np.array(  )