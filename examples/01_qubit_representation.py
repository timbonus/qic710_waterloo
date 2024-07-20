"""
Quantum information theory is interested in the manipulation of quantum bits, or qubits.

Qubits are represented as a vector of length two. Each dimension of the vector corresponds to one of two basis vectors
spanning the space of possible states that the qubit may be in. This space is a two-dimensional Hilbert space embedded
in the complex plane, so any pair of basis vectors for a given qubit representation can be reduced to a pair of
orthonormal basis vectors. The 'computational basis' is defined as the representation in which the two basis vectors
correspond to the measurable 0 and 1 states of the qubit, written in Dirac notation as |0> and |1>.

The vector exists in C2, a complex vector space. In the computational basis the modulus squared of the projection onto
each basis vector is interpreted as the probability of observing the qubit in that state (|0> or |1>). when performing
a measurement

The reasons qubits are defined this way is because the quantum particles they represent (namely electrons)  can only be
described mathematically as spinors - complex two-dimensional vectors which are transformed by the set of all 2x2
complex unitary transformations with determinant = 1. The origin of this is related to the type of transformation the
wave function can be subject to under rotation.

Contrast this to classical physics where in our 3D world vectors can be used to represent certain quantities, and
rotations in the classical sense are just the orthogonal 3D rotations that we expect.

One interesting property of C2 comes from a more general property of Lie groups. i.e. that orthogonal groups in n
dimensions - Special Orthogonal groups, or SO(n) - can be expressed as special cases of rotations in an associated
complex space. These ideas are captured by mathematics of Lie groups and Lie algebras.

Specifically when talking about the (real) 3D space we inhabit, the Lie group SO(3) is the group of all orthogonal
rotations in three dimensions. Rotations take the form of 3x3 matrices, and specifically what we are rotating (to
conserve angular momentum) is not a rotating body, but the space (frame of reference) in which it is rotating.

It can be shown that the 'associated complex space' that is relevant to SO(3) is SU(2) - the Special Unitary group in
two complex dimensions. The complex unitary transformations in this group are an equivalent way of representing the
real rotation transformations in SO(3), with one difference. For each rotation in SO(3) there are actually two distinct
corresponding rotations in SU(2), which is kind of where we end up breaking down the angular moment (in three
dimensions) with an additional "spin" angular momentum which requires separate treatment by the two distinct operators
in SU(2).

All in all, the actual vector - or spinor - whose space is undergoing transformations that come from SO(3) and SU(2), is
exactly the same vector.

** how does this lead to Pauli matrices?
** how does this assist with understanding state distinguishing procedures? coding this up would be interesting

The tensor product is a way of combining the vector spaces inhabited by each individual qubit in terms of the underlying
|0> and |1> states that ech qubit can ultimately be measured in. It is worth noting that the space formed by the tensor
product of two qubit states is itself a vector space.
"""

