# Generator is a way to create iterators, without doing object management, no need next(), iter() nor StopIteration exception
def CustomGenerator():
    yield 'CNN'
    yield 'Fox'
    yield 'ABC'
    yield 'HBO'

for i in CustomGenerator():
    print(i)

it = CustomGenerator()
print(next(it))

# Fibonacci series using Generators
import modules.FibonacciGenerator as fg
count = 10
for f in fg.FibonacciGenerator():
    if count > 0:
        print(f)
        count -= 1
    else:
        break