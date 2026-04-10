import pytest

@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', [4, 5])
@pytest.mark.parametrize('z', [7, 8])
@pytest.mark.parametrize('d', [9, 10])
def test(x, y, z, d):
    print('x=%d, y=%d, z=%d, d=%d' % (x, y, z, d))



