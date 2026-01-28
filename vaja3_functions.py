def hello():
    print("Hello, Python learners!")

hello()

def greeting(name: str):
    print(f"Pozdravljen, {name}!")

greeting("Jon")

def sum(x: int, y: int) -> int:
    return x + y

print(sum(1,2))

def fav_color(color: str = "blue"):
    return color

print(fav_color("rumena"))
print(fav_color())

print("squares: ")
def squares():
    sq = []
    for i in range(1, 6):
        r = i * i
        sq.append(r)
    return sq

print(squares())

print("Function That Uses a Loop:")
def looping(n: int):
    for x in range(0, n):
        print(x+1)

looping(10)

print("list modification: ")
def list_modification(l: list) -> list:
    new_list = []
    for i in l:
        j = i * 2
        new_list.append(j)
    return new_list


print(list_modification([1,2,3,4,5]))