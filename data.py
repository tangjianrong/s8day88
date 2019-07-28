# _*_encoding:utf-8_*_
import chardet
result = chardet.detect(open("D:/毕业设计/text.txt", mode="rb").read())
print(result)  # 即可知道文档的格式
# f = open("D:/毕业设计/testing.doc", "r", encoding="utf-8")
# for i in f:
#     print(i)
# f.close()
