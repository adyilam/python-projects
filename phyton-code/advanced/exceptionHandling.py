#
def divide():
    list_ = [2, 4, 8, 10, 0]
    x = 2
    for i in list_:
        try:
            if x / i == 1:  # divisible by zero error at index 4
                print(i)
        except:
            print("Error: Divisible by zero!")
