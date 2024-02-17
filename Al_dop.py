import numpy as np
import openpyxl
import pandas


arr = pandas.read_excel('/Users/Xiaomi/MIEM/ПСА/Semestr2.xlsx',
                        sheet_name='for_python')

arr=arr.to_numpy()


def minor_ij(arr, i, j):
    m_shape = arr.shape[0] - 1
    arrM = np.eye(m_shape, dtype='float')
    print(arrM.shape)
    arrM[:i, :j] = arr[:i, :j]
    arrM[:i, j:] = arr[:i, j + 1:]
    arrM[i:, :j] = arr[i + 1:, :j]
    arrM[i:, j:] = arr[i + 1:, j + 1:]
    return arrM



rows = arr.shape[0]
cols = arr.shape[1]
i, j = (map(int, input().split()))
print((-1) ** (i + j) *np.linalg.det(minor_ij(arr, i, j)))

