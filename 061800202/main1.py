# -*- coding:utf-8 -*-
import sys
from simhash import Simhash


def simhash_similarity(text1, text2):
    simhash_1 = Simhash(text1)  # 处理文本一
    simhash_2 = Simhash(text2)  # 处理文本二
    max_hashbit = max(len(bin(simhash_1.value)), (len(bin(simhash_2.value))))
    distince = simhash_1.distance(simhash_2)  # 计算汉明距离
    similar = 1 - distince / max_hashbit  # 计算相似度
    return similar


if __name__ == '__main__':
    inputfile1=sys.argv[1]
    inputfile2=sys.argv[2]
    f1 = open(inputfile1, "r", encoding='utf-8')      # 读入文本
    f2 = open(inputfile2, "r", encoding='utf-8')
    text1=f1.read()
    text2=f2.read()
    similar = simhash_similarity(text1, text2)         # 进行比对
    outputfile=open(sys.argv[3],"a")
    outputfile.write((str(round(similar,2))+'\n'))
    print(0)
    f1.close()
    f2.close()