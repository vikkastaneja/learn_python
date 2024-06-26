import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--number1', help='first number')
    parser.add_argument('--number2', help='second number')
    parser.add_argument('--operation', help='operation to perform on number1 and number2', choices=['add', 'multiply','subtract'])
    args = parser.parse_args()

    print('passed numbers are:',args.number1, args.number2)
    print('operation:',args.operation)
    result = None
    n1 = int(args.number1)
    n2 = int(args.number2)
    if args.operation == 'add':
        result = n1 + n2
    elif args.operation == 'subtract':
        result = n1 - n2
    elif args.operation == 'multiply':
        result = n1 * n2

    print('Result:', result)