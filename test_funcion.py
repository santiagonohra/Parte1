"""
Your module description
"""
from funcion import numero_menor

def test_numero_menor():
    assert numero_menor([1, 2, 3, 8, 5, 12, -1, -56, 0, 0.1]) == -56
    assert numero_menor([1,42,42,243,24,7,1,23,4315,65,-1243, -12, -5, -456, 53, 65, 0, 461, 345]) == -1243
    assert numero_menor([12,735,74,45,645,6,77,84,8,8,8,2,73,4,7,8,56,4,345,36,8, -1, 32, -4, -656345, 14234, 2]) == -656345
    