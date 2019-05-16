#This is my geometry analysis code
import numpy
import os

def calculate_distance(atom1, atom2):
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance

def bondcheck(bond_distance,minimum_value=0,maximum_value=1.5):
    if bond_distance > minimum_value and bond_distance < maximum_value:
        return True
    else:
        return False

file_location = os.path.join('data','water.xyz')
print(file_location)

xyz_file = open(file_location,'r')

print("TEST")
print(xyz_file[0])
print("END TEST")

symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]

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
