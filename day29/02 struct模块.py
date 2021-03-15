import struct
# 2的23次方都可以转换成4个字节
num1 = 129469649
num2 = 123
num3 = 8

ret1 = struct.pack('i', num1)
print(ret1)
ret2 = struct.pack('i', num2)
print(ret2)
ret3 = struct.pack('i', num3)
print(ret3)    # 返回的是4位字节

print(struct.unpack('i', ret1))
print(struct.unpack('i', ret2))
print(struct.unpack('i', ret3))



