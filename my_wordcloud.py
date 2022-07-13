import matplotlib.pyplot as plt
from wordcloud import WordCloud

backgroup_Image = plt.imread('D:/jobdata_process/cv2/cv2.jpg') #笼罩图

f = open('01.txt', 'r',encoding='UTF-8').read()  # 生成词云的文档
wordcloud = WordCloud(
    background_color='white',  # 背景颜色，根据图片背景设置，默认为黑色
    mask=backgroup_Image, #笼罩图
    font_path='msyh.ttc',  # 若有中文需要设置才会显示中文
    width=1000,
    height=860,
    margin=1,
    scale=6,
    max_font_size=45,
    min_font_size=5,
    stopwords=[line.strip() for line in open('D:/stopwords-master/hagongda.txt', encoding='UTF-8').readlines()]).generate(f)  # generate 可以对全部文本进行自动分词

# 参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片：默认为此代码保存的路径
wordcloud.to_file('touxiang.jpg')
