import numpy as np


def form_qubit_system_tensor( *qubits ):
    """
    :param qubits: any number of arguments each containing numpy arrays of shape (2,)
    :return: an n-dimensional tensor, where n is the number of arguments passed into the function.
    """
    system = 1
    for qubit in qubits:
        system = np.kron(system, qubit)
    return system


def bit_transform(theta, psi, phi): #np.matmul(A, bit)
    """
    Defines a generic unitary transformation of a bit (vector in C2).
    """
    assert 0 <= theta <= np.pi
    assert 0 <= psi <= 4 * np.pi
    assert 0 <= phi <= 2 * np.pi
    A_00 = np.cos(theta / 2) * np.exp(1 / 2 * 1j * (psi + phi))
    A_01 = np.sin(theta / 2) * np.exp(1 / 2 * 1j * (psi - phi))
    A_10 = -np.sin(theta / 2) * np.exp(-1 / 2 * 1j * (psi - phi))
    A_11 = np.cos(theta / 2) * np.exp(-1 / 2 * 1j * (psi + phi))
    A = np.array([[A_00, A_01], [A_10, A_11]])
    return A


def system_transform( *transforms ):
    total_transform = 1
    for transform in transforms:
        total_transform = np.kron(total_transform, transform)
    return total_transform


def state_to_probability(state):
    """
    :param state: numpy tensor containing n levels of C2
    :return: float - probability of correctly labelling the state
    """
    return np.sum(np.square(np.abs(state)))


def average_case_probability(alpha_subspace,
                             beta_subspace,
                             plus_arrival_probability=0.5):
    return (plus_arrival_probability * state_to_probability(alpha_subspace) +
            (1 - plus_arrival_probability) * state_to_probability(beta_subspace))


# state should be defined as tuple of complex numbers (a + b*1j, c+d*1j) with mod = 1
q = 'c'

if q == 'a':
    alpha = np.array([[1, 0]])
    beta = np.array([[np.sqrt(3)/2, 1/2]])
elif q == 'b':
    alpha = np.array([[3 / 5, 4 / 5 * 1j]])
    beta = np.array([[4 / 5 * 1j, 3 / 5]])
elif q == 'c':
    alpha = form_qubit_system_tensor(np.array([[1, 0]]),
                                     np.array([[1, 0]]))
    beta = form_qubit_system_tensor(np.array([[1/np.sqrt(2), 1/np.sqrt(2)]]),
                                    np.array([[1/np.sqrt(2), 1/np.sqrt(2)]]))
else:
    print(f'Invalid option "{q}"')
    exit(1)

# validation
assert np.isclose(np.tensordot(alpha, np.conjugate(alpha).T, axes=1), 1.0)
assert np.isclose(np.tensordot(beta, np.conjugate(beta).T, axes=1), 1.0)

results = []

if q in ('a', 'b'):   # single state case

    for theta in np.linspace(0, np.pi, 17):
        for phi in np.linspace(0, 2 * np.pi, 17):
            for psi in np.linspace(0, 4 * np.pi, 17):
                transform = bit_transform(theta=theta, phi=phi, psi=psi)
                prob = average_case_probability(np.matmul(transform, alpha)[0],
                                                np.matmul(transform, beta)[1])
                results.append((theta, phi, psi, prob))

    results = np.array(results, dtype=[('theta (rad)', 'f'),
                                       ('phi (rad)', 'f'),
                                       ('psi (rad)', 'f'),
                                       ('average case success probability', 'f')])

    best = results[np.argmax(results['average case success probability'])]

    print(best[0] / np.pi)
    print(best[1] / np.pi)
    print(best[2] / np.pi)
    print(best[3])

elif q in ('c', 'd'):
    for theta in np.linspace(0, np.pi, 17):
        for phi in np.linspace(0, 2 * np.pi, 17):
            for psi in np.linspace(0, 0 * 4 * np.pi, 1):
                transform_1 = bit_transform( theta=theta, phi=phi, psi=psi )
                for theta_2 in np.linspace(0, np.pi, 17):
                    for phi_2 in np.linspace(0, 2 * np.pi, 17):
                        for psi_2 in np.linspace(0, 0 * 4 * np.pi, 1):
                            transform_2 = system_transform(transform_1, bit_transform( theta=theta_2, phi=phi_2, psi=psi_2))
                            prob = average_case_probability(np.matmul(transform_2, alpha.T)[0], np.matmul(transform_2, beta.T)[1:])
                            # prob = average_case_probability(np.tensordot(transform_2, alpha)[0, :],
                            #                                 np.tensordot(transform_2, beta)[1, :])
                            results.append((theta/np.pi, phi/np.pi, psi/np.pi, theta_2/np.pi, phi_2/np.pi, psi_2/np.pi, prob))

    results = np.array(results, dtype=[('theta (rad)', 'f'),
                                       ('phi (rad)', 'f'),
                                       ('psi (rad)', 'f'),
                                       ('theta_2 (rad)', 'f'),
                                       ('phi_2 (rad)', 'f'),
                                       ('psi_2 (rad)', 'f'),
                                       ('average case success probability', 'f')])

    best = results[np.argmax(results['average case success probability'])]
    print(best)
    print(best[-1])
