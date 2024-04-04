def add(x,y):
    print(__name__)
    return x+y
    


def division(x,y):
    if y != 0:
        print(__name__)
        return x/y
    else:
        print("Error, cannot divide by zero")
        print(__name__)
        return
    
print(division(2,3))