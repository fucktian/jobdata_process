
from jieba.analyse import extract_tags

sentence = open('04.txt', encoding='utf-8', mode='r').readlines().__str__()
keywords = extract_tags(sentence, topK=100, withWeight=True, allowPOS=())
for item in keywords:
    print(item)


