# import random
#
# # 姓和名的列表
# surnames = ["张", "李", "王", "赵", "周"]
# first_names = ["伟", "芳", "娜", "强", "敏"]
# # 生成字典，键由姓和随机名构成，值为0-100的随机整数
# name_scores={}
# for surname in surnames:
#     name_scores = {surname + random.choice(first_names): random.randint(0, 100)}
#
# #name_scores = {surname + random.choice(first_names): random.randint(0, 100) for surname in surnames}
# # 输出结果
# print(name_scores)



# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

#
# a = 100 #全局变量
#
# def f1():
#     global a #如果要在函数内改变全局变量的值，增加 global 关键字声明
#     print(a) #打印全局变量 a 的值
#
# f1()
# a = 300
# print(a)


# dp=[5 for i in range(5)]
#
# print(dp)
#
#
# def numWays(n):
#     if n <= 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         dp = [0 for i in range(n)]
#         dp[0] = 1
#         dp[1] = 2
#         i = 2
#         while i < n:  # 循环计算每个dp[i]的值
#             dp[i] = dp[i - 1] + dp[i - 2]
#             i += 1
#         a = int(dp[i - 1])
#         return a
# print(numWays(4))

# import os
# os.system("notepad.exe")
# import os
# os.system("ping www.baidu.com")


#print(4+spam*3)

#
#
# def get_score():
#     # 尝试接收用户输入并转换为整数
#     try:
#         score = int(input("请输入你的分数（0-100）："))
#     except ValueError:
#         # 如果输入不能转换为整数，抛出异常
#         raise ValueError("输入错误！请输入一个整数。")
#
#     # 判断分数是否在0到100之间
#     if 0 <= score <= 100:
#         print("你的成绩是：", score)
#     else:
#         # 如果分数不在这个范围内，抛出异常
#         raise ValueError("分数必须在0到100之间！")
#
# # 调用函数
# try:
#     get_score()
# except Exception as e:
#     print(e)


# # step 1 引用
# import matplotlib.pyplot as plt
# import numpy as np
# # step 2 准备数据
# x=np.arange(-np.pi,np.pi,0.1)
# y=np.sin(x)
# # step 3  制图
# plt.plot(x,y,'b')     # ‘b’代表使用蓝色画曲线
# # step 4 显示图形
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# data = np.random.randint(1, 11, 5)
# plt.pie(data, explode = [0,0,0.2, 0, 0])  # explode的第三个参数为0.2 ，意味着对应饼块被拖出饼plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.rcParams['font.family'] = 'sans-serif'
# mpl.rcParams['font.sans-serif'] = [u'SimHei']
# data = np.random.randint(1, 10, 10)
# x = np.arange(len(data))
# plt.plot(x, data, color = 'r')
# plt.bar(x, data, alpha = .5, color = 'b',width=0.2)
# plt.show()



# n_angles = 36
# n_radii = 8
# radii = np.linspace(0.125, 1.0, n_radii)
# angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
# angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
# # angles[..., np.newaxis] 将angles转置，将每个元素转化成一个列表
# x = np.append(0, (radii * np.cos(angles)).flatten())
# y = np.append(0, (radii * np.sin(angles)).flatten())
# # flatten作用是将矩阵的行之间首尾相接连接成一个一维矩阵
# z = np.sin(-x * y)
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
# plt.show()


# num1 = list(range(1, 5 * 10, 5))
# #ending
# print(num1)

#
# from matplotlib import pyplot as plt
# from matplotlib import animation
# import numpy as np
# # 首先建立图形对象figure，坐标轴对象ax1和ax2，画图元素line1和line2
# fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1,xlim=(0, 2), ylim=(-4, 4))
# ax2 = fig.add_subplot(2,1,2,xlim=(0, 2), ylim=(-4, 4))
# line, = ax1.plot([], [], lw=1)
# line2, = ax2.plot([], [], lw=1)
#
# def init():
#   line.set_data([], [])
#   line2.set_data([], [])
#   return line,line2
# def animate(i): # 参数i随FuncAnimation的frame参数改变，在0-49周而往复变化
#   x = np.linspace(0, 2, 100)
#   y = np.sin(2 * np.pi * (x - 0.01 * i))
#   line.set_data(x, y)
#   x2 = np.linspace(0, 2, 100)
#   y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))
#   line2.set_data(x2, y2)
#   return line,line2
# anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=10)
# plt.show()
#
#
# def multiply(n):
#   num2 = list(range(n))
#   num1 = list(range(1, 5 * n, 5))
#   mul = []
#   for i in range(len(a)):
#     mul.append(num2[i] ** 2 + num1[i] ** 3)
#
#
# #return (mul)
# print(multiply(10))  # 运行中循环10次
#
# #使用NumPy的代码实例
# import numpy as np
# #用numpy函数创建num1,num2,mul
# def pynum(n):
#     num1 = np.arange(1, 5 * n, 5)
#     num2 = np.arange(n)
#     mul = num2 ** 2 + num1 ** 3
#     return(mul)
# print(pynum(10)) #运行中没有进行循环操作
#
#
# import datetime  #datetime模块提供了用于以简单或复杂的方式操作日期和时间的类
# dt = datetime.datetime.now()
# multiply(10000)
# dtend = datetime.datetime.now()-dt
# print("Python程序运行时间:",dtend.total_seconds()*1000,"毫秒")
# dt1 = datetime.datetime.now()
# pynum(10000)
# dtend1 = datetime.datetime.now()-dt1
# print("NumPy程序运行时间:",dtend1.total_seconds()*1000,"毫秒")
#
#
#
# [14.1, 14.3, 14.5, 14.2, 14.6, 14.8, 15.0, 15.2, 15.3, 15.5, 15.6, 15.4, 15.7, 15.8, 16.0, 16.1, 16.2, 16.4, 16.5, 16.8, 17.0]

# def multiply(n):
#   num2 = list(range(n))
#   num1 = list(range(1, 5 * n, 5))
#   mul = []
#   for i in range(len(n)):
#     mul.append(num2[i] ** 2 + num1[i] ** 3)
#   return (mul)
#
# print(multiply(10))  # 运行中循环10次
# import numpy as np
# #用numpy函数创建num1,num2,mul
# def pynum(n):
#     num1 = np.arange(1, 5 * n, 5)
#     num2 = np.arange(n)
#     mul = num2 ** 2 + num1 ** 3
#     return(mul)
# print(pynum(10)) #运行中没有进行循环操作
# import datetime  #datetime模块提供了用于以简单或复杂的方式操作日期和时间的类
# dt = datetime.datetime.now()
# multiply(10000)
# dtend = datetime.datetime.now()-dt
# print("Python程序运行时间:",dtend.total_seconds()*1000,"毫秒")
# dt1 = datetime.datetime.now()
# pynum(10000)
# dtend1 = datetime.datetime.now()-dt1
# print("NumPy程序运行时间:",dtend1.total_seconds()*1000,"毫秒")
#
#
#
#
# A = np.array([[1, 2],
#               [3, 4]])
# B = np.array([[5, 6],
#               [7, 8]])
# A * B
#
# np.dot(A, B)
#
#




#
#
# import pandas as pd
# URl='https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json'
# df=pd.read_json(URl)
# print(df)







num = int(input("请输入一个不多于5位的正整数："))
# 知识点：input()函数用于从键盘接收输入，int()函数将输入的字符串转换为整数。
# 求出它是几位数
digit_count = len(str(num))
print(f"这是一个{digit_count}位数。")
# 知识点：str()函数将数字转换为字符串，len()函数获取字符串的长度。
# 分别输出每一位数字
for digit in str(num):
    print(digit)
# 知识点：for循环用于遍历序列中的每个元素。
# 按逆序输出每位数字
reversed_digits = str(num)[::-1]
print(reversed_digits)
