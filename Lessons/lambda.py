people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# lookup and return name property
# if we need short functions like before we can represent them as lambda functions

""" def f(person):
    return person["name"] """

# sort using function f result
people.sort(key = lambda person: person ["name"])

print(people)