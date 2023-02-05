import torch


def mul(a, b):
    a_rows, a_columns = a.shape
    b_rows, b_columns = b.shape
    if a_columns != b_rows:
        raise ValueError()
    result = torch.zeros(a_rows, b_columns)
    print(result.shape)
    # TODO Remove 2nd loop with broadcasting
    for i in range(a_rows):
        for j in range(b_columns):
            result[i, j] = (a[i, :] * b[:, j]).sum()
    return result


# @profile
def multiply(a, b):
    a_rows, a_columns = a.shape
    b_rows, b_columns = b.shape

    if a_columns != b_rows:
        raise ValueError()

    result = torch.matmul(a, b)

    return result


def calc_column(A, B):
    if len(A[0]) != len(B):
        raise ValueError()
    res = []
    for i in range(len(A)):
        res.append(torch.matmul(A[i], B))
    return res
