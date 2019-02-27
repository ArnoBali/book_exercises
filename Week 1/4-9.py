'''
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .
'''

l = [i for i in range(11)]

cube_l = []

for x in l:
    cube_l.append(x**3)


print(cube_l)
