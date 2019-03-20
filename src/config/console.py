import os

def get_size():
    """
        gets and gives console dimention

        Return: (int rows, int columns)
    """
    return os.popen('stty size', 'r').read().split()

