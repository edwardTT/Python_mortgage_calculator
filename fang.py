#Add some commment
#用户输入房贷相关信息
money = int(input('贷款金额（万）：'))
year = int(input('贷款期限（年）：'))
rate = float(input('年利率（%）：'))
factor = float(input('浮动倍数：'))

month = year * 12
month_rate = rate / 100 * factor / 12
money *= 10000

month_pay = (money * month_rate * (1 + month_rate) ** month) / ((1 + month_rate) ** month - 1)
all_pay = month_pay * month

print('等额本息')
print('每月还款 %.2f' % month_pay)
print('总支付利息 %.2f' % (all_pay - money))

#计算结果
month_pay = money / month + money * month_rate
pay_down = money / month * month_rate
all_pay = ((money / month + money * month_rate) + money / month * (1 + month_rate)) / 2 * month

#输出结果
print('等额本金')
print('首月还款 %.2f' % month_pay)
print('每月递减 %.2f' % pay_down)
print('总支付利息 %.2f' % (all_pay - money))
