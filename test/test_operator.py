import unittest

import numpy as np

from operators import TrivialRotation


class test_operators(unittest.TestCase):

    def test_trivial(self):
        tr = TrivialRotation(theta=np.pi/2)
        self.assertEqual(tr.theta, np.pi/2)