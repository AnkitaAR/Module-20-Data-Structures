s1={1,2,3}
s2={'a','b','c'}
result=list(zip(s1,s2))
print(list(result))
list1=[10,20,30]
list2=[100,200,300]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks=["reliance","tata","infosys"]
prices=[2000,3000,4000]
new_dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print(new_dict)
        