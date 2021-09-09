data=[4,5,104,105,110,120,130,130,150,160,170,183,185,187,
       188,191,350,360]

del data[0:2]
print(data)

del data[14:]
print(data)
print()
print()
print()

print("*"*80)
print()
new_data=[4,5,104,105,110,120,130,130,150,160,170,183,185,187,
        188,191,350,360]
min_valid=100
max_valid=200
print(new_data)
stop=0
for index, value in enumerate(new_data):
    if value >= min_valid:
        stop=index
        break
print(stop)
del new_data[:stop]
print(new_data)
print()
print("*"*80)
print()

# process the high values in the list
start = 0
for index in range(len(new_data) - 1, -1, -1):
    if new_data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start)  # for debugging
del data[start:]
print(data)