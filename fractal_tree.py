"""
    功能: 利用递归绘制分形树
    版本: 1.0
    日期: 03/06/2018
    加入循环操作
    使用迭代绘制
"""
import turtle


def deaw_branche(branch_lengh):
    """
    :param branch_lengh:
    :return:
    """

    if branch_lengh > 5:
        if branch_lengh < 30:
            turtle.pencolor('blue')

        # 绘制右侧树枝
        turtle.forward(branch_lengh)
        print('向前', branch_lengh)
        turtle.right(20)
        print('右转20°')
        deaw_branche(branch_lengh-15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转40°')
        deaw_branche(branch_lengh - 15)
        # 返回之前的树枝
        turtle.right(20)
        print('右转20°')
        if branch_lengh > 30:
            turtle.pencolor('red')
        turtle.backward(branch_lengh)
        print('返回', branch_lengh)



def main():

    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.pensize(3)
    deaw_branche(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()