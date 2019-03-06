## This code will compute the fibonacci sequence

def fibonacci(x):
    if (x<0) : raise ValueError('input is less than 0')
    list = [0,1]
    count = 0
    while count < x:
        y = list[len(list)-1]
        z = list[len(list)-2]
        list.append(y+z)
        count+=1
    return list
