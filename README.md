# List Extension

This package extends lists in python with some methods that help fast and clean coding.
For example: 

### Where Method
```py
from list_ext import List

def filter_evens():
    my_list = List([1, 2, 3, 4, 5, 6])
    return my_list.where(lambda x: (x % 2) == 0)
```

### Select Method
```py
def select_property(characters: List):
    return characters.select(lambda character: character.health_points)
```

### Concat Method
```py
def create_string(people: List):
    return people.concat()

create_string(["Paolo", "Giovanni", "Maria"])
# output: "Paolo, Giovanni, Maria"

def new_line_string(people: List):
    return people.concat(sep="\n")

new_line_string(["Paolo", "Giovanni", "Maria"])
# output: 
# Paolo
# Giovanni
# Maria
```

And much more!