num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y,num1,num2)
print(list(result))

def square(n):
    return n*n
numbers=[1,2,3,4,5]
squared_numbers=map(square,numbers)
print(list(squared_numbers))