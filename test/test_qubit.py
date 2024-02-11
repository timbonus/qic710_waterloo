import unittest

import numpy as np

from qubit import QubitCartesian, QubitEuler


class TestQubitCartesian(unittest.TestCase):

    def test_to_cartesian(self):
        q = QubitCartesian(zero=1, one=0)
        q_e = q.to_euler()
        self.assertAlmostEqual(q_e.theta, 0)
        self.assertAlmostEqual(q_e.phi, 0)

        q = QubitCartesian(zero=0, one=1j)
        q_e = q.to_euler()
        self.assertAlmostEqual(q_e.theta, np.pi)
        self.assertAlmostEqual(q_e.phi, np.pi/2)

        q = QubitCartesian(zero=np.sqrt(5)/5+2/5*1j, one=4/5)
        q_e = q.to_euler()
        self.assertAlmostEqual(q_e.theta, 2*np.arccos(0.6))
        self.assertAlmostEqual(q_e.phi, -np.arctan(2/np.sqrt(5)))


class TestQubitEuler(unittest.TestCase):

    def test_to_cartesian(self):
        q = QubitEuler(theta=0, phi=0)
        q_c = q.to_cartesian()
        self.assertAlmostEqual(q_c.zero, 1)
        self.assertAlmostEqual(q_c.one, 0)

        q = QubitEuler(theta=np.pi, phi=np.pi/2)
        q_c = q.to_cartesian()
        self.assertAlmostEqual(q_c.zero, 0)
        self.assertAlmostEqual(q_c.one, 1j)


if __name__ == '__main__':
    unittest.main()
