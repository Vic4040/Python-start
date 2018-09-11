y = [1, 3, 5, 6, 548, 549, 10, 11, 12]

new_list = [num / 4 for num in y if num % 2 != 1]
new_list2  = [num * 2 for num in y if num % 2 == 1]
print(new_list)
print(new_list2)

z = (new_list2 + new_list)
print(sorted(z))