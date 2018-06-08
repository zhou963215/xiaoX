"""
    功能: 五角星的绘制
    版本: 2.0
    日期: 03/06/2018
    加入循环操作
    使用迭代绘制
"""
import turtle


def deaw_recurssive_pentagram(size):
    """
    :param size:
    :return:
    """
    count=1

    while count <= 5:
        turtle.forward(size)
        turtle.right(144)

        count += 1
    # 更新参数
    size += 10
    if size <= 100:
        deaw_recurssive_pentagram(size)


def main():

    turtle.penup()
    turtle.bk(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    deaw_recurssive_pentagram(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()