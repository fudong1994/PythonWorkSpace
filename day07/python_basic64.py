"""
-------------------------------------------------
   File Name:python_basic64
   Author:Lee
   date: 2021/6/2-10:25
-------------------------------------------------
"""

"""
通过流操作文件：读和写
"""

""" 1、文件内容读取 """
# 第一步：打开文件 (注意在路径中,有绝对路径[一般从根目录的路径比如: D:\Tools]和相对路径[相对于当前文件的路径])
fr = open(r'./test.txt', mode='r', encoding='utf8')  # 打开当前目录下的test.txt文件，并且读取操作(r代表只读),以utf8的编码格式进行识别
# 第二步：文件内容读取
# result = fr.read()  # 读取文件所有内容
# result = fr.readline()  # 读取首行内容
result = fr.readlines()  # 读取所有内容，但是会把每一行的内容读取到列表里，包括换行符
print(result)
# 第三步:关闭流
fr.close()

""" 2、文件的写入 w代表覆盖式写入，会把以前的内容覆盖掉。 a代表追加式写入，会在以前的内容基础上增加内容 """
# w模式和a模式 当文件不存在时都会创建这个文件
fw = open(r'C:\Users\Hello\Desktop\test.txt', mode='w', encoding='utf8')  # 创建流，指向test.txt文件，并且以utf8的格式解析和写入
fw.write('路漫漫其修远兮')
fw.write('\n吾将上下而求索')
# fw.flush()  # 先把内容保存到缓存区，我们可以手动使用flush()刷新缓存区的内容到文件
fw.close()  # 先刷新缓存区的内容到文件，并且关闭流

""" 3、传统方式的读和写：好处,不用手动刷新或关闭 """
with open(r'./test.txt', 'r', encoding='utf8') as fr:
    print(fr.read())

with open(r'./test.txt', mode='a', encoding='utf8') as fw:
    fw.write('\n好好学习，天天向上')
