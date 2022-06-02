#Rectangle Class
from shape import Shape

class Rectangle(Shape):
    def __init__(self, width:float = 1, length:float = 1, color:str = "red", filled:bool = True):
        super().__init__(color, filled)
        self._width = width
        self._length = length
        
    def getWidth(self) -> float:
        return self._width
    
    def getLength(self) -> float:
        return self._length
    
    def getArea(self) -> float:
        return self._width * self._length
    
    def getPerimeter(self) -> float:
        return 2 * (self._width + self._length)
    
    def __str__(self) -> str:
        return f'Rectangle[width = {self._width}, length = {self._length}, color = {self._color}, filled = {self._filled}]'