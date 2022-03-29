# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons = [{'name': 'Ana', 'age': 15, 'hobbies': ['futbol']},
            {'name': 'Pepe', 'age': 10, 'hobbies': ['futbol']}]

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

names_of_persons = [person['name'] for person in persons]
print('2 => names_of_persons ', names_of_persons)

# 3) Use a list comprehension to check whether all persons are older than 20.

older_persons = all([person['age'] > 20 for person in persons])
print('3 => older_persons ', older_persons)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

copy_persons = [person.copy() for person in persons]
copy_persons[0]['name'] = 'Leonardo'
print('4 => ', copy_persons)

# 5) Unpack the persons of the original list into different variables and output these variables.

person_1, person_2 = persons
print('5 => person 1 ', person_1)
print('5 => person 2 ', person_2)