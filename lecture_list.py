my_list = [15,6,7,8,35,12,14,4,10,15]
my_string_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art","econ"]
print(f"Ints: {my_list}")
print(f"Strings: {my_string_list}")
#Finding info
# print(my_string_list.index("physics"))
#Length
#print(my_list[-1])
#min value
print(min(my_list))
#max value
print (max(my_list))
# methods available
print(dir(my_list))
#Count
print(my_list.count(15))
#Add Remove
# append, insert and extend
my_string_list.extend(my_new_list)
print(f"Strings: {my_string_list}")
# pop() remove()
print(f"Strings: {my_string_list.pop()}")
#sublist
my_list[-1] = 1000
print(f"Ints: {my_list}")
my_list.reverse()
print(my_list)
#Simple for loop
for item in my_list:
    print(item)
