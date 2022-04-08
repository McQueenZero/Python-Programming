import re

if __name__ == '__main__':

    # 1
    print('# 1')
    with open('water.txt', 'r') as w:
        water_list = w.read().splitlines()
    # print(water_list)
    acc_list = []
    # 分割出单个数值
    for acc_raw in water_list:
        acc_list.append(acc_raw.split(' '))
    # print(acc_list)
    # 计算各月用水量及合计水费
    print("{:^10}{:^32}{:^7}".format('户号', '1~12各月用水量', '合计水费'))
    for acc in acc_list:
        for i in range(1, 13):
            acc[i] = int(acc[i+1]) - int(acc[i])
        acc[13] = sum(acc[1:13])*1.05
    # 打印
    for acc in acc_list:
        for item in acc:
            if type(item) == float:
                print('{:.2f}'.format(item), end='\n')
            else:
                print(item, end=' ')

    # 2
    print('\n# 2')
    with open('freedom.txt', 'r') as f:
        para = f.read()
    # print(para)
    # 分割出单词，多个分隔符，用re包的split
    word_list = re.split("[ ,.:;!?\'\"\n]", para)
    # 用集合类型去掉重复词，并排除空和破折号
    word_dic = {word: word_list.count(word)
                for word in set(word_list)
                if word != '' and word != '--'}
    # print(word_dic)
    with open('dic.txt', 'w') as d:
        for k, v in word_dic.items():
            print(k, v, end=', ')
            # print(k, v, file=d)

    # 3
    print('\n\n# 3')

    def sumfrac(n):
        addend = []
        for i in range(1, n + 1):
            if i == 1:
                addend.append('1')
            elif i%2 == 1:
                addend.append('+1/{}'.format(i))
            else:
                addend.append('-1/{}'.format(i))
        print(''.join(addend), end='=')  # 列表连成字符串的表达式
        addend = map(eval, addend)
        print('{:.6f}'.format(sum(addend)))

    n = eval(input("Please input a number:"))
    sumfrac(n)

    # 4
    print('\n# 4')

    # 计算阶乘
    def factorial(n):
        n = int(n)
        if n <= 1:
            return 1
        else:
            return n*factorial(n-1)

    # 给出加数表达式并计算
    def nexp(n):
        addstr = 'e='
        addend = []
        for i in range(n+1):
            if i == 0:
                addstr += '1'
            else:
                addstr += '+1/{}!'.format(i)
            addend.append(1/factorial(i))
        print(addstr, end='=')
        print('{:.15f}'.format(sum(addend)))

    n = eval(input("Please input a number:"))
    nexp(n)

    # 5
    print('\n# 5')

    def isdaff3(n):
        if 100 <= n < 1000:  # 判断是否三位数
            n_str = str(n)
            n_sum = 0
            for dig in n_str:
                n_sum += int(dig)**3
            if n == n_sum:
                return True
            else:
                return False
        else:
            print("Not a 3-digit number!")

    def daff3():
        for num in range(100, 1000):
            if isdaff3(num):
                print(num, end=' ')

    print("所有的三位水仙数：", end='')
    daff3()
    print()

    # 6
    print('\n# 6')

    def ispali3(n):
        if 100 <= n < 1000:  # 判断是否三位数
            n_str = str(n)
            n_pali = int(n_str[::-1])
            if n == n_pali:
                return True
            else:
                return False
        else:
            print("Not a 3-digit number!")

    def pali3():
        for num in range(100, 1000):
            if ispali3(num):
                print(num, end=' ')

    print("所有的三位回文数：", end='')
    pali3()
    print()

    # 7
    print('\n# 7')

    def fibo(n):
        n = int(n)
        if n <= 0:
            return 0
        elif n <= 2:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)

    n = eval(input("请输入项数:"))
    value = fibo(n)
    print("f({})的值是{}".format(n, value))

    # 8
    print('\n# 8')
    s, le = input("请输入一个字符串和一个字母:").split(' ')

    def strcd(s, le):
        s_result = ''
        for letter in s:
            if letter != le:
                s_result += letter
        return s_result, s.count(le)

    s_out, s_c = strcd(s, le)
    print("结果字符串是：", s_out)
    print("输入字母在原字符串中出现次数是：", s_c)

    # 9
    print('\n# 9')
    m, d = map(eval, input("请输入月, 日:").split(','))

    def constellation(m, d):
        if m == 3:
            return '白羊座' if d >= 21 else '双鱼座'
        elif m == 4:
            return '金牛座' if d >= 20 else '白羊座'
        elif m == 5:
            return '双子座' if d >= 21 else '金牛座'
        elif m == 6:
            return '巨蟹座' if d >= 22 else '双子座'
        elif m == 7:
            return '狮子座' if d >= 23 else '巨蟹座'
        elif m == 8:
            return '处女座' if d >= 23 else '狮子座'
        elif m == 9:
            return '天秤座' if d >= 23 else '处女座'
        elif m == 10:
            return '天蝎座' if d >= 24 else '天秤座'
        elif m == 11:
            return '射手座' if d >= 23 else '天蝎座'
        elif m == 12:
            return '摩羯座' if d >= 22 else '射手座'
        elif m == 1:
            return '水瓶座' if d >= 20 else '摩羯座'
        elif m == 2:
            return '双鱼座' if d >= 19 else '水瓶座'
        else:
            print("月份错误！")

    print("星座：", constellation(m, d))
