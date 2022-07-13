# -*- coding: utf-8 -*-

import jieba
import jieba.analyse

jieba.load_userdict('质量管理词典.txt')

# 取出停用词表
def stopwordlist():
    stopwords = [line.strip() for line in open('D:/stopwords-master/hagongda.txt', encoding='UTF-8').readlines()]
    return stopwords
# 分词并去停用词

def seg_word(line):
    # seg=jieba.cut_for_search(line.strip())

    seg = jieba.cut(line.strip(),cut_all=False,HMM=True)

    temp = ""
    wordstop = stopwordlist()
    for word in seg:
        if word not in wordstop:
            if word != '\t':
                temp += word
                temp += '\n'
    # tag = jieba.analyse.extract_tags(sentence=temp, topK=10, withWeight=True)
    # print(tag)

    return temp



# 输出分词并去停用词的有用的词到txt

def output(inputfilename, outputfilename):
    inputfile = open(inputfilename, encoding='UTF-8', mode='r')

    outputfile = open(outputfilename, encoding='UTF-8', mode='w')

    for line in inputfile.readlines():
        line_seg = seg_word(line)

        #  line_seg = seg_word(line) + "\n"

        outputfile.write(line_seg)
    inputfile.close()
    outputfile.close()

    return outputfile

if __name__=='__main__':

    print("__name__",__name__)
    inputfilename='01.txt'

    outputfilename='04.txt'

    output(inputfilename,outputfilename)

