import sys
import jieba
from simhash import Simhash


def getText(filepath):  # 处理读入的文件
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


if __name__ == '__main__':
    text1=getText(sys.argv[1])
    text2=getText(sys.argv[2])
    similar = simhash_similarity(text1, text2)
    outputfile=open(sys.argv[3],"a")           # 输出结果到参数指定的文件夹
    outputfile.write((str(round(similar,2))+'\n'))
    print(0)