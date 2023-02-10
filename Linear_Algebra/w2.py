# %%
import numpy as np


# %%
def SwapRows(M, row_num_1, row_num_2):
    M_new = M.copy()
    # exchange row_num_1 and row_num_2 of the matrix M_new
    temp = M_new[row_num_1].copy()
    M_new[row_num_1] = M_new[row_num_2]
    M_new[row_num_2] = temp
    return M_new


# %%
A_test = np.array([
    [1, -2, 3, -4],
    [-5, 6, -7, 8],
    [-4, 3, -2, 1],
    [8, -7, 6, -5]
], dtype=np.dtype(float))

# %%
print(SwapRows(A_test, 0, 2))
