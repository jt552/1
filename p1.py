import torch
from multiply import mul, calc_column, multiply
from cdf_plot import cdf_plot

# Create matrices with random values
A = torch.rand(100000, 1000)
B = torch.rand(1000, 100000)
# B = [torch.rand(1000, 1) for _ in range(10000)]
C = torch.rand(10000, 1)
# print(B[0])
# Plot Matrix A's CDF
# cdf_plot(A)

# Multiply(A*B)*C
try:
    AB = multiply(A, B)
    result = multiply(AB, C)
    print(result[0, 0])
except ValueError as e:
    print(f'Incorrect matrix dimensions : {e}')
# res = []
# for i in range(1000):
#     res.append(calc_column(A, B[i]))
# print(res[0])
