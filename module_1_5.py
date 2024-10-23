immutable_var = 8, "red", 11
print(immutable_var)
immutable_var[0] = 228  #кортеж не поддерживает обращение по элементам
print(immutable_var)
mutable_list = [3, 9, 6 , "Jojo"]
mutable_list.append("Bizarre Adventure")
print(mutable_list)