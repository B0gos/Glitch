import turtle
count = 0
repeat = 0
turtle.color("blue")
for repeat in range(2):
    for counnt in range(88):
        turtle.forward(100)
        turtle.right(178)
        print("working on layer")
        print(repeat)
        print(count)
        count += 1
    count = 0
    turtle.forward(100)
turtle.left(90)
turtle.width(10)
turtle.forward(500)
