class Node():
      
 def encodefile(Inputfile):
    f = open(Inputfile, 'wb+')
    filedata = f.read()
    filesize = len(filedata)
    for x in range(filesize):
        tmp = filedata[x]
        if tmp in char_freq.keys():
            char_freq[tmp] = char_freq[tmp] + 1
        else:
            char_freq[tmp] = 1
    f.close()
    
    tmp = Node(x, char_freq[x])
    list_Node.append(tmp)
    for i in range(filesize):
        key = filedata[i]
        Huffmancode = Huffmancode + str(char_code[key])
    node_length = len(char_freq.keys())
    out = int.to_bytes(node_length, 4, byteorder='big')
    output.write(out)
    out = int.to_bytes(int('1111111', 2),  1, byteorder='big')
    output.write(out)

 def decodefile(Inputfile):
    f = open(Inputfile, 'rb')
    filedata = f.read()
    binstr = "".join(["{:08b}".format(c) for c in filedata])
    node_length = binstr[:32]
    binstr = binstr[32:]

    value = int(Node[:32], 2)
    freq = int(Node[32:], 2)
    char_freq[value] = freq

    bytecode=''
    bytecode=bytecode + binstr[0]                  
    binstr = binstr[1:]

    if bytecode in reverse_code.keys():
        output.write(int.to_bytes(reverse_code[bytecode], 1, byteorder='big'))
    f.close()


char_code=[]
char_freq={}
list_Node=[]
reverse_code={}
encodefile(input("请输入要压缩的文件："))
decodefile(input("请输入要解压的文件："))  
    





