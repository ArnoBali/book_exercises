'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message, The first three items in the list are: . Then use a slice to print the first three items from that program’s list .
• Print the message, Three items from the middle of the list are: . Use a slice to print three items from the middle of the list .
• Print the message, The last three items in the list are: . Use a slice to print the last three items in the list .
'''


l = [i for i in range(11)]

cube_l = []

for x in l:
    cube_l.append(x**3)


print(cube_l)

print(f"The first three items in the list are: {cube_l[:3]}")
print(f"Three items from the middle of the list are: {cube_l[5:8]}")
print(f"The last three items in the list are: {cube_l[-3:]}")