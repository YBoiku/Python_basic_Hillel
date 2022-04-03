####################### 1 #######################
my_list = [100, 156, 365, 4568, 20, 48, 600]
for some_list in my_list:
    if some_list > 100:
        print(some_list)
####################### 2 #######################
my_list = [100, 156, 365, 4568, 20, 48, 600]
new_list = []
for some_list in my_list:
    if some_list > 100:
        new_list.append(some_list)
print(new_list)
####################### 3 #######################
my_list = [100, 1, 365, 48, 2, 48, 60]
# my_list = [1]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(sum(my_list[-2:]))
print(my_list)
