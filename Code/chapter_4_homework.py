if __name__ == '__main__':

    # 1
    print('# 1')
    for n in range(1, 6):
        print('{:<5}'.format(n*'*'))
    print('{:^7}'.format('(a)\n'))
    for n in range(1, 10, 2):
        print('{:^10}'.format(n*'*'))
    print('{:^10}'.format('(b)\n'))
    for n in [1, 3, 5, 3, 1]:
        print('{:^5}'.format(n*'*'))
    print('{:^7}'.format('(c)\n'))

    # 2
    print('# 2')
    num_list = [num for num in range(1, 31)]
    count = 1  # count：计数，1起
    num_list_called = []
    while count <= 10:
        print("报数：", end='')
        for i in range(1, 10):  # i：编号报号，1起
            print(i, end=' ')
        j = i * count % len(num_list) - 1  # j：编号1~30的索引，故-1
        print("编号：", num_list[j])
        num_list_called.append(num_list[j])
        count += 1
    print("离开的前10人编号为：", num_list_called)

    # 3
    print('\n# 3')


    def perfect_num(x):
        i = 1
        if x <= 0 or x % 1 != 0:
            print("输入错误，请输入正整数")  # 判断是否输入非正数或非整数
        elif x == 1:
            # print("1不是完数")
            return False
        else:
            factor_list = []
            while i < x:
                if x % i == 0:
                    factor_list.append(i)  # 真因子列表
                i += 1
            if sum(factor_list) == x:
                # print("数字{}是完数".format(x))
                return True
            else:
                # print("数字{}不是完数".format(x))
                return False


    print("1000内的所有完数为：", end='')
    for j in range(1, 1000):
        if perfect_num(j):
            print(j, end=' ')

    # 4
    print('\n\n# 4')


    def prime_num(x):
        i = 2
        if x <= 0 or x % 1 != 0:
            print("输入错误，请输入正整数")  # 判断是否输入非正数或非整数
        elif x == 1:
            # print("1不是质数")
            return False
        elif x == 2:
            # print("2是质数")
            return True
        else:
            while i < x:
                if x % i == 0:
                    # print("{}不是质数，可被{}整除".format(x, i))
                    return False
                else:
                    i += 1
                    if x == i:
                        # print("{}是质数".format(x))
                        return True


    PRIMENUM_100_1000 = []
    for j in range(100, 1000):
        if prime_num(j):
            PRIMENUM_100_1000.append(j)
    # print("100到1000范围内所有素数是：", PRIMENUM_100_1000)
    print("100到1000范围内所有素数的和是：", sum(PRIMENUM_100_1000))

    # 5
    print('\n# 5')
    opr_1 = input("请输入数字1：")  # operand, 操作数1
    opt = input("请输入运算符：")  # operator, 操作符
    opr_2 = input("请输入数字2：")  # operand, 操作数2
    exec('result = '+opr_1+opt+opr_2)
    print('运算结果为：{:.2f}'.format(result))

    # 6
    print('\n# 6')
    while True:
        a, n = map(int, input("请输入不超过9的正整数a和n：").split())
        if a <= 0 or a % 1 != 0 or n <= 0 or n % 1 != 0:
            print("输入错误，请输入正整数")  # 判断是否输入非正数或非整数
        elif a > 9 or n > 9:
            print("输入错误，请输入均小于9")  # 判断是否输入大于9
        else:
            break
    # 方法一：
    s = ''
    for i in range(1, n+1):
        if i == 1:
            s = s + i * str(a)
        else:
            s = s + '+' + i * str(a)
    print('s='+s+'='+'{}'.format(eval(s)))
    # 方法二：
    lst = ['+'+i*str(a) for i in range(1, n+1)]
    s = ''.join(lst)
    print(s[1:], '=', eval(s))

    # 7
    print('\n# 7')
    s_input = list(map(int, input("请输入一系列正整数：").split()))
    i_input = [i for i in s_input if i > 0]
    sum_i = sum([j for j in i_input if j % 2 == 1])
    print("正整数序列中奇数的和为：", sum_i)

    # 8
    print('\n# 8')
    N = int(input("请输入正整数N："))
    ar = [i/(2*i-1)*(-1)**(i-1) for i in range(1, N+1)]
    print("交错序列前{}项和为{:.3f}".format(N, sum(ar)))

    # 9
    print('\n# 9')
    x = eval(input("请输入实数x："))
    y = 1/x if x != 0 else 0
    print("f({:.1f})={:.1f}".format(x, y))

    # 10
    print('\n# 10')
    while True:
        ele_used = eval(input("请输入某用户的月用电量(千瓦时)："))
        if ele_used < 0:
            print("Invalid Value!")
        else:
            break
    if ele_used <= 50:
        ele_bills = 0.53*ele_used
    else:
        ele_bills = 0.53*50 + (0.53+0.05)*(ele_used-50)
    print("cost={:.2f} 元".format(ele_bills))
