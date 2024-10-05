def test_function():
    def inner_function():
        print(f'Я в области видимости функции test_function')
    inner_function()

try:
    test_function()
    inner_function()
except Exception as e:
    print(type(e), e)