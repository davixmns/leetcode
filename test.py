
persons = [
    {
        "name": "John",
        "age": 30,
    },
    {
        "name": "David",
        "age": 30,
    },
    {
        "name": "Lucas",
        "age": 30,
    },
]

name = [p["name"] for p in persons]

for i in range(len(persons)):
    print(persons[i]['age'] + i+1)
