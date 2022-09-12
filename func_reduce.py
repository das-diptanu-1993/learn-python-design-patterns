from functools import reduce

def func1(n):
    return (n+10)

def func2(n):
    return (n**2)

def func3(n):
    return (n/2)

func4 = lambda n: 3*n

def generate_pipeline_executor(*funcs):
    return lambda x: reduce(lambda value, function: function(value), funcs, x)

func = generate_pipeline_executor(func1, func2, func3, func4)

print(func(10))

