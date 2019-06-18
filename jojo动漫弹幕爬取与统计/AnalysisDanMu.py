# -*- coding:utf-8  -*-
import jieba
import wordcloud
from scipy.misc import imread

#分析弹幕统计词语
txt = open("E:/DanMu.txt", "r", encoding='gb18030').read()
words  = jieba.lcut(txt)
counts = {}
useless = ['这个','不是','一个','什么','怎么','真是','就是','真的',
           '可以','已经','不行','这么','没有','哈哈哈','知道','自己','你们',
           '那个','不会','这里','出来','所以','不能']
for word in words:
    for i in useless:
        if word == i:
            word = 'a'
    if len(word) == 1:
        continue        
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
cloudtext = []
for i in range(30):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
    cloudtext.append((items[i][0]+' ')*items[i][1])

#生成分析词语的文件
for word in cloudtext:
    f = open('E:/cloudtext.txt', "a", encoding='gb18030')
    f.writelines(word)
    f.close()

#生成词云
#mask = imread('E:/jojo.jpg')
excludes = { }
f = open("E:/cloudtext.txt", "r", encoding="gb18030")
txt = f.read()
f.close()

w = wordcloud.WordCloud(width = 1000, height = 700,
    background_color = "white",
    font_path = "msyh.ttc", #mask = mask
    )
w.generate(txt)
w.to_file("E:/JOJOwordcloud.png")
