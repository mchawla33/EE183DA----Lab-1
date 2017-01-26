'''
EE183DA -- Lab 1
Professor Mehta

Written by:
Mrinal Chawla
'''

import math

'''
Builds a 4x4 transformation matrix based on the state variables
'''
def trans_matrix(q1, q2, q3, q4):
	matrix = [[0 for x in range(4)] for y in range(4)]
	matrix[0][0] = int(math.sin(q2)*math.sin(q4) + math.cos(q2)*math.cos(q3)*math.cos(q4))
	matrix[0][1] = int(math.sin(q2)*math.cos(q4) - math.sin(q4)*math.cos(q2)*math.cos(q3))
	matrix[0][2] = int(math.sin(q3)*math.cos(q2))
	matrix[0][3] = int((5*math.cos(q3)*math.cos(q4)+25)*math.cos(q2) + 5*math.sin(q2)*math.sin(q4) + 30)
	matrix[1][0] = int(math.sin(q2)*math.cos(q3)*math.cos(q4) - math.sin(q4)*math.cos(q2))
	matrix[1][1] = int(-math.sin(q2)*math.sin(q4)*math.cos(q3) - math.cos(q2)*math.cos(q4))
	matrix[1][2] = int(math.sin(q2)*math.sin(q3))
	matrix[1][3] = int((5*math.cos(q3)*math.cos(q4)+25)*math.sin(q2) - 5*math.sin(q4)*math.cos(q2))
	matrix[2][0] = int(math.sin(q3)*math.cos(q4))
	matrix[2][1] = int(-math.sin(q3)*math.sin(q4))
	matrix[2][2] = int(-math.cos(q3))
	matrix[2][3] = int(5*math.sin(q3)*math.cos(q4))
	matrix[3][0] = 0
	matrix[3][1] = 0
	matrix[3][2] = 0
	matrix[3][3] = 1
	return matrix

'''
Pulls out the last column of the matrix. This column is the origin
'''
def extract_origin(matrix):
	retval = []

	retval.append(matrix[0][3])
	retval.append(matrix[1][3])
	retval.append(matrix[2][3])
	retval.append(matrix[3][3])

	return retval

'''
Performs forward kinematics
'''
def forward_kinematics(q1, q2, q3, q4):
	t_matrix = trans_matrix(q1, q2, q3, q4)
	return extract_origin(t_matrix)

'''
Creates lookup table for relevant positions of the linkage
'''
def build_lookup_table():

	table = {}
	key = forward_kinematics(math.radians(0), math.radians(45), math.radians(90), math.radians(0))
	value = [0, 45, 90, 0]

	table[str(key)] = value

	key2 = forward_kinematics(math.radians(0), math.radians(0), math.radians(90), math.radians(0))
	value2 = [0, 0, 90, 0]

	table[str(key2)] = value2

	return table
'''
Performs inverse kinematics using the lookup method
'''
def inverse_kinematics(x, y, z):
	table = build_lookup_table()
	key = [x, y, z, 1]
	value = table[str(key)]

	return value


'''
The following code executes the commands asked for in the Results section 
of the spec. 
'''
start =  inverse_kinematics(47, 17, 5)
end =  inverse_kinematics(55, 0, 5)

print start
print end

print forward_kinematics(0, 45, 90, 0)

print forward_kinematics(0, 33.75, 90, 0)

print forward_kinematics(0, 22.5, 90, 0)

print forward_kinematics(0, 11.25, 90, 0)

print forward_kinematics(0, 0, 90, 0)