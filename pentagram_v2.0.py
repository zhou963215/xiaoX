"""
    功能: 五角星的绘制
    版本: 2.0
    日期: 03/05/2018
    加入循环操作
"""
import turtle


def draw_pentagram(size):
    # 绘制五角星
    count = 1

    while count <= 5:
        turtle.forward(size)
        turtle.right(144)

        count += 1


def main():

    turtle.penup()
    turtle.bk(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    while size <= 100:
        draw_pentagram(size)
        size += 10
    turtle.exitonclick()


if __name__ == '__main__':
    main()