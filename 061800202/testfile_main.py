# -*- coding:utf-8 -*-
import sys
import os
import jieba
from simhash import Simhash


class FileErorr(Exception):
    pass


class EmptyfileError(FileErorr):  # 比对文本没有内容
    def __init__(self):
        print("出错了，对比文件为空！")
        print("0")

    def __str__(self, *args, **kwargs):
        return "请找篇有内容的文本来进行比对"


def getText(filepath):  # 处理读入的文件
    try:
        if os.path.getsize(filepath) == 0:   # 文本为空，触发异常
            raise EmptyfileError()
    except Exception as err:
        print(err)
    else:
        with open(filepath, 'r', encoding='utf-8') as f:   # 读取文件
            text = f.read()
        content = jieba.cut(text)   # 使用jieba库对文本进行分词处理
        contents = ""
        for i in content:
            contents += i + " "
        documents = [contents]
        texts = [[word for word in document.split()] for document in documents]
        f.close()
        return str(texts)


# 求两篇文章相似度
def simhash_similarity(text1, text2):
    simhash_1 = Simhash(text1)     # 处理文本一
    simhash_2 = Simhash(text2)     # 处理文本二
    max_hashbit = max(len(bin(simhash_1.value)), (len(bin(simhash_2.value))))
    distince = simhash_1.distance(simhash_2)  # 汉明距离
    similar = 1 - distince / max_hashbit     # 计算相似度
    return similar


def test_main(testfile1,testfile2,testans):
    text1=getText(testfile1)
    text2=getText(testfile2)
    similar = simhash_similarity(text1, text2)
    outputfile=open(testans,"a")           # 输出结果到参数指定的文件夹
    outputfile.write((str(round(similar,2))+'\n'))
    outputfile.close()
    print('相似度: %.2f%%' % (similar * 100))