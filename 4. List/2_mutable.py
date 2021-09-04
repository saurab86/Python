# A mutuable object is one whose value can be changed
# Python has the following mutuable objects:
#  list
#  dict
#  set
#  bytearray

shoppinglist= ["milk","pasta", "egg","spam","bread","rice"]

another_list = shoppinglist
print(id(shoppinglist))
print(id(another_list))

shoppinglist += ["Cookies"]    #Concatenate at the end of list
print(shoppinglist)            # O/P: ['milk', 'pasta', 'egg', 'spam', 'bread', 'rice', 'Cookies']
print(id(shoppinglist))        #give same id as above list because list are mutuable, Python can able to change the contents  of the list without creating new one.

#STRING ARE 'IMMUTABLE'. WHEN WE TRY TO CHANGE A STRING, PYTHON CREATES THE NEW OBJECT -a NEW STRING - AND RE-ATTACHETED A NAME TO IT.
print("*"*80)
a = b = c = d = e = f = another_list  #Binding Multiple name to a List.
print(a)
print("Adding new item to a list that is 'Pasta'")
b.append("Pasta")
print(c)
print(f)
