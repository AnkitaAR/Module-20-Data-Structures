start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
melist_even = []
melist_odd = []
mylist_squares = []
print("List of squares.")
for j in range(start_range, end_range + 1):
    mylist_squares.append(j**2)
print(mylist_squares)

for i in mylist_squares:
    if i % 2 == 0:
        list.extend(melist_even, [i])

print("List of even numbers.")
print(melist_even)

for i in mylist_squares:
    if i % 2 != 0:
        list.extend(melist_odd, [i]) 

print("List of odd numbers.")
print(melist_odd)
