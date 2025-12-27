numbers=[10,4,2,20,5,8,15,6]
sum=0
for num in numbers:
    sum+=num
print("Sum of all numbers in the list:", sum)
avg=sum//len(numbers)
print("Average of the numbers in the list:", avg)
max_num=max(numbers)
print("Maximum number in the list:", max_num)
min_num=min(numbers)
print("Minimum number in the list:", min_num)