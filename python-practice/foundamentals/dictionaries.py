# Initiated with curly braces
# Consists of key value pairs
student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

# These are ways of accessing values by keys
print(student['name'])
print(student.get('name'))
# [] method of access will produce a keyerror if none is found. The {} method returns none
