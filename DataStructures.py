def sample_function(need_what):
    if need_what == 'integer':
        return 1
    elif need_what == 'string':
        return 'sample'
    elif need_what == 'float':
        return 3.14
    else:
        return 'Not found'


print(sample_function('string'))
print(sample_function('integer'))
print(sample_function('float'))
print(sample_function('else'))

# Create a list and print it
vehicles = ['car', 'truck', 'bus', 'bicycle','motorcycle']
print(type(vehicles))
print(vehicles)
print(len(vehicles))
print(vehicles[len(vehicles) - 1])

# Create a dictionary and print it using iterator
d={'truck':6,'car':4,'bicycle':2}
print(type(d))
print(d['car'])
for key in d:
    print ('key:', key, ',value:', d[key])

d['motorcycle'] = 2
print(d)
print(len(d))


for k,v in d.items():
    print('key:', k, 'value:', v)

print('car' in d)
print('motor' in d)

d.clear()
print(len(d))


# Tuples - can have any data type
t = ('tom', 25.0, 55)
print(len(t))
print(t)
for e in t:
    print(e)

print(t[0],t[1],t[2])
