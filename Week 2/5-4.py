'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain .
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien .
• If the alien’s color isn’t green, print a statement that the player just earned 10 points .
• Write one version of this program that runs the if block and another that runs the else block . DON'T UNDERSTAND
'''

alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    if color == 'green':
        print("You earned 5 points for shooting the alien!")
    else:
        print("You just earned 10 points")

