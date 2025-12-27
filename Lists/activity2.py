def get_count(list):
    count=0
    for item in list:
        if len(item)>=2 and item[0]==item[-1]:
            count+=1
    return count    
my_list=['aba','xyz','ag','xax','1221','ase']
result=get_count(my_list)
print("Number of strings with length >=2 and same first and last character:", result)


