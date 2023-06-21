""" x = len("Hello World")
y = len(str(x))
z = y^2
print(z)

while True:
    try:
        answer = input("Do you want to continue? (yes/no): ")
        if answer.lower() == "yes":
            print("Continuing...")
            break
        elif answer.lower() == "no":
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    except:
        print("Invalid input. Please enter 'yes' or 'no'.") """

""" x = {0:4, 1:8, 2:16, 3:32}
print(list(x.values())[2]) """

""" x = 65
y = 53
z = y if(x % 2 == 0) else x
print(z) """

""" x = [[0.0, 1.0, 2.0],[4.0, 5.0, 6.0]]
y = x[1][2]
print(y) """

""" x = 10.0
y = (x < 100.) and isinstance(x, float) """

""" x = 50
if x > 10: print(30)
elif x == 40: print(20)
else: print(10) """

""" 'a' + 'x' if '123'.isdigit() else 'y' + 'b' """

""" var = 'Python'
t = type(list())

print(t(var)) """

""" l = [1,2,3,4,5]
print(l[2:4])"""

""" x = [(1,2),(3,4),(5,6)]
y = [i[1] for i in x]
print(y) """

""" def func(a,b):
    return a + b
#Output: error
args = (2,3)
kwargs = {'b': 4}
res = func(*args, **kwargs)
print(res) """

""" x = [1,[2,3],4]
y = x.copy()
x[1].append(5)
print(y) """

""" x = "Hello"
y = x
x += "World"
print(y) """

""" x = [(1,2),(3,4),(5,6)]
y = list(zip(*x))
print(y) """
