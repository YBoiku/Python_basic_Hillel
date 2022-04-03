####################### 1 #######################
my_list = [100, 156, 365, 4568, 20, 48, 600]
for some_list in my_list:
    if some_list > 100:
        print(some_list)
####################### 2 #######################
my_list = [100, 156, 365, 4568, 20, 48, 600]
my_result = []
for new_list in my_list:
    if new_list > 100:
        my_result.append(new_list)
print(my_result)
####################### 3 #######################
my_list = [100, 1, 365, 48, 2, 48, 60]
# my_list = [1]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(sum(my_list[-2:]))
print(my_list)
