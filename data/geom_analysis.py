"""
Functions and script for geometry analysis
"""
import numpy
import os

def calculate_distance(atom1, atom2):
    """
    Calculate the distance between two atoms

    Parameters
    ----------
    atom1: list
        A list of coordinates [x, y, z]
    atom2: list
        A list of coordinates [x, y, z]

    Returns
    -------
    bond_length: float
        The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0, 0, 0], [0, 0, 1])
    1.0
    """
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance

def bondcheck(bond_distance,minimum_value=0,maximum_value=1.5):
    """"
    See if bond meets requirements to be considered a bond

    Parameters
    ----------
    bond_distance: float
        the distance between atoms in angstroms
    minimum_value: float
        the minimum value to be considered a bond
    maximum_value: float
        the maximum value to be considered a bond

    Returns
    -------
    True if bond
    False if not a bond
    """

    if not isinstance(bond_distance, float):
        raise TypeError(F'bond_distance must be type float.')


    if bond_distance > minimum_value and bond_distance < maximum_value:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise IndexError('No file was found charlie')


    file_location = sys.argv[1]
    print(file_location)

    #xyz_file = open(file_location,'r')
    xyz_file = open('water.xyz','r')
    data = xyz_file.readlines()

    num_atoms = int(data[0])
    coord_data = data[2:]

    symbols = []
    coordinates = []

    for atom in coord_data:
        atom_data = atom.split()
        symbol = atom_data[0]
        symbols.append(symbol)
        x, y, z = atom_data[1], atom_data[2], atom_data[3]
        coordinates.append([float(x), float(y), float(z)])

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB<numA:
                x_distance = atomA[0]-atomB[0]
                y_distance = atomA[1]-atomB[1]
                z_distance = atomA[2]-atomB[2]
                distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
                if distance > 0 and distance < 1.5:
                    print(F'{symbols[numA]} to {symbols[numB]}: {distance:.3f}')
