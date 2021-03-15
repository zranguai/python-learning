"""
    自定义模块
"""
# 使用__all__控制被导入的成员
__all__ = ['age', 'age2']
age = 10
age1 = 20
age2 = 30
age3 = 40
def f1():
    print('haha')

# 测试函数，在开发阶段，对本模块中的功能进行测试
def main():
    print(age)
    f1()
# 可以快速生成(main)
if __name__ == '__main__':
    main()


