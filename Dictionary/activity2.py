my_dict={'Codingal':2,'is':2,'best':2,'for':2,'learning':2,'Python':1}
#print dictionary
print("Original Dictionary:",my_dict)
result=0
for key in my_dict:
    if my_dict[key]==2:
        result+=1
print("Number of keys with value 2:",result)