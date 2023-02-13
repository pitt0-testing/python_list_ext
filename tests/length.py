from list_ext import List

names = List[str]() # []
print(names.empty)
# output: True

print(names.single)
# output: False

print(names.multiple)
# output: False


names.append("Gianni") # ["Gianni"]
print(names.empty)
# output: False

print(names.single)
# output: True

print(names.multiple)
# output: False

names.append("Pinotto") # ["Gianni", "Pinotto"]
print(names.empty)
# output: False

print(names.single)
# output: False

print(names.multiple)
# output: True


print(names.capacity) # starts from 0
# output: 1
print(names.length)
# output: 2