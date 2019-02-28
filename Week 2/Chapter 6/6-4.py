'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102)
    by replacing your series of print statements with a loop that runs through the dictionary’s keys and values .
When you’re sure that your loop works, add five more Python terms to your glossary .
When you run your program again, these new words and meanings should automatically be included in the output .
'''

glossary = {'word1': 'explanation1','word2': 'explanation2','word3': 'explanation3','word4': 'explanation4','word5': 'explanation5'}

for a,b in glossary.items():
    print(f"{a}, {b} \n")
    #print(f"{a} \n {b}")
