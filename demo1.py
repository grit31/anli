# # # # # str1=input('请您输入一个字符串')
# # # # # print(str1)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # magicians = ['alice', 'david', 'carolina']
# # # # # for magician in magicians:
# # # # #      print(magician+ ", that was a great trick!")
# # # # #      print("I can't wait to see your next trick, " + magician.title() + ".\n")
# # # # #
# # # # #
# # # # #
# # # # # cars = ['bmw', 'audi', 'toyota', 'subaru']
# # # # # print(cars)
# # # # # cars.sort()
# # # # # print(cars)
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # import random
# # # # #
# # # # # # 姓和名的列表
# # # # # surnames = ["张", "李", "王", "赵", "周"]
# # # # # first_names = ["伟", "芳", "娜", "强", "敏"]
# # # # #
# # # # # # 生成字典，键由姓和随机名构成，值为0-100的随机整数
# # # # # name_scores = {surname + random.choice(first_names): random.randint(0, 100) for surname in surnames}
# # # # #
# # # # # # 输出结果
# # # # # print(name_scores)
# # # #
# # # # import numpy as np
# # # # def sigmod(x):
# # # #     return  1/(1+np.exp(-x))
# # # #
# # # # print(sigmod(4))
# # # # print(np.exp(1))
# # #
# # #
# # # import random
# # #
# # # # 生成两个集合，每个集合包含最多200个随机数
# # # set1 = {random.randint(0, 500) for _ in range(200)}
# # # set2 = {random.randint(0, 500) for _ in range(200)}
# # #
# # # # 找出两个集合中不相同的数据
# # # unique_to_set1 = set1 - set2
# # # unique_to_set2 = set2 - set1
# # #
# # # # 找出两个集合中相同的数据
# # # common_elements = set1 & set2
# # #
# # #
# # # print(set1)
# # # # # 显示结果
# # # # print("集合1中独有的数据：", unique_to_set1)
# # # # print("集合2中独有的数据：", unique_to_set2)
# # # # print("两个集合中共有的数据：", common_elements)
# #
# # # import numpy as np
# # # def search(x,nums):
# # #     a=np.array(nums)
# # #     for r in range(a.shape[0]):
# #
# #
# # import matplotlib.pyplot as plt
# #
# # # 准备数据
# # x = [1, 2, 3, 4, 5]  # X轴数据
# # y = [2, 3, 5, 7, 11] # Y轴数据
# # # 创建图形和轴
# # fig, ax = plt.subplots()
# # # 绘制线图
# # ax.plot(x, y, label='Sample Data', marker='o')  # 'o'代表圆点标记每个数据点
# # # # # 添加标题和轴标签
# # # ax.set_title('Simple Line Plot')  # 图表标题
# # # ax.set_xlabel('X Axis')  # X轴标签
# # # ax.set_ylabel('Y Axis')  # Y轴标签
# # # # 显示图例
# # # ax.legend()
# # # # 保存图像到文件
# # # #plt.savefig('/mnt/data/Simple_Line_Plot.png')
# # # plt.show()
# # # plt.close()  # 关闭图形，释放内存
# #
# # #
# # # import matplotlib.pyplot as plt
# # # # 准备数据
# # # heights = [150, 160, 165, 170, 175, 180, 185]  # 身高（cm）
# # # weights = [50, 55, 60, 68, 70, 75, 80]        # 体重（kg）
# # # # 创建图形和轴
# # # fig, ax = plt.subplots()
# # # # 绘制散点图
# # # ax.scatter(heights, weights, color='blue', marker='o')  # 使用蓝色圆点标记
# # # # 添加标题和轴标签
# # # ax.set_title('Height vs. Weight Scatter Plot')  # 图表标题
# # # ax.set_xlabel('Height (cm)')  # X轴标签
# # # ax.set_ylabel('Weight (kg)')  # Y轴标签
# # # # 显示图形
# # # plt.show()
# #
# #
# # from turtle import *
# # from math import *
# #
# #
# # # 高级椭圆参数方程（颜色），sita为逆时针旋转角度
# # def ty_c(x, y, sita, a, b, p, q, c):
# #     fillcolor(c)
# #     si = 2 * pi / 100
# #     penup()
# #     goto(x + a * cos(sita), y + a * sin(sita))
# #     pendown()
# #     t = 0
# #     for i in range(201):
# #         if i * si + sita <= p:
# #             penup()
# #             goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita) \
# #                  , y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
# #             pendown()
# #         elif p <= i * si + sita <= q + 2 * pi / 100:
# #             if t == 0:
# #                 begin_fill()
# #                 t = 1
# #             goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita) \
# #                  , y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
# #     end_fill()
# #
# #
# # # 高级椭圆方程
# # def ty(x, y, sita, a, b, p, q):
# #     si = 2 * pi / 100
# #     penup()
# #     goto(x + a * cos(sita), y + a * sin(sita))
# #     pendown()
# #     for i in range(201):
# #         if i * si + sita < p:
# #             penup()
# #             goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita) \
# #                  , y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
# #             pendown()
# #         elif p <= i * si + sita <= q + 2 * pi / 100:
# #             goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita) \
# #                  , y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
# #
# #
# # speed(0)
# # hideturtle()
# # # 篮球
# # pensize(10)
# # pencolor('black')
# # ty_c(350, -267, 0, 161, 161, 0, 2 * pi, '#ff9900')
# # ty(350, -267 + 161 + 50, 0, 161, 161, 7 * pi / 6 + pi / 12, 11 * pi / 6 - pi / 12)
# # ty(350, -267 - 161 - 50, 0, 161, 161, pi / 6 + pi / 12, 5 * pi / 6 - pi / 12)
# # ty(350, -267 + 161 + 330, 0, 500, 500, 8.5 * pi / 6, 9.5 * pi / 6)
# # # 脸
# # pensize(20)
# # ty_c(0, 0, 0, 657 / 2, 576 / 2, 0, 2 * pi, '#ffcc00')
# # # 眼睛
# # pensize(22)
# # ty_c(55, 52, 0, 106, 104, 0, 2 * pi, 'white')
# # ty_c(-165, 60, 0, 101, 99, 0, 2 * pi, 'white')
# # pensize(20)
# # ty_c(4, 79, 0, 14, 14, 0, 2 * pi, 'black')
# # ty_c(-201, 80, 0, 14, 14, 0, 2 * pi, 'black')
# # # 嘴巴
# # pensize(12)
# # ty_c(-66, -76, 0, 102, 62, 0, 2 * pi, '#ff6600')
# # penup()
# # goto(-155, -50)
# # pendown()
# # goto(-134, -64)
# # goto(-115, -74)
# # goto(-90, -82)
# # goto(-67, -86)
# # goto(-47, -85)
# # goto(-25, -82)
# # goto(0, -77)
# # goto(15, -66)
# # goto(25, -55)
# # # 腮红
# # pensize(1)
# # pencolor('red')
# # ty_c(-256, -90, 15 * pi / 180, 49, 66, 0, 2 * pi + 15 * pi / 180, 'red')
# # ty_c(201, -105, 0, 73, 75, 0, 2 * pi, 'red')
# # # 领口
# # color('black', 'black')
# # pensize(10)
# # penup()
# # goto(-275, -227)
# # pendown()
# # begin_fill()
# # goto(-241, -209)
# # goto(-189, -233)
# # goto(-166, -260)
# # goto(-127, -272)
# # goto(-88, -252)
# # goto(-49, -233)
# # goto(-19, -227)
# # goto(51, -237)
# # goto(108, -242)
# # goto(168, -242)
# # goto(210, -233)
# # goto(250, -206)
# # goto(252, -254)
# # goto(216, -269)
# # goto(-13, -353)
# # goto(-65, -362)
# # goto(-109, -356)
# # goto(-178, -317)
# # goto(-214, -296)
# # goto(-246, -266)
# # goto(-272, -245)
# # goto(-275, -227)
# # end_fill()
# # # 衣服
# # penup()
# # goto(-244, -287)
# # pendown()
# # begin_fill()
# # goto(-269, -314)
# # goto(-310, -405)
# # goto(-304, -410)
# # goto(-21, -416)
# # goto(317, -410)
# # goto(331, -398)
# # goto(323, -381)
# # goto(319, -356)
# # goto(315, -320)
# # goto(275, -266)
# # goto(263, -257)
# # pensize(15)
# # pencolor('#c0c0c0')
# #
# # goto(252, -254)
# # goto(216, -269)
# # goto(-13, -353)
# # pensize(13)
# # goto(-65, -362)
# # goto(-109, -356)
# # pensize(10)
# # goto(-178, -317)
# # goto(-214, -296)
# # goto(-246, -284)
# # end_fill()
# # # 肩带
# # penup()
# # goto(-206, -310)
# # pendown()
# # pensize(30)
# # goto(-183, -363)
# # goto(-180, -384)
# # goto(-184, -414)
# #
# # penup()
# # goto(229, -285)
# # pendown()
# # goto(203, -360)
# # pensize(34)
# # goto(190, -415)
# #
# # penup()
# # goto(-115, -360)
# # pendown()
# # pensize(8)
# # goto(-96, -411)
# # goto(-75, -413)
# # goto(18, -371)
# # goto(69, -341)
# # goto(105, -325)
# # pensize(12)
# # goto(177, -297)
# # # 中分
# # pencolor('#808080')
# # pensize(1)
# # penup()
# # goto(67, 393)
# # pendown()
# # fillcolor('#808080')
# # begin_fill()
# # goto(43, +419)
# # goto(13, +431)
# # goto(-96, +426)
# # goto(-156, +402)
# # goto(-239, +336)
# # goto(-277, +300)
# # goto(-307, +263)
# # goto(-372, +153)
# # goto(-383, +101)
# # goto(-373, +57)
# # goto(-339, +38)
# # goto(-298, +40)
# # goto(-278, +61)
# # goto(-236, +74)
# # goto(-176, +103)
# # goto(-163, +128)
# # goto(-135, +224)
# # goto(-95, +265)
# # goto(-64, +271)
# # goto(-30, +253)
# # goto(22, +269)
# # goto(61, 268)
# # goto(75, 202)
# # goto(93, 132)
# # goto(108, 71)
# # goto(136, 31)
# # goto(171, 4)
# # goto(236, -10)
# # goto(277, -10)
# # goto(323, -25)
# # goto(363, -61)
# # goto(404, -35)
# # goto(423, 14)
# # goto(453, 71)
# # goto(457, 120)
# # goto(441, 170)
# # goto(398, 227)
# # goto(331, 285)
# # goto(283, 323)
# # goto(232, 360)
# # goto(168, 396)
# # goto(122, 416)
# # goto(87, 406)
# # goto(67, 393)
# # end_fill()
# # pencolor('black')
# # pensize(4)
# # goto(-30, +253)
# # done()
# #
# #
# # import numpy as np
# # A = np.array([[1, 2],
# #               [3, 4]])
# # B = np.array([[5, 6],
# #               [7, 8]])
# #
# # print(A * B)
# #
# # print(np.dot(A, B))
# #
#
# # import numpy as np
# # # a = np.array([[1, 2, 3],
# # #              [4, 5, 6],
# # #              [7, 8, 9]])
# # # b = np.array([1, 2, 3])
# # #
# # # print(a + np.tile(b, (3, 1)))
# #
# # a = np.array([1.1, 2.2])
# # print(a)
# # b = np.array([1.1, 2.2], dtype = np.int64)
# #
# # print(b)
#
#
# # for i in range(5):
# #     i+=1
# #     print(i)
# #
# #
# # import random
# # import math
# #
# # # 生成5到20之间的随机实数作为半径
# # radius = round(random.uniform(5, 20), 3)
# #
# # # 计算球的体积
# # volume = (4/3) * math.pi * (radius ** 3)
# #
# # # 格式化输出半径和体积
# # print(f"{radius:>15.3f}")  # 半径，右对齐，占15列，保留3位小数
# # print(f"{volume:>15.3f}")  # 体积，右对齐，占15列，保留3位小数
# #
#
#
#
#
#
# # # 定义两个列表，元素个数大于10
# # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # list2 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# #
# # # 合并两个列表
# # combined_list = list1 + list2
# #
# # # 截取第8到第15个元素（Python索引从0开始，所以是7到14）
# # selected_elements = combined_list[7:15]
# #
# # # 输出结果
# # print(selected_elements)
#
#
#
#
# # # 定义原始列表
# # original_list = [1, 3, 4, 6, 6, 7, 8, 8, 10, 21, 22, 22]
# #
# # # 使用列表推导式去除重复元素，同时过滤出小于10的元素
# # unique_filtered_list = [x for n, x in enumerate(original_list) if x < 10 and original_list.index(x) == n]
# #
# # # 输出结果
# # print(unique_filtered_list)
#
# #
# #
# # # 从键盘输入一个不多于5位的正整数
# # number = int(input("请输入一个不多于5位的正整数："))
# #
# # # 1) 求出它是几位数
# # digit_count = len(str(number))
# # print(digit_count)
# #
# # # # 2) 分别输出每一位数字
# # # print("每一位数字为：")
# # # while number > 0:
# # #     digit = number % 10  # 获取当前最低位的数字
# # #     print(digit)
# # #     number //= 10  # 去掉最低位
# #
# #
# # # 2) 从高到低输出每一位数字
# # print(f"它是{digit_count}位数。")
# #
# # # 从最高位开始输出每一位数字
# # temp_number = number
# # while temp_number > 0:
# #     digit = temp_number % 10  # 获取当前最低位的数字
# #     print(digit, end=' ')  # 输出当前位数字，后面跟一个空格而不是换行
# #     temp_number //= 10  # 去掉最低位
# #
# # # # 3) 按逆序输出每位数字
# # # print("逆序输出每位数字：")
# # # reversed_number = 0
# # # while number > 0:
# # #     reversed_number = reversed_number * 10 + number % 10
# # #     number //= 10
# # # print(reversed_number)
#
#
# # def remove_duplicates_from_tuple(input_tuple):
# #     # 使用集合来去除重复元素
# #     unique_elements = set(input_tuple)
# #     # 将集合转换回列表
# #     unique_list = list(unique_elements)
# #     return unique_list
# #
# # # 示例使用
# # input_tuple = (1, 2, 2, 3, 4, 4, 4, 5)
# # result = remove_duplicates_from_tuple(input_tuple)
# # print(result)
#
#
# # # 定义两个长度相同的元组，存放动物名和年龄
# # animals = ('Dog', 'Cat', 'Elephant', 'Giraffe')
# # ages = (4, 3, 7, 2)
# #
# # # 使用zip函数将两个元组的元素配对
# # pairs = zip(animals, ages)
# #
# # # 创建字典
# # animal_dict = dict(pairs)
# #
# # # 按要求输出字典，每个数据一行
# # for animal, age in animal_dict.items():
# #     print(f"{animal}: {age}")
#
#
# # import random
# #
# # # 产生0~500范围内的随机数，创建两个整数数据集合
# # set1 = set(random.sample(range(501), 201))
# # set2 = set(random.sample(range(501), 201))
# #
# # # 1) 求两个集合中不同的数据，并显示
# # unique_numbers = set1.symmetric_difference(set2)
# # print("Unique numbers in set1 and set2:")
# # for i, number in enumerate(unique_numbers, 1):
# #     print(f"{number:5d}", end=' ')
# #     if i % 10 == 0:
# #         print()  # 每行显示10个数后换行
# #
# # # 2) 求出两个集合中相同的数据，并显示
# # common_numbers = set1.intersection(set2)
# # print("\nCommon numbers in set1 and set2:")
# # for i, number in enumerate(common_numbers, 1):
# #     print(f"{number:5d}", end=' ')
# #     if i % 10 == 0:
# #         print()  # 每行显示10个数后换行
#
# # # 定义一个字典，存储四个嫌疑人及其对应的陈述
# # statements = {
# #     'A': '我不是罪犯',
# #     'B': 'C是罪犯',
# #     'C': 'D是罪犯',
# #     'D': 'C骗人'
# # }
# #
# # # 定义一个函数，用于检查如果指定的人是罪犯，其他人的陈述是否都是真话
# # def check_statements(guilty_person):
# #     # 初始化一个计数器，用于记录说真话的人数
# #     truth_tellers = 0
# #     # 遍历嫌疑人及其陈述
# #     for person, statement in statements.items():
# #         # 如果当前遍历的人不是假设的罪犯
# #         if person != guilty_person:
# #             # 根据嫌疑人的陈述和假设的罪犯进行逻辑判断
# #             # 如果当前嫌疑人的陈述是“我不是罪犯”，并且这个人不是罪犯，则认为是真话
# #             if statement == '我不是罪犯':
# #                 truth_tellers += 1
# #             # 如果B说C是罪犯，且假设的罪犯是C，则B说的是真话
# #             elif person == 'B' and statement == 'C是罪犯' and statements[guilty_person] == 'C':
# #                 truth_tellers += 1
# #             # 如果C说D是罪犯，且假设的罪犯是D，则C说的是真话
# #             elif person == 'C' and statement == 'D是罪犯' and statements[guilty_person] == 'D':
# #                 truth_tellers += 1
# #             # 如果D说C骗人，且假设的罪犯是C，则D说的是真话
# #             elif person == 'D' and statement == 'C骗人' and statements[guilty_person] == 'C':
# #                 truth_tellers += 1
# #     # 如果说真话的人数为3，则返回True，表示找到了罪犯
# #     return truth_tellers == 3
# #
# # # 使用for循环遍历嫌疑人，尝试找出罪犯
# # for person in statements.keys():
# #     # 如果当前嫌疑人是罪犯，则调用check_statements函数进行检查
# #     if check_statements(person):
# #         # 如果找到了罪犯，则打印结果并退出循环
# #         print(f"{person} 是罪犯")
# #         break
#
#
#
# #
# # def calculate_time(distance, walking_speed, cycling_speed, find_and_unlock_time, lock_time):
# #     # 计算步行时间
# #     walking_time = distance / walking_speed
# #     # 计算骑车时间（包括找车、开锁、锁车的时间）
# #     cycling_time = distance / cycling_speed + find_and_unlock_time + lock_time
# #     return walking_time, cycling_time
# #
# # # 已知参数
# # walking_speed = 1.2  # 步行速度，单位：m/s
# # cycling_speed = 3    # 骑车速度，单位：m/s
# # find_and_unlock_time = 27  # 寻车和开锁时间，单位：s
# # lock_time = 23         # 锁车时间，单位：s
# #
# # # 用户输入距离
# # distance = float(input("请输入距离（单位：米）："))
# #
# # # 计算时间
# # walking_time, cycling_time = calculate_time(distance, walking_speed, cycling_speed, find_and_unlock_time, lock_time)
# #
# # # 输出结果
# # if walking_time < cycling_time:
# #     print(f"步行更快。步行所需时间：{walking_time:.2f}秒")
# # else:
# #     print(f"骑车更快。骑车所需时间：{cycling_time:.2f}秒")
#
#
#
# # # 从键盘输入一个不多于5位的正整数
# # num = int(input("请输入一个不多于5位的正整数："))
# #
# # # 知识点：input()函数用于从键盘接收输入，int()函数将输入的字符串转换为整数。
# #
# # # 求出它是几位数
# # digit_count = len(str(num))
# # print(f"这是一个{digit_count}位数。")
# #
# # # 知识点：str()函数将数字转换为字符串，len()函数获取字符串的长度。
# #
# # # 分别输出每一位数字
# # for digit in str(num):
# #     print(digit)
# #
# # # 知识点：for循环用于遍历序列中的每个元素。
# #
# # # 按逆序输出每位数字
# # reversed_digits = str(num)[::-1]
# # print(reversed_digits)
# #
# # # 字符串的切片操作，[::-1]表示从后向前取，实现逆序。
# #
# #
# # # 从键盘输入一个不多于5位的正整数
# # num = int(input("请输入一个不多于5位的正整数："))
# #
# # # 求出它是几位数
# # digit_count = len(str(num))
# # print(f"这是一个{digit_count}位数。")
# # #str()函数将数字转换为字符串，len()函数获取字符串的长度。
# # # 分别输出每一位数字
# # for digit in str(num):
# #     print(digit)
# # # for循环用于遍历序列中的每个元素。
# # # 按逆序输出每位数字
# # reversed_digits = str(num)[::-1]
# # print(reversed_digits)
#
#
# # def calculate_time(distance, walking_speed, cycling_speed, find_and_unlock_time, lock_time):
# #     # 计算步行时间
# #     walking_time = distance / walking_speed
# #     # 计算骑车时间（包括找车、开锁、锁车的时间）
# #     cycling_time = distance / cycling_speed + find_and_unlock_time + lock_time
# #     return walking_time, cycling_time
# # # 已知参数
# # walking_speed = 1.2  # 步行速度，单位：m/s
# # cycling_speed = 3    # 骑车速度，单位：m/s
# # find_and_unlock_time = 27  # 寻车和开锁时间，单位：s
# # lock_time = 23         # 锁车时间，单位：s
# # # 用户输入距离
# # distance = float(input("请输入距离（单位：米）："))
# # # 计算时间
# # walking_time, cycling_time = calculate_time(distance, walking_speed, cycling_speed, find_and_unlock_time, lock_time)
# # # 输出结果
# # if walking_time < cycling_time:
# #     print(f"步行更快。步行所需时间：{walking_time:.2f}秒")
# # else:
# #     print(f"骑车更快。骑车所需时间：{cycling_time:.2f}秒")
#
#
# #print(10/10)
#
# #
# # x=input("请您输入您的姓名：")
# # print('姓名:',x)
#
# #
# # # 从键盘获取输入
# # number_str = input("请输入一个四位整数：")
# # number = int(number_str)  # 转换为整数
# #
# # # 获取各个位上的数字
# # thousands = number // 1000  # 千位
# # hundreds = (number % 1000) // 100  # 百位
# # tens = (number % 100) // 10  # 十位
# # units = number % 10  # 个位456
# #
# # # 输出结果
# # print("千位上的数字是：", thousands)
# # print("百位上的数字是：", hundreds)
# # print("十位上的数字是：", tens)
# # print("个位上的数字是：", units)
#
#
# # tu = ("miaoye","gou")
# # v = ''.join(tu)
# # print(v)
#
# # # 创建一个空集合来存储通讯录信息
# # 通讯录集合 = set()
# #
# # # 从用户那里获取5位好友的姓名和电话
# # for i in range(5):
# #     姓名 = input(f"请输入第{i+1}位好友的姓名: ")
# #     电话 = input(f"请输入{姓名}的电话号码: ")
# #     联系人信息 = f"{姓名}: {电话}"  # 将姓名和电话号码组合成一个字符串
# #     通讯录集合.add(联系人信息)  # 将联系人信息添加到集合中
# #
# # # 输出整个通讯录
# # print("您的通讯录如下：")
# # for 信息 in 通讯录集合:
# #     print(信息)
#
#
# # def fact(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * fact(n-1)
# # print(fact(3))
#
#
# # def get_score():
# #     # 尝试接收用户输入并转换为整数
# #     try:
# #         score = int(input("请输入你的分数（0-100）："))
# #     except ValueError:
# #         # 如果输入不能转换为整数，抛出异常
# #         raise ValueError("输入错误！请输入一个整数。")
# #
# #     # 判断分数是否在0到100之间
# #     if 0 <= score <= 100:
# #         print("你的成绩是：", score)
# #     else:
# #         # 如果分数不在这个范围内，抛出异常
# #         raise ValueError("分数必须在0到100之间！")
# #
# # # 调用函数
# # try:
# #     get_score()
# # except Exception as e:
# #     print(e)
#
#
# #
# # def can_form_triangle(a, b, c):
# #     # 检查三角形的形成条件
# #     if a + b > c and a + c > b and b + c > a:
# #         print(f"可以构成三角形，三边长为：a={a}, b={b}, c={c}")
# #     else:
# #         # 如果不满足形成条件，抛出异常
# #         raise Exception(f"{a},{b},{c} 不能构成三角形")
# #
# # # 输入三个边长
# # try:
# #     a = float(input("请输入第一条边长："))
# #     b = float(input("请输入第二条边长："))
# #     c = float(input("请输入第三条边长："))
# #     can_form_triangle(a, b, c)
# # except Exception as e:
# #     print(e)
# # except ValueError:
# #     print("输入错误，请输入有效的数字。")
# #
# #
# # import random
# #
# # # 生成包含10个随机整数的列表，范围从1到100
# # random_numbers = [random.randint(1, 100) for _ in range(10)]
# #
# # def find_max(numbers):
# #     # 初始化最大值为列表的第一个元素
# #     maximum = numbers[0]
# #     # 遍历列表中的每个元素
# #     for number in numbers:
# #         # 如果当前元素大于已知的最大值，则更新最大值
# #         if number > maximum:
# #             maximum = number
# #     return maximum
# #
# # # 调用函数并输出结果
# # max_value = find_max(random_numbers)
# # print("生成的随机列表:", random_numbers)
# # print("列表中的最大值:", max_value)
#
# #
# # tu = ("miaoye","gou")
# # v = "".join(tu)
# # print (v)
#
# # sites = ["Baidu", "Google","Runoob","Taobao"]
# # for site in sites:
# #     if site == "Runoob":
# #       print("菜鸟教程!")
# #       continue
# #
# #     print("循环数据 " + site)
# # else:
# #     print("没有循环数据!")
# #     print("###########完成循环!")
# #
# #
# # print("完成循环!")
#
# # def f1(a,b,c=10,d=20): #默认值参数必须位于普通位置参数后面
# #     print(a,b,c,d)
# # f1(8,9)
# # f1(8,9,19)
# # f1(8,9,19,29)
#
#
# #
# # def f1(a,b,*c):
# #     print(a,b,c)
# # f1(8,9,19,20)
# # def f2(a,b,**c):
# #     print(a,b,c)
# # f2(8,9,name='梦孚',age=18)
# # def f3(a,b,*c,**d):
# #     print(a,b,c,d)
# # f3(8,9,20,30,name='梦孚',age=18)
# #
#
# # lst=['red','pink','blue']
# # def fun(x):
# #     lst.append(x)
# # fun('white')
# # print(lst)
# #
# # try:
# #
# #     def numWays(n):
# #     if n <= 1:
# #         return 1
# #     elif n == 2:
# #         return 2
# #     else:
# #         dp = [0 for i in range(n)]
# #         dp[0] = 1
# #         dp[1] = 2
# #         i = 2
# #         while i < n:  # 循环计算每个dp[i]的值
# #             dp[i] = dp[i - 1] + dp[i - 2]
# #             i += 1
# #         a = int(dp[i - 1])
# #         return a
# #
# # except:
# #     print("异常")
# #     print(numWays(2))
# #
# #
# #
# # for x in range(100):
# #     for y in range(100):
# #         for z in range(100):
# #             t=x+y+z
# #             m=5*x+3*y+z/3
# #             if t==100 and m==100 :
# #                 print ("x=",x,"  y=",y,"  z=",z)
# #
# #
# #
# # s = ["梦孚\n","奇立思\n","爬虫\n"]
# # with open(r"bb.txt","w") as f:
# #     f.writelines(s)
# #
# # import os
# # os.system("notepad.exe")
# #
# #
# # import os
# # os.system("ping www.baidu.com")
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


# import numpy as np
# a = np.array([[12,27,3],[3,24,15]])
# print ('创建的数组是:')
# print (a)
# print ('\n')
# print ('调用 mean() 方法:')
# print (np.mean(a))
# print ('\n')
# print ('沿轴 0 调用 mean() 方法:')
# print (np.mean(a, axis = 0))
# print ('\n')
# print ('沿轴 1 调用 mean() 方法:')
# print (np.mean(a, axis = 1))


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
#
#
# import matplotlib.pyplot as plt
# # 数据准备
# years = list(range(2000, 2021))
# temperatures = [14.1, 14.3, 14.5, 14.2, 14.6, 14.8, 15.0, 15.2, 15.3, 15.5,
#                 15.6, 15.4, 15.7, 15.8, 16.0, 16.1, 16.2, 16.4, 16.5, 16.8, 17.0]
# # 创建图形和轴
# fig, ax = plt.subplots()
# # 绘制线图，每五年一个特殊标记和颜色
# for i in range(len(years)):
#     if (years[i] - 2000) % 5 == 0:
#         ax.plot(years[i], temperatures[i], marker='o', markersize=8, color='red')  # 每五年用红色圆点标记
#     else:
#         ax.plot(years[i], temperatures[i], marker='o', color='blue')  # 其他年份用蓝色圆点标记
# # 使用蓝线连接所有点
# ax.plot(years, temperatures, label='Average Temperature', color='blue')
# # 添加标题和轴标签
# ax.set_title('Global Average Temperatures from 2000 to 2020')
# ax.set_xlabel('Year')
# ax.set_ylabel('Temperature (℃)')
# # 显示网格
# ax.grid(True)
# # 显示图例
# ax.legend()
# # 显示图形
# plt.show()
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
#
#
# import matplotlib.pyplot as plt
# import numpy as np
# # 数据准备
# cities = ['A', 'B', 'C', 'D', 'E']
# populations = np.array([12, 5.5, 8, 4, 6.5])  # 人口数量（百万）
# park_areas = np.array([30, 15, 25, 10, 20])  # 公园面积（平方公里）
# # 创建图形和轴
# fig, ax = plt.subplots()
# # 散点图的颜色和大小
# colors = ['blue', 'green', 'red', 'purple', 'orange']
# sizes = populations * 10  # 根据人口大小调整标记大小
# # 绘制散点图
# scatter = ax.scatter(populations, park_areas, c=colors, s=sizes, alpha=0.6, edgecolors='w', linewidth=1)
# # 标注城市名称
# for i, txt in enumerate(cities):
#     ax.annotate(txt, (populations[i], park_areas[i]))
# # 添加标题和轴标签
# ax.set_title('City Population vs. Park Area')
# ax.set_xlabel('Population (millions)')
# ax.set_ylabel('Park Area (sq km)')
# # 显示网格
# ax.grid(True)
# # 显示图形
# plt.show()


#
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# # 生成数据：10x10 的随机矩阵
# data = np.random.rand(10, 10)
# # 数据标准化：减去均值并除以标准差
# normalized_data = (data - np.mean(data)) / np.std(data)
# # 创建图形和轴
# fig, ax = plt.subplots()
# # 使用 Seaborn 库来绘制热力图
# # Seaborn 的 heatmap 函数提供了更多的可定制选项和美观的颜色映射
# sns.heatmap(normalized_data, ax=ax, cmap='coolwarm', annot=True, fmt=".1f",
#             linewidths=.5, cbar_kws={'shrink': .8, 'label': 'Standardized Value'})
# # 添加标题
# ax.set_title('Complex Heatmap Example')
# # 显示图形
# plt.show()

# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
# # 生成模拟数据
# np.random.seed(0)
# data = {
#     'Horsepower': np.random.randint(100, 200, 100),
#     'Miles_per_Gallon': np.random.uniform(20, 35, 100),
#     'Weight': np.random.randint(1500, 3000, 100),
#     'Acceleration': np.random.uniform(10, 20, 100)
# }
# df = pd.DataFrame(data)
# # 计算相关系数矩阵
# corr_matrix = df.corr()
# # 创建原始数据的热力图
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar_kws={'label': 'Correlation Coefficient'})
# plt.title('Correlation Matrix of Car Performance Metrics')
# plt.show()
# # 附加挑战：标准化数据后重新绘制热力图
# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(df)
# # 重新计算相关系数矩阵
# scaled_df = pd.DataFrame(scaled_features, columns=df.columns)
# scaled_corr_matrix = scaled_df.corr()
# # 创建标准化数据的热力图
# plt.figure(figsize=(8, 6))
# sns.heatmap(scaled_corr_matrix, annot=True, fmt=".2f", cmap='viridis', cbar_kws={'label': 'Correlation Coefficient'})
# plt.title('Correlation Matrix of Standardized Car Performance Metrics')
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm, mlab
#
#
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
# ax.plot_trisurf(x, y, z,cmap=cm.jet,  linewidth=0.2)
# plt.show()
# delta = 0.025
# x = np.arange(-3.0, 3.0, delta)
# y = np.arange(-2.0, 2.0, delta)
# X, Y = np.meshgrid(x, y)
# Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0) #产生双变量正态分布，四个整数分别为：# x和y的方差，x和y 的均值。
# Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# # difference of Gaussians
# Z = 10.0 * (Z2 - Z1)
# # 使用默认色创建带标签轮廓图
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(X, Y, Z, cmap=cm.jet, linewidth=0.2)
# plt.show()

import pandas as pd

import json
# with open('nested_mix.json','r') as f:
#     data=json.loads(f.read())
#
# df=pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=[
#         'class',
#         ['info','president'],
#         ['info','contacts','tel']
#     ]
# )
# print(df)


# import pandas as pd
# data=[{'a':1,"b":2},{'a':5,'b':10,'c':20}]
# # data['1']=10
# df=pd.DataFrame(data)#,index=[0],copy=False)
# print(df)
#
# import pandas as pd
# import json
# with open('nested_list.json','r')as f:
#     data= json.loads( f.read())# Flatten data
#     df_nested_list =pd.json_normalize( data ,record path=['students"])print( df nested list )




