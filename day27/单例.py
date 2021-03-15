# 在其他的地方使用该模块只会有一个实例变量
class Baby:
    def __init__(self,cloth,pants):
        self.cloth = cloth
        self.pants = pants
baby = Baby('红上衣', '绿裤子')