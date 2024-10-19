def test_function(x):
    y=x**2
    def  inner_function(z):
        y=z/2
        print('Я в области видимости функции test_function')

    inner_function(6)
    return print(y)
test_function(4)
inner_function(5)