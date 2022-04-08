import random
import copy
import json
import collections

if __name__ == '__main__':

    # 1
    print('# 1')
    # 方法一：
    mul_table_1 = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i <= j:
                mul_table_1.append('{}*{}={}'.format(i, j, i * j))
    print(mul_table_1)
    # 方法二：
    mul_table_2 = ['{}*{}={}'.format(i, j, i * j) for i in range(1, 10) for j in range(1, 10) if i <= j]
    print(mul_table_2)

    temp = '1'
    for item in mul_table_2:
        if temp == item[0]:
            print('{:6}'.format(item), end=' ')
        else:
            print()
            print('{:6}'.format(item), end=' ')
        temp = item[0]

    # 2
    print('\n# 2')
    a = ['a', 'b', 'c']
    b = ['.jpg', '.png', '.bmp']
    # 方法一：
    file_list_1 = []
    for i in a:
        if i != 'a':
            for j in b:
                if j != '.jpg':
                    file_list_1.append(i + j)
    print(file_list_1)
    # 方法二：
    file_list_2 = [i+j for i in a if i != 'a' for j in b if j != '.jpg']
    print(file_list_2)

    # 3
    print('\n# 3')
    score = {'Amy': 45, 'Bob': 50, 'Cathy': 62, 'David': 45, 'Eason': 63, 'Fred': 78, 'George': 72, 'Helen': 82,
             'Ivan': 100, 'Jason': 98, 'Kevin': 0, 'Laura': 100}
    score_0_9 = {key: value for key, value in score.items() if 0 <= value < 10}
    for i in range(1, 10):
        exec("score_"+str(i)+"0_"+str(i)+"9 = {key: value for key, value in score.items() "
                                         "if "+str(i)+"0 <= value < "+str(i+1)+"0}")
        # 用exec()的方式生成score_10_19~score_90_99几个变量
    score_100 = {key: value for key, value in score.items() if value == 100}
    for i in range(11):
        if i == 0:
            print("分数段0~9分：", end='')
            print(list(score_0_9.keys()))
        elif i < 10:
            print("分数段{0}0~{0}9分：".format(i), end='')
            eval("print(list(score_"+str(i)+"0_"+str(i)+"9.keys()))")
            # 用eval()的方式打印score_10_19~score_90_99几个变量
        else:
            print("分数段100分：", end='')
            print(list(score_100.keys()))

    # 4
    print('\n# 4')
    random.seed(0x1010)
    code_in = 'abcdefghijklmnopqrstuvwxyz' \
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
              '1234567890' \
              '!@#$%^&*'
    initial_list = []  # 10个密码的首字母组成的列表
    code_out_list = []  # 10个密码组成的列表
    for i in range(10):
        code_out = ''
        for j in range(10):
            if j == 0:
                initial = random.choice(code_in)
                if initial in initial_list:
                    j -= 1  # 若首字母重复则重新生成
                else:
                    initial_list.append(initial)
                    code_out += initial_list[-1]
            else:
                code_out += random.choice(code_in)
        code_out_list.append(code_out)
    # print(initial_list)
    for code in code_out_list:
        print(code)

    # 5
    print('\n# 5')
    sen = input("请输入一句英文：").split()
    sen_set = set(sen)
    for word in sen_set:
        print(word, sen.count(word))

    # 6
    print('\n# 6')
    while True:
        N = int(input("请输入生成整数的个数N："))
        if N > 1000:
            print("非法，请重新输入")
        else:
            break
    RI_list = []
    for i in range(N):
        RI = random.randint(1, 1000)
        RI_list.append(RI)
    RI_set = set(RI_list)
    RI_list_out = list(RI_set)
    RI_list_out.sort()
    print(RI_list_out)

    # 7
    print('\n# 7')
    lst = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
    lst[0][1][2]['k1'][0] = 'TT'
    lst[0][1][2]['k1'][1] = '100'
    lst[0][1][2]['k1'][2] = 101
    print(lst)
    lst = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
    lst[-1][-2][-2]['k1'][-3] = 'TT'
    lst[-1][-2][-2]['k1'][-2] = '100'
    lst[-1][-2][-2]['k1'][-1] = 101
    print(lst)

    lst = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]

    # 递归拆包(拆列表)，根据数据类型判断
    def inner_value(var, v_old, v_new):
        for item in var:
            if type(item) is list:
                return inner_value(item, v_old, v_new)
            elif type(item) is dict:
                return inner_value(item.values(), v_old, v_new)
            else:
                if v_old == item:
                    var[var.index(v_old)] = v_new
                else:
                    continue


    inner_value(lst, 'tt', 'TT')
    inner_value(lst, 3, '100')
    inner_value(lst, '1', 101)
    print(lst)

    # 8
    print('\n# 8')
    RI_list = []
    for i in range(1000):
        RI = random.randint(20, 100)
        RI_list.append(RI)
    RI_set = set(RI_list)
    print('数字', '重复次数')
    for number in RI_set:
        print(number, RI_list.count(number))

    # 9
    print('\n# 9')
    m1 = {'a': 1, 'b': 2, 'c': 1}
    m2 = {}
    for k, v in m1.items():
        m2.setdefault(v, []).append(k)
    print(m2)

    # 10
    print('\n# 10')
    raw_list = [
        {"id": 1, "pid": 0},
        {"id": 2, "pid": 0},
        {"id": 3, "pid": 1},
        {"id": 4, "pid": 3},
        {"id": 5, "pid": 1},
        {"id": 6, "pid": 2},
        {"id": 7, "pid": 4},
    ]

    # 方法一：
    temp_list = copy.deepcopy(raw_list)  # 各层深拷贝

    def dict_tree(lst, out):
        node_list = []
        while lst:
            for p in lst:
                for c in lst:
                    if p['id'] == c['pid'] and c not in node_list:
                        # 根据父节点-子节点id，加入子字典
                        p.setdefault('child', []).append(c)
                    if p['id'] == c['pid'] or c['pid'] == 0 and c not in node_list:
                        # 加入树的节点统计（且防止重复加入）
                        node_list.append(copy.deepcopy(c))
                if p['pid'] == 0:
                    # 根节点添加
                    out.append(lst.pop(lst.index(p)))
                else:
                    # 枝、叶节点去除
                    if 'child' not in p.keys():
                        # 叶节点添加'child'为空list
                        p['child'] = []
                    for node in node_list:
                        # 与已经加入树的节点判断后去除
                        if p['id'] == node['id']:
                            lst.remove(p)
                            break
        return out

    out_list = dict_tree(temp_list, [])
    print(json.dumps(out_list, indent=4))  # 格式化输出

    # 方法二：
    temp_list = copy.deepcopy(raw_list)  # 各层深拷贝

    def list_dict_tree(data_list):
        tree_list = []
        data_list_dict = collections.defaultdict(list)  # 当字典里的key不存在但被查找时，返回的不是key error 而是一个默认值
        for item in data_list:
            if item.get("pid") == 0:  # 给0级创建child键，产生第一个分支
                item["child"] = []
                tree_list.append(item)

            deep_item = copy.deepcopy(item)  # 深拷贝产生一个独立的个体
            deep_item["child"] = []
            data_list_dict[item.get("pid")].append(deep_item)  # pid级别目录下存在的

        recursion(tree_list, data_list_dict)
        return tree_list


    def recursion(data_list, data_list_dict):
        """
        递归
        :param data_list:
        :param data_list_dict:
        :return:
        """
        for item in data_list:  # 当最后一个data_list 为[] for循环不执行，自动结束
            id = item.get("id")  # get当前文件id
            if id in data_list_dict:  # 判断当前id是不是data_list_dict中的pid级别目录
                item["child"].extend(data_list_dict.get(id))  # list用extend，dict用update
            recursion(item.get("child"), data_list_dict)

    tree_list = list_dict_tree(temp_list)
    print(json.dumps(out_list, indent=4))  # 格式化输出
