#调用argv
from sys import argv
#将运行环境变量赋值给filename
script, filename = argv
#打开文件
txt = open(filename)
#打印文字
print ("Here's your file %r:" % filename )
#打印文件内容
print (txt.read())
#关闭文件
txt.close()
#打印文字
print ("文件已关闭")
#打印文字
print ("Type the filename again:")
#读取新文件名
file_again = input("> ")
#打开新文件
txt_again = open(file_again)
#打印新文件内容
print (txt_again.read())
#关闭文件
txt_again.close()
#打印文字
print ("文件已关闭")
