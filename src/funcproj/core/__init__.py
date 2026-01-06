from typing import *
import operator
import setdoc

__all__ = ["FuncProj"]


class FuncProj:
    key:int|str
    __slots__ = ("_key",)
    @setdoc.basic
    def __call__(self:Self, *args:Any, **kwargs:Any)->Any:
        if isinstance(self.key, int):
            return args[self.key]
        else:
            return kwargs[self.key]
    @setdoc.basic
    def __init__(self:Self, key:int|str)->None:
        self.key = key
    @property
    def key(self:Self) -> int| str:
        return self._key
    @key.setter
    def key(self:Self, value:int|str) -> None:
        if isinstance(value, int):
            return operator.index(value)
        if isinstance(value, str):
            return str(value)
        raise TypeError
