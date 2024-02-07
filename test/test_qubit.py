import unittest

import numpy as np

from qubit import QubitCartesian, QubitEuler


class TestQubitEuler(unittest.TestCase):

    def test_to_cartesian(self):
        q = QubitEuler(theta=0, phi=0)
        q_c = q.to_cartesian()
        self.assertAlmostEquals(q_c.bra, 1+0j)


if __name__ == '__main__':
    unittest.main()
