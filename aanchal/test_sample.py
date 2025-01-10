"""import pytest

def func(x):
    return x + 5

def test_method():
    assert func(3) == 5"""

def greet(fx):
    def mfx(*args, **kwargs)   :
        print("thanks for using tis function")
        return mfx

@greet
def hello():
    print("hello world")

@greet    
def add(a,b):
    print(a+b)   

hello()
greet(add)(1,2)      