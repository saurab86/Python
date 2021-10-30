#Python 3 has 5 sequence types built in
# They are the string type, list, tuple, range, bytes and bytearray
string1="he's "
string2="probably "
string3="pining "
string4="fjords"
 
print(string1 + string2 + string3 + string4)
print("hello " * 5)  #Hello will be repeated 5 times.
#print("Hello"* 5 +4) would not print Hello 9 times. I shows an error.
#print("hello"(5+4)) would print Hello 9 times

today = "friday"
print("day" in today)       #TRUE
print("fri" in today)       #TRUE
print("parrot" in string4)  #FALSE