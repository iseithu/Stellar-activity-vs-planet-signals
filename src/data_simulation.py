import numpy as np

def generate_data(n_samples=1000):
    time = np.linspace(0, 10, n_samples)

    # Stellar activity (noise)
    stellar_noise = 0.2 * np.sin(2 * np.pi * time)

    # Planet signal (transit-like dip)
    planet_signal = np.where((time % 2) < 0.1, -0.5, 0)

    signal = stellar_noise + planet_signal

    return signal
