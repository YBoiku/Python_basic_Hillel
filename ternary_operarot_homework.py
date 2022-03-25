###################### 1 ######################
value = 150
new_value = int(value) / 2 if value < 100 else int(-value)
print(new_value)
###################### 2 ######################
value = 150
new_value = int(value) == "1" if value < 100 else int(value) == "0"
print(new_value)