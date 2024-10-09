import pytest

@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', [4, 5])
@pytest.mark.parametrize('z', [7, 8])
def test(x, y, c):
    print('x=%d, y=%d, z=%d' % (x, y, z))
    print(123)
