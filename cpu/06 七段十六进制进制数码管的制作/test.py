import os

# 获取当前绝对路径
dirname = os.path.dirname(os.path.abspath(__file__))

# wb以写入二进制的方式打开当前目录下的test.txt文件
with open(os.path.join(dirname,'test.bin'),'wb') as file:
    # 0-255 写入文件
    for var in range(256):
        #将16进制数转成10进制
        var=str(var)
        var=int(var,base=16)
        byte = var.to_bytes(2,byteorder='little')
        file.write(byte)