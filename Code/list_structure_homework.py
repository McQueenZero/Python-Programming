# 作者：赵敏琨
# 学号：2018302068

if __name__ == '__main__':

    # 01
    lt = []
    print("01-1. 定义空列表lt：", lt)

    for i in range(1, 6):
        lt.append(i)
    print("01-2. 向lt新增5个元素：", lt)

    lt[1] = 6
    print("01-3. 修改lt中第2个元素为6：", lt)

    lt.insert(1, 7)
    print("01-4. 向lt中第2个位置增加一个元素7：", lt)

    del lt[0]
    print("01-5. 从lt中第1个位置删除一个元素：", lt)

    del lt[0:3]
    print("01-6. 删除lt中第1-3位置元素：", lt)

    if 0 in lt:
        print("01-7. lt中包含数字0")
    else:
        print("01-7. lt中不包含数字0")

    lt.append(0)
    print("01-8. 向lt新增数字0：", lt)

    # 写循环是为了处理列表lt中含有多个数字0的情况
    # lt.clear()
    # lt = [0, 5, 4, 0, 8, 1, 2, 6, 8, 0, 4]
    print("01-9. 数字0在lt中的索引为：", end='')
    z_i = 0  # 初始化索引
    while True:
        if 0 in lt[z_i:]:  # 判断剩下的列表还有没有0
            z_i += lt[z_i:].index(0)  # 返回第一个0在剩下列表中的索引再修正
            print(z_i, end=' ')  # 打印第一个0在lt中的索引
            z_i += 1  # 向前走一步
        else:
            print()  # 输出换行符
            break

    print("01-10. lt的长度：", len(lt))

    print("01-11. lt中最大元素：", max(lt))

    lt.clear()
    print("01-12. 清空lt：", lt)

    lt = [1, 2, 3, 4, 5]
    lt[1:3] = [10, 11]
    print("01-13. 对列表lt中第2-4位置替换成10, 11两元素：", lt)

    # 02
    print()
    while True:
        shoes_n = eval(input("02. 请输入购买数量："))
        if shoes_n < 1 or shoes_n % 1 != 0:
            print("非法，请重新输入！")
        else:
            break
    shoes_p = shoes_n * 160  # shoes_number/price
    if 2 <= shoes_n <= 4:
        shoes_p *= 0.9
    elif 5 <= shoes_n <= 9:
        shoes_p *= 0.8
    elif shoes_n >= 10:
        shoes_p *= 0.7
    print("02. 总额为：", int(shoes_p))

    # 03
    print('''
03. 以下代码：
count = 0
while count < 3:
    print(count, "is less than 3")
    count = count + 1
else:
    print(count, "is not less than 3")''')
    print('''03. 输出的结果是：
0 is less than 3
1 is less than 3
2 is less than 3
3 is not less than 3
''')

    # 04
    result = ((3 ** 4 + 5 * 6 ** 7) / 8) ** 0.5
    print("04. 表达式的结果为：{:.3f}".format(result))

    # 05
    print()
    GUA_1 = 0x4DC0
    print("05. 第1卦：", chr(GUA_1), end='，')
    GUA_51 = 0x4DC0 + 50
    print("第51卦：", chr(GUA_51))
    print("05. 二进制{0:b}、十进制{0:d}、八进制{0:o}、十六进制{0:X}".format(GUA_51))

    # 06
    print()
    print("06. 文本如下：")
    for i in range(10, 101, 10):
        print("{0:>3}%@{1:<}".format(i, "=="*int(i/10)))

    # 07
    print()
    s = "学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？"
    n = 0  # 汉字个数
    m = 0  # 标点符号个数
    for cha in s:
        if 0x4e00 <= ord(cha) <= 0x9fa5:
            n += 1
        else:
            m += 1
    print("07. 字符数为{}，标点符号数为{}。".format(n, m))

    # 08
    print()
    N = int(input("08. 请输入一个整数："))
    if N % 2 == 0:
        N_S = N + 1  # 输入的是偶数
    else:
        N_S = N  # 输入的是奇数
    N_sum = 0
    for i in range(N_S, N+100, 2):
        N_sum += i
    print("08. 整数{0}到整数{0}+100之间所有奇数的数值和为：{1}".format(N, N_sum))
