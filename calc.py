def add(x,y):
    print(__name__)
    return x+y
    


def division(x,y):
    if y != 0:
        return x/y
    else:
        print("Error, cannot divide by zero")
        return
    
def main():
    print("lets calculate! input 1 to add, 2 to divide")
    x =  int(input())
    if x ==1:
        a = int(input())
        b = int(input())
        add(a,b)
    elif x==2:
        a = int(input())
        b = int(input())
        division(a,b)