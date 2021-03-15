class File:
    lst = [('读文件', 'read'), ('写文件', 'write'), ('删除文件', 'remove')]
    def read(self):
        print(' in read')
    def write(self):
        print(' in write')
    def remove(self):
        print(' in remove')

f = File()
while True:
    for index, opt in enumerate(File.lst, 1):
        print(index, opt[0])
    num = int(input('输入你要做的操作'))
    if hasattr(f, f.lst[num - 1][1]):
        getattr(f, f.lst[num - 1][1])()























