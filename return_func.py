def say_hello(name):
    return 'Hello {}'.format(name)

def be_awesome(name):
    return 'yo {}'.format(name)

def greet_bob(greeter_func):
    return greeter_func('Bob')

print(greet_bob(say_hello))
print(greet_bob(be_awesome))
