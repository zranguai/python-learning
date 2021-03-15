# 背诵
# python3 所有的类都是继承Object类
# 只要继承object类就是新式类
# python3 所有的类都是新式类

# 经典类：在py3中不存在，在py2中 不继承object的类都是经典类

# 在py2中
class A:pass  # 经典类
class B(object):pass # 新式类
# 在py3中
class A:pass  # 新式类
class B(object):pass # 新式类

# 在单继承方面(无论是新式类还是经典类都是一样的)
# class A:
#     def func(self):pass
# class B(A):
#     def func(self):pass
# class C(B):
#     def func(self):pass
# class D(C):
#     def func(self):pass
#
# print(D.mro())    # 查看继承顺序，只在新式类中有，经典类中没有
# d = D()
# 寻找某一个方法的顺序:D->C->B->A
# 越往父类走,是深度


# 在新式类中，在走到一个点,下一个点既可以从深度走,也可以从广度走的时候,总是先走广度,再走深度,广度优先
# 在经典类中，都是深度优先，总是在一条路走不通之后再换一条路，走过的点不会再走了


# C3算法
# A(O) = [AO]
# B(A) = [BAO]
# C(A) = [CAO]
# D(B) = [DBAO]
# E(C) = [ECAO]
#
# F(D,E) = merge(D(B) + E(C))
#          = [F] + [DBAO] + [ECAO]
#        F = [DBAO] + [ECAO]
#     FD   = [BAO] + [ECAO]
#     FDB  = [AO] + [ECAO]
#     FDBE = [AO] + [CAO]
#     FDBEC= [AO] + [AO]
#     FDBECA= [O] + [O]
#     FDBECAO

# 算法的内容
#     如果是单继承 那么总是按照从子类->父类的顺序来计算查找顺序
#     如果是多继承 需要按照自己本类,父类1的继承顺序,父类2的继承顺序,...
#     merge的规则 :如果一个类出现在从左到右所有顺序的最左侧,并且没有在其他位置出现,那么先提出来作为继承顺序中的一个
#                 或 一个类出现在从左到右顺序的最左侧,并没有在其他顺序中出现,那么先提出来作为继承顺序中的一个
#                 如果从左到右第一个顺序中的第一个类出现在后面且不是第一个,那么不能提取,顺序向后继续找其他顺序中符合上述条件的类


# 经典类 - 深度优先 新式类 - 广度优先
# 深度优先要会看,自己能搞出顺序来
# 广度优先遵循C3算法,要会用mro,会查看顺序
# 经典类没有mro,但新式类有


# 练习客户端合法性：
class G:pass

class F(G):pass
class B(F):pass
class E:pass
class C(E):pass
class D(G):pass
class A(B, C, D):pass

print(A.mro())





