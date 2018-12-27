import pytest

from common import calculate_power
from common import compute_grid
from sol1 import highest_power


@pytest.mark.parametrize('coord,serial,power', [
    ((3, 5), 8, 4),
    ((122, 79), 57, -5),
    ((217, 196), 39, 0),
    ((101, 153), 71, 4),
])
def test_calculate_power(coord, serial, power):
    assert calculate_power(coord, serial) == power


@pytest.mark.parametrize('serial,cell_size,corner,power', [
    (18, 16, (90, 269), 113),
    (42, 12, (232, 251), 119),
])
def test_highest_power(serial, cell_size, corner, power):
    grid = compute_grid(serial)
    assert highest_power(grid, cell_size) == (corner, power)
