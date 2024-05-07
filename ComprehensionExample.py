lst = [1,2,3,4,5,6,7,8,9]
# problem - find even numbers
# first way - iterate the list and filter
even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)

print(even)

# second way - use comprehension
even = [i for i in lst if i%2 == 0]
print(even)

# problem - square numbers using comprehension
sqr = [i*i for i in lst]
print(sqr)

# It works on sets as well
s = set([1,2,3,4,5,6,6,5,4])
print(s)

# Square using comprehension on set
sqr = [i*i for i in s]
print(sqr)

# Comprehension on dictionaries
cities=['Mumbai', 'New York', 'Paris']
countries=['India', 'USA', 'France']
# Zip creates collection of tuples index-wise
z = zip(cities, countries)
print(type(z))
for t in z:
    print(t)

# create dict
d = {city:country for city,country in zip(cities,countries)}
print(type(d))
print(d)