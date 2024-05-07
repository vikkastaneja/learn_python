import modules.my_module as m
def test_main():
    print(__name__)
    m.test_main_module()

if __name__ == '__main__':
    test_main()

print(__name__)
