"""
Tests for geom_analysis.py
"""

import pytest
import geom_analysis as ga


def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2



def test_bondchecktrue():
    bond_distance = 1.0
    minimum_value = 0
    maximum_value = 1.5

    observed = ga.bondcheck(bond_distance, minimum_value, maximum_value)
    assert observed == True

def test_bondcheckfalse():
    bond_distance = 1.6
    minimum_value = 0
    maximum_value = 1.5

    observed = ga.bondcheck(bond_distance, minimum_value, maximum_value)
    assert observed == False

def test_bondcheckerror():
    bond_distance = 'a'

    with pytest.raises(TypeError):
        observed = ga.bondcheck(bond_distance)
