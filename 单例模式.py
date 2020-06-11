# -*- coding: utf-8 -*-
# 方法 1: 重写 __new__,__init__
class Foo:
     __instance = None
     __isFirstInit = False
     def __new__(cls, *args, **kwargs):
          if not cls.__instance:
               Foo.__instance = super().__new__(cls)
          return Foo.__instance

     def __init__(self,name):
          if not self.__isFirstInit:
               self.__name = name
               Foo.__isFirstInit = True

     def getName(self):
          return self.__name


f1 = Foo('kz1')
f2 = Foo('kz2')
print(f1.getName(),f2.getName())
print(f'id(kz1):{id(f1)}, id(kz2): {id(f2)}')
print('='*20)

# 方法2： 装饰器
# 方法3： 正规做法，元编程
class Singleton(type):
     def __init__(self, *args, **kwargs):
          self.__instance = None
          super().__init__(*args, **kwargs)

     def __call__(self, *args, **kwargs):
          if self.__instance is None:
               self.__instance = super(Singleton,self).__call__(*args, **kwargs)
          return self.__instance


class Caicloud(metaclass=Singleton):
     def __init__(self,name):
          self.name = name

     def getName(self):
          return self.name


c1 = Caicloud('kz1')
c2 = Caicloud('kz2')
print(c1.getName(),c2.getName())
print(f'id(kz1):{id(c1)}, id(kz2): {id(c2)}')
print('='*20)

