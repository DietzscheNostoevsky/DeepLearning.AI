# %%
import numpy as np

# %%

A = np.array([[2, 1, 5], [1, 2, 1], [2, 1, 3]])

# %%
d = np.linalg.det(A)
print(d)
# %%

B = np.array([[1, 2, 3], [0, 2, 2], [1, 4, 5]])
np.linalg.det(B)

# %%
