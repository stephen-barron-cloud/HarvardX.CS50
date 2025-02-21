# hogwarts.py

students = ["Hermoine", "Harry", "Ron", "Draco"]
print(students[0]) # print specific location in list, lists are 0 indexed
for x in students:
    print(x)

## len function
for i in range(len(students)):
    print(i + 1, students[i])

# dict data type.  Key Value pairs.  1:1 ratio
var_students = { #type dict
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

print(var_students["Hermoine"])

#print through the keys
for x in var_students:
    print(x, var_students[x], sep="; ")


# A list of dicts
var_students2 = [
    {"name" : "Hermoine", "house" : "Gryffindor", "Patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "Patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "Patronus" : "Jack Russell Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "Patronus" : None}
]

for e in var_students2:
    print(e["name"], e["house"],e["Patronus"],  sep=", ")
