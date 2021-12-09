import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
# plt.figure(figsize = (7, 5))

# 正弦函数
# x = np.linspace(0, 2*np.pi, 50)
# y = np.sin(x)
# plt.plot(x, y, 'bp--')
# plt.show()

# 饼状图
# # 定义标签
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# # 每一块的比例
# sizes = [15, 30, 45, 10]
# # 每一块的颜色
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# # 突出显示（第二块）
# explode = (0, 0.1, 0, 0)

# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
# # 显示为圆
# plt.axis('equal')
# plt.show()

# x = np.random.randn(1000)
# plt.hist(x, 10)     # 直方图
# plt.show()

# 定义误差列
error = np.random.randn(10)
# 均值数据列
y = pd.Series(np.sin(np.arange(10)))
# 绘制误差图
y.plot(yerr = error)
plt.show()