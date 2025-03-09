# Dictionatries are a collection of key-value pairs. They are unordered, changeable and indexed.
# They are written with curly brackets, and have keys and values.
# The keys are unique within a dictionary while the values may not be.
# The values of a dictionary can be of any data type, while the keys must be immutable.
grades = {
    "name": 'Berdimuhammet',
    "age": 25,
    "hobbies": ['reading', 'coding', 'playing games'],
    "grades": {
        "math": 4,
        "english": 5,
        "history": 5,
        "surname": 'Yslamow'
    }
}
print(grades.get('name'))