
def isleap(y):
    '''
    判断是否闰年
    输入年份 :param y: int
    返回真或假 :return: bool
    '''
    if y % 100 == 0:  # 整百年份
        if y % 400 == 0:  # 看是否被400整除
            return True
        else:
            return False
    else:  # 非整百年份
        if y % 4 == 0:  # 看是否被4整除
            return True
        else:
            return False


def nydsofar(y):
    '''
    计算距1900年1月1日过去了多少天
    左开右闭：不包括1900年1月1日但包括当年1月1日
    输入年份 :param y: int
    返回过去的天数 :return: int
    '''
    if y < 1900:
        print("输入年份错误！")
    else:
        days = 0
        for i in range(1901, y+1):
            days += 366 if isleap(i) else 365
        return days


def nydweek(y):
    '''
    计算当年1月1日(New Year's Day)为星期几
    输入年份 :param y: int
    返回星期几 :return: bool
    '''
    week = ['一', '二', '三', '四', '五', '六', '日']
    days = nydsofar(y)
    return week[days % 7]


def daymonth(y):
    '''
    得到每月的天数信息
    输入年份 :param y: int
    返回每月的天数 :return: dict
    '''
    if isleap(y):
        mdays = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        mdays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mdays


def daysofar(y, m, d):
    '''
    计算当年某日与当年1月1日相差的天数
    左开右闭：不包括当年1月1日但包括当年某日
    输入年份 :param y: int
    输入月份 :param m: int
    输入日期 :param d: int
    返回天数 :return: int
    '''
    mdays = daymonth(y)
    if d > mdays[m]:
        print("日期有误！")
    else:
        days = 0
        for i in range(1, m):
            days += mdays[i]
        days += d - 1  # 注意不包括当年1月1日
        return days


def dayweek(y, m, d):
    '''
    计算当年某日为星期几
    输入年份 :param y: int
    输入月份 :param m: int
    输入日期 :param d: int
    返回星期几 :return: bool
    '''
    week = ['一', '二', '三', '四', '五', '六', '日']
    week_start = nydweek(y)
    week_bias = week.index(week_start)
    days = daysofar(y, m, d)
    return week[(days+week_bias) % 7]


def printcalendar(y):
    '''
    打印当年的年历
    输入年份 :param y: int
    打印出当年年历 :return: None
    '''
    week = ['一', '二', '三', '四', '五', '六', '日']
    mdays = daymonth(y)
    for m in range(1, 13):
        print('{:^27}'.format(str(m)+' 月'))
        print("{:>23}".format("一   二  三   四  五   六  日"))
        for d in range(1, mdays[m]+1):
            if d == 1:
                for i in range(week.index(dayweek(y, m, d))):
                    print('{:>3}'.format(' '), end=' ')
                if dayweek(y, m, d) == '日':
                    print('{:>3}'.format(d))
                else:
                    print('{:>3}'.format(d), end=' ')
            else:
                if dayweek(y, m, d) == '日' or d == mdays[m]:
                    print('{:>3}'.format(d))
                else:
                    print('{:>3}'.format(d), end=' ')
        print()


if __name__ == '__main__':
    year = int(input("请输入年份："))
    print("{}年的年历如下：".format(year))
    printcalendar(year)
