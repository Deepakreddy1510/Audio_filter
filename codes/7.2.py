import numpy as np
import matplotlib.pyplot as plt

# Given values of r(i), p(i), and k(i)
r_values = [0.06029142-0.14682007j, 
            0.06029142+0.14682007j, 
            -0.06029459+0.02518904j, 
            -0.06029459-0.02518904j]

p_values = [0.88475217+0.0445749j, 
            0.88475217-0.0445749j, 
            0.94427798+0.11485352j, 
            0.94427798-0.11485352j]

k_values = [2.19e-5, 0, 0, 0]

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
