###################### 1 ######################
value = 10
new_value = value / 2 if value < 100 else -value
print(new_value)
###################### 2 ######################
value = 15
new_value = 1 if value < 100 else 0
print(new_value)
###################### 3 ######################
value = 150
new_value = True if value < 100 else False
print(new_value)
###################### 4 ######################
my_str = "qwer"
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)
###################### 5 ######################
my_str = "qwer"
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)