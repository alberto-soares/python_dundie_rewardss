from functools import wraps

def soma(a, b):
    return a + b 
soma(1, 2)


def dobra(f):
    def manipuladora(a, b):
        return f(a * 2, b * 2)
 

def dobra(f):
    def manipuladora(a, b):
        return f(a * 2, b * 2)
    return manipuladora
 
soma = dobra(soma)

soma
soma(1, 2)

@dobra
def soma(a, b):
    return a + b
soma(1, 2)


@dobra
def multi(a, b):
    return a * b
multi(2, 4)


def bold(f):
	@wraps(f)
    def wrapper(text):
	    return f(f"<strong>{text}</strong>")
    return wrapper 


def ital(f):
    @wraps(f)
    def wrapper(text):
        return f(f"<i>{text}</i>")
    return wrapper
 

@bold
@ital
def hello(text):
    return f"Hello {text}"
hello("Alberto Luiz")

