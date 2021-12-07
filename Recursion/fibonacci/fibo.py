#fibonacci number sequnce 0,1,1,2,3,5,8,13,21,34,55,89...

def fibo(number):
    if  not isinstance(number,int) and number < 0:
        return 1
    if number in [0,1]:
        return 1
    else:
        return fibo(number -1) + fibo(number -2)

print(fibo(5))
