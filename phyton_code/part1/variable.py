# global variable
var = "global variable"


def myfunction():
    y = "inside function"
    print(y)
    print("Hello: " + var)


myfunction()


class MyClass:
    # Variable
    # data type of variable specified by casting
    x = int(3)
    y = str('Hello')
    z = float(5)
    print(x)
    print(y)
    print(z)

    # legal variable names
    varname = "legal variable name"
    var_name = "legal variable name"
    _var_name = "legal variable name"
    varName = "legal variable name"
    x, y, z = "test1", "test2", "test3"
    print(x, y, z)
    x = y = z = "test"
    print(x, y, z)
    print(x + y + z)
    x = 10
    y = 20
    print(x + y)

    # illegal variable name
    # 1varname = "illegal variable name"
    # var-name = "illegal variable name"
    # var name = "illegal variable name"
