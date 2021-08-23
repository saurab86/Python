splitString = "This string has been\nsplit over\nsevral\nlines" #backslash 'n' changes the new line
print(splitString)

tabbedString = "1\t2\t3\t4"   #backslash ''t' set the new tab
print(tabbedString)

print("""The pet shop owner said"No, no 'e's uh,...he's resting".""")
#OR
print("The pet shop owner said \"No, no 'e's uh, ...he's resting\".")

#Splitting the strings
anotherSplitString = """This String has been
split over
several
times"""
print(anotherSplitString)

escapeSplitString = """This String has been \
split over \
several \
times\
"""
print(escapeSplitString)

#escaping the backslash
print("C:\\Users\\tekken\\newfile.txt") #By using double backslash can escape the backslsah property.
#Or
print(r"C:\Users\tekken\newfile.txt") #By using 'Raw String'. We can create the raw string by prefixing the string with letter 'r' 