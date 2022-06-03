# 设计文档
## 程序实现说明及运行
问题：对任意一个文件，按照字节进行霍夫曼编码，实现压缩和解压
定义node类，要压缩文件，先定义函数来打开文件、操作文件，其中以二进制读取文件
```python
class Node():      
 def encodefile(Inputfile):
    f = open(Inputfile, 'wb+')
    filedata = f.read()
```
获取文字的字节总数，统计各种字节的频率，保存在字典中，最后关闭文件
```python
    filesize = len(filedata)
    for x in range(filesize):
        tmp = filedata[x]
        if tmp in char_freq.keys():
            char_freq[tmp] = char_freq[tmp] + 1
        else:
            char_freq[tmp] = 1
    f.close()
```
构造霍夫曼树，使用node构造函数，并添加到数组list_huftrees当中
```python
tmp = Node(x, char_freq[x])
    list_Node.append(tmp)
```
获取huffman编码文件，写入辅助信息，将编码以八位字节分割
```python
for i in range(filesize):
        key = filedata[i]
        Huffmancode = Huffmancode + str(char_code[key])
    node_length = len(char_freq.keys())
    out = int.to_bytes(node_length, 4, byteorder='big')
    output.write(out)
    out = int.to_bytes(int('1111111', 2),  1, byteorder='big')
    output.write(out)
```
之后解压文件：打开文件，读取文件并转换成二进制字符串的形式
```python
def decodefile(Inputfile):
    f = open(Inputfile, 'rb')
    filedata = f.read()
    binstr = "".join(["{:08b}".format(c) for c in filedata])
```
解析辅助信息，读取node节点数、字节和频率
```python
    node_length = binstr[:32]
    binstr = binstr[32:]

    value = int(Node[:32], 2)
    freq = int(Node[32:], 2)
    char_freq[value] = freq
```
逆编码来写入文件
```python
     bytecode=''
    bytecode=bytecode + binstr[0]                 
    binstr = binstr[1:]

    if bytecode in reverse_code.keys():
        output.write(int.to_bytes(reverse_code[bytecode], 1, byteorder='big'))
    f.close()
```
定义全局变量，实现压缩及解压
```python
char_code=[]
char_freq={}
list_Node=[]
reverse_code={}
encodefile(input("请输入要压缩的文件："))
decodefile(input("请输入要解压的文件："))  
```