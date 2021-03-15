print('from the tbjx.py')
name = '太白金星'

def read1():
    print('tbjx模块：',name)

def read2():
    print('tbjx模块')
    read1()

def change():
    global name
    name = 'barry'
    print(name)
