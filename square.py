#Rectangle Class
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side:float, color:str = "red", filled:bool = True):
        super().__init__(side, side, color, filled)
        
    def setSide(self, side:float):
        self._width = side
        self._length = side
        
    def getSide(self) -> float:
        return self._width
    
    def __str__(self) -> str:
        return f'Square[side = {self._width}, color = {self._color}, filled = {self._filled}]'

square = Square(4)
print(square)