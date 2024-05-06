import sys
sys.path.append('/Users/vtaneja/AI_ML/learn_python/modules')
import my_module as m


print(m.sample_function('string'))
print(m.sample_function('integer'))
print(m.sample_function('float'))
print(m.sample_function('else'))

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
