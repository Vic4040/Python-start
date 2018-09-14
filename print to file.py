ft = open('C:/Users/vic40/Documents/1.txt','w')

newarray= []


N = int(input("Please enter data: "))
for i in range (N):
    import random
    line = str(random.uniform(-100, 100))

newarray.append(line) #append to the list


ft.writelines(newarray)

ft.close()

with open("C:/Users/vic40/Documents/1.txt", "r") as ft:
    for line in ft:
        print(line)
