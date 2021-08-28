# parrot = "Norwegian Blue"

# for character in parrot:
#     print(character)      #Print each character in new lines according to character length.

number = "9,223;372:036 054,775;807"
seprators = ""
for char in number:
    if not char.isnumeric():
        seprators = seprators + char

print("The character in given numbers are: {}".format(seprators))

print("*"*80)

quote="Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads,\
 the Fresh-Water System,and Public Health, what have the Romans ever done for us?"
for char in quote:
   if char.isupper():
       print(char)