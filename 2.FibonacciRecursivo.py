import pytest

def fibonacci(n):
    if n < 2:       #base da recursao
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # chamada recursiva

print(fibonacci(45))
@pytest.mark.parametrize("entrada, saida", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8)])

def testa_fatorial(entrada, saida):
    assert fibonacci(entrada) == saida