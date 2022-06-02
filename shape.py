#Shape Class
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color:str = "red", filled:bool = True):
        self._color = color
        self._filled = filled

    def getColor(self):
        return self._color
      
    def setColor(self, color:str):
        self._color = color

    def isFilled(self):
        return self._filled

    def setFilled(self, color:str):
        self._filled = color
    
    @abstractmethod
    def getArea() -> float:
        pass

    @abstractmethod
    def getPerimeter() -> float:
        pass

    def __str__(self) -> str:
        return f'Shape[color = {self._color}, filled = {self._filled}]'