#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.

The 100-matrix_mul module supplies one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    """matrix_mul function
    Args:  m_a m_b
    Returns:  m_c """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if (len(m_a) == 0 or len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if (len(m_b) == 0 or len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if (not isinstance(elem, int) and not isinstance(elem, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(row):
                raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        for elem in row:
            if (not isinstance(elem, int) and not isinstance(elem, float)):
                raise TypeError("m_b should contain only integers or floats")
            if len(m_b[0]) != len(row):
                raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for m in range(len(m_a)):
        row = []
        for p in range(len(m_b[1])):
            c = 0
            for i in range(len(m_a[0])):
                add = m_a[m][i] * m_b[i][p]
                # print("add " , add)
                c += add
                # print("c ", c)
            row += [c]
            # print("row " , row)
        m_c += [row]

    return m_c
