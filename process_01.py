import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_excel('中级测试.xlsx')
# 有些是异地招聘   过滤掉
data = df['岗位名称'].value_counts()
city = list(data.index)[:10]    # 城市
nums = list(data.values)[:10]   # 岗位数
print(city)
print(nums)

#colors = ['#FF0000', '#0000CD', '#00BFFF', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970', '#9932CC']
#random.shuffle(colors)

# 设置大小   像素
plt.figure(figsize=(22, 14), dpi=150)
# 设置中文显示
mpl.rcParams['font.family'] = 'SimHei'
# 绘制柱形图  设置柱条的宽度和颜色
# color参数  每根柱条配置不同颜色
plt.bar(city, nums, width=0.5, )

# 添加描述信息
plt.title('招聘数最多的岗位Top10', fontsize=25)
plt.xlabel('岗位', fontsize=20)
plt.ylabel('岗位数', fontsize=20)

# 展示图片
plt.show()
