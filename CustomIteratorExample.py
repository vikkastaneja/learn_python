import modules.custom_iterator as ci

if __name__ == '__main__':
    custom_iterator = ci.CustomIterator()
    it = iter(custom_iterator)
    for i in it:
        print(i)

    it = iter(ci.CustomIterator())
    print(next(it))
    print(next(it)) 
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration as st:
        print('End of iteration reached')