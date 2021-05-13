"""
Were making a program that goes through a list of 
colors and seperates them based off their first letter.
Were going to ask the user for a letter
the program will go through the .txt file and
sperate the colors in the list that begin with the user input.
It will then display all colors that start with that letter. 


"""

"""
colors = list

main()
letter = request_letter
fill_list _with_colors
display_colors

request_letter():
letter = input("enter the first letter: ")
return letter.upper()

fill_list _with _colors(letter):
colors
infile =open("Colors.txt", 'r')
for color in infile:
    if color startswith(letter):
        colors.append(color.rstrip())
    infile.close()

def displayColors():
    for color in colors:
        print(color)        

main()
"""
