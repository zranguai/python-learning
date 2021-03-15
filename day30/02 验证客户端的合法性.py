# 生成一个随机字符串
import os
ret = os.urandom(32)
print(ret)

# import hashlib
# sha = hashlib.sha1(密钥)  # 加盐
# sha.update(随机字符串)
# 结果 = sha.hexdigest()



# hmac模块：
import os
import hmac    # 替代hashlib模块的
h = hmac.new(b'hahaha', os.urandom(32))
ret = h.digest()
print(ret)

# 后面调通利用hmac模块









