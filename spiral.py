import turtle

radius = float(input ("Nhập bán kính hình xoắn: "))
d= int(input ('Nhập khoảng tiến lên '))
original_xcor = turtle.xcor()
original_ycor = turtle.ycor()

while True:
    turtle.forward(d)
    turtle.left(10)
    d += 0.1
    if turtle.distance(original_xcor, original_ycor) > radius:
        break
          
turtle.done()