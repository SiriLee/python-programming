from .add import add
from .minus import minus

def calculate(a, b):
    return add(a, b), minus(a, b)
