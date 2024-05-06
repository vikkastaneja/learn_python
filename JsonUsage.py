books = {}
books['a']={
    'name': 'blah',
    'price': 100.99,
    'code': 'skjfjs2sds344433'
}

books['b']={
    'name': 'blahblah',
    'price': 10.99,
    'code': '3423432bjkbkbk'
}

import json
s=json.dumps(books)

books_file_location='./books.txt'

with open(books_file_location, 'w') as f:
    f.write(s)

books1=None
with open(books_file_location, 'r') as f:
    books1 = json.loads(f.read())

print(type(books1))
for person in books1:
    print(person)
    print(books1[person])

print(books1)