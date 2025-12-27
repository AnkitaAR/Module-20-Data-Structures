tuple1=(1,2,5,"hello",7.4,"world",10)
print("Tuple wity different data values:", tuple1)
tuple2=(10,20,30,40,50)
print("Tuple with integer values:", tuple2)
tuple3=tuple2+(9,)
print("New tuple after adding an element to tuple2:", tuple3)

#count the occurence of an element in a tuple
tuple4=(1,2,3,4,5,1,2,1,1,6,7,8,1)
count_1=tuple4.count(1)
print("Count of 1 in tuple4:", count_1)

#perform slicing on a tuple
tuple5=(10,20,30,40,50,60,70,80,90)
sliced_tuple=tuple5[2:7]
print("Sliced tuple from index 2 to 6:", sliced_tuple)
