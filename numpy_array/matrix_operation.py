#------------------------#
# Apache License 2.0
# @copyright
#------------------------#

# Common library
import sys

# feature realted library
import numpy as np
import scipy.linalg as lalgebra


def matrix_mul(marr, narr):
    """

    :param marr:
    :param narr:
    :return:
    """
    return marr * narr

def matrix_product(marr, narr):
    """

    :param marr:
    :param narr:
    :return:
    """
    #marr.dot(narr)
    #
    return marr @ narr

def matrix_transpose(marr):
    """

    :param marr:
    :return:
    """
    pass


if __name__ == '__main__':

    m = np.array([[3,4], [-1,5]])
    n = np.array([[7,8],[1,2]])
    print(matrix_mul(m,n))
    a = np.arange(0,30,3).reshape(2,5)
    rg = np.random.default_rng(1)
    rg.








