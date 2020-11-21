#------------------------#
# Apache License 2.0
# @copyright
#------------------------#

# Common library
import sys

# feature realted library
import numpy as np
import scipy.linalg as lalgebra

def get_column(narr, col_num):
    """

    :param narr:
    :return:
    """
    if col_num < narr.shape[1]:
        col = narr[:,col_num]
    else:
        raise Exception("Out of range")
    return col

if __name__ == '__main__':
    one_dim_array = np.array([1,2,4,5,6],float)
    print(one_dim_array)
    ndim = one_dim_array.ndim
    print("dimension of array {}".format(ndim))

    shape = one_dim_array.shape
    print("shape of the array {}".format(shape))

    two_dim_array = np.array([[1,2],[3,4],[5,6]])
    print("dimension of the array {}".format(two_dim_array.ndim))
    print("shape of the array {}".format(two_dim_array.shape))
    print("size of the araray {}".format(two_dim_array.size))

    col = get_column(two_dim_array, 1 )
    print(col, col.ndim,col.shape)

