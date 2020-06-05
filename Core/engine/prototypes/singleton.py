class Singleton:
    """
    单例模式原型
    """
    __instance = None

    def __new__(cls, *args, **kw):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls.__instance
