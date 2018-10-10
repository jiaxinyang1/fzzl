import  abc

class Common(metaclass=abc.ABCMeta):
    #选择关卡
    @classmethod
    def begin(cls):
        pass
    #图内战斗流程
    @classmethod
    def attack(cls):
        pass
    #是否结束
    @classmethod
    def end(cls):
        pass