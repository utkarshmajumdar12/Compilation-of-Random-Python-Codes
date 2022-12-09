def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(2,3,4,5,6))

def calculate(**kwargs):
    sum = 0
    sum_list = [items for items in kwargs if kwargs.keys=="add"]
    for i in range(len(sum_list)):
        sum +=i
    return sum

print(calculate(add=5))
