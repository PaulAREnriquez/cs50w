people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

"""
def f(person):
    return person['name']

people.sort(key=f)
"""
# instead of defining a function which has a short implementation
# we can use lambda
# lambda syntax is:
# lambda input : output based on the input
people.sort(key=lambda person: person['name'])
print(people)