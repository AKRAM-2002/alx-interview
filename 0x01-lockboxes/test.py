my_list = [1,2,3]
my_list1 = [5,6]
my_list.append(4)
my_list.extend(my_list1)

print(my_list)
new_my_list = []
for i in range(len(my_list)):
    new_my_list.append(my_list[i] ** 2)

print(new_my_list)

