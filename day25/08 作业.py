# 简答题：
#
# 面向对象的三大特性是什么？
#
# 封装，继承，多态
#
# 什么是面向对象的新式类？什么是经典类？
#
# 基类的根是object的就是新式类，经典类是在基类的根什么都不写
#
# 面向对象为什么要有继承？继承的好处是什么？
#
# 为了减少重复代码的使用
#
# 增加类的耦合性
#
# 减少了重复代码
#
# 使得代码规范化，合理化，简约大方
#
# 面向对象中super的作用。
#
# 继承父类的__init__方法
#
# 代码题(通过具体代码完成下列要求)：
#
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A, B):
#     def func(self):
#
#         print('in C')
# super讲完看
# 可以改动上上面代码，完成下列需求：对C类实例化一个对象产生一个c1，然后c1.func()
#
# 1.让其执行C类中的func class C(A,B): def func(self): print('in C')
# c1 = C()
# c1.func()
# 2.让其执行A类中的func class C(A,B): def func(self): super().func()
#
# 3.让其执行B类中的func class C(A,B): def func(self): B.func(self)
#
# 4.让其既执行C类中的func，又执行A类中的func class C(A,B): def func(self): print('in C') super().func()
#
# 5.让让其既执行C类中的func，又执行B类中的func class C(A,B): def func(self): print('in C') B.func(self)
#
# 下面代码执行结果是什么？为什么？
#
# class Parent:
#     def func(self):
#         print('in Parent func')
#
#     def __init__(self):
#         self.func()
#
# class Son(Parent):
#     def func(self):
#         print('in Son func')
#
# son1 = Son()

# class A:
#     name = []
#
# p1 = A()
# p2 = A()
# p1.name.append(1)
# print(p1.name)
# print(p2.name)
# print(A.name)
# p1.name，p2.name，A.name 分别是什么？
# [1] [1] [1]
# p1.age = 12
# print(p1.age)
# p2.age
# A.age
# p1.age，p2.age，A.age 分别又是什么？为什么？
# 12 error error
# 写出下列代码执行结果：
# class Base1:
#     def f1(self):
#         print('base1.f1')
#
#     def f2(self):
#         print('base1.f2')
#
#     def f3(self):
#         print('base1.f3')
#         self.f1()
#
#
# class Base2:
#     def f1(self):
#         print('base2.f1')
#
#
# class Foo(Base1, Base2):
#     def f0(self):
#         print('foo.f0')
#         self.f3()
#
#
# obj = Foo()
# obj.f0()
# foo.fo base1.f3 base1.f1
# 看代码写结果：
# class Parent:
#     x = 1
#
# class Child1 (Parent):
#     # x = 3
# 	pass
#
# class Child2(Parent):
#     # x = 2
# 	pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# # 1 1 1
# Child2.x = 2
# print(Parent.x, Child1.x, Child2.x)
# # 1 1 2
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)
# # 1 3 2
# 有如下类：
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B,C):
    pass

class F(C,D):
    pass

class G(D):
    pass

class H(E,F):
    pass

class I(F,G):
    pass

class K(H,I):
    pass
# 如果这是经典类，请写出他的继承顺序。
# khebacfdig

# 如果这是新式类，请写出他的继承顺序，并写出具体过程。
#
# mro(K(H,I)) = [k] + merge(mro(H), mro(I), [H,I])
# mro(K(H,I)) = [k] + merge([H,E,B,F,C,D,A], [I,F,C,G,D,A], [H,I])
# mro(K(H,I)) = [k,H] + merge([E,B,F,C,D,A], [I,F,C,G,D,A], [I])
# mro(K(H,I)) = [k,H,E] + merge([B,F,C,D,A], [I,F,C,G,D,A], [I])
# mro(K(H,I)) = [k,H,E,B] + merge([F,C,D,A], [I,F,C,G,D,A], [I])
# mro(K(H,I)) = [k,H,E,B,I] + merge([F,C,D,A], [F,C,G,D,A])
# mro(K(H,I)) = [k,H,E,B,I,F] + merge([C,D,A], [C,G,D,A])
# mro(K(H,I)) = [k,H,E,B,I,F,C] + merge([D,A], [G,D,A])
# mro(K(H,I)) = [k,H,E,B,I,F,C,G] + merge([D,A], [D,A])
# mro(K(H,I)) = [k,H,E,B,I,F,C,G,D] + merge([A], [A])
# # mro(K(H,I)) = [k,H,E,B,I,F,C,G,D,A]
#
# mro(H(E,F)) = [H] + merge(mro(E), mro(F), [E,F])
# mro(H(E,F)) = [H] + merge([E,B,C,A], [F,C,D,A], [E,F])
# mro(H(E,F)) = [H,E] + merge([B,C,A], [F,C,D,A], [F])
# mro(H(E,F)) = [H,E,B] + merge([C,A], [F,C,D,A], [F])
# mro(H(E,F)) = [H,E,B,F] + merge([C,A], [C,D,A])
# mro(H(E,F)) = [H,E,B,F,C] + merge([A], [D,A])
# mro(H(E,F)) = [H,E,B,F,C,D] + merge([A], [A])
# mro(H(E,F)) = [H,E,B,F,C,D,A]
#
# mro(E(B,C)) = [E] + merge(mro(B), mro(C), [B,C])
# mro(E(B,C)) = [E] + merge([B,A], [C,A], [B,C])
# mro(E(B,C)) = [E,B] + merge([A], [C,A], [C])
# mro(E(B,C)) = [E,B,C] + merge([A], [A])
# mro(E(B,C)) = [E,B,C,A]
#
# mro(F(C,D)) = [F] + merge(mro(C), mro(D), [C,D])
# mro(F(C,D)) = [F] + merge([C,A], [D,A], [C,D])
# mro(F(C,D)) = [F,C] + merge([A], [D,A], [D])
# mro(F(C,D)) = [F,C,D] + merge([A], [A])
# mro(F(C,D)) = [F,C,D,A]
#
# mro(I(F,G)) = [I] + merge(mro(F), mro(G), [F,G])
# mro(I(F,G)) = [I] + merge([F,C,D,A], [G,D], [F,G])
# mro(I(F,G)) = [I,F] + merge([C,D,A], [G,D], [G])
# mro(I(F,G)) = [I,F,C] + merge([D,A], [G,D], [G])
# mro(I(F,G)) = [I,F,C,G] + merge([D,A], [D])
# mro(I(F,G)) = [I,F,C,G,D] + merge([A])
# mro(I(F,G)) = [I,F,C,G,D,A]



# K,H,E,B,I,F,C,G,D,A