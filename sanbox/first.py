print ("welcome to the class")

def greet_names(names):
    for name in names:
        print(f"Hi {name}")

list_of_names = ["joy,", "arit", "agnes"]
greet_names(list_of_names)

for num in range(0, 100, 1):
    if num %7 == 0:
        print(num)

for num in range(5, 25):
    if num % 2 == 0:
        continue
print(num)



for i in range (2, 14, 3):
    if i > 8:
        break
    print(i)

for i in range (1, 15):
    if i == 6:
        break
    print (i)   


for i in range (1, 15):
    if i > 5:
        break
    print (i)   
