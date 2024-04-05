import numpy as np
import matplotlib.pyplot as plt

# Given values of r(i), p(i), and k(i)
r_values = [0.07028132-0.13571006j, 
            0.07028132+0.13571006j, 
            -0.05018348+0.01417803j, 
            -0.05018348-0.01417803j]

p_values = [0.78465217+0.0346749j, 
            0.78465217-0.0346749j, 
            0.84417798+0.11384352j, 
            0.84417798-0.11384352j]

k_values = [2.14e-5, 0, 0, 0]

# Time indices
n_values = np.arange(31)  # n values up to 30

# Compute h(n)
hn_values = np.zeros_like(n_values, dtype=np.complex128)
for n in n_values:
    for i in range(len(r_values)):
        hn_values[n] += r_values[i] * (p_values[i] ** n)
    for j in range(len(k_values)):
        if n - j >= 0:
            hn_values[n] += k_values[j]

# Plot
plt.stem(n_values, np.abs(hn_values))
plt.xlabel('$n$')
plt.ylabel('$|h(n)|$')
plt.title('Magnitude of $h(n)$')
plt.grid(True)
plt.show()
