#Equilateral Triangle Class
from shape import Shape

class EquilateralTriangle(Shape):
    def __init__(self, sideLength:float = 1.0, color:str = "red", filled:bool = True):
        super().__init__(color, filled)
        self._sideLength = sideLength
        
    def getsideLength(self) -> float:
        return self._sideLength
    
    def setsideLength(self, sideLength:float):
        self._sideLength = sideLength
        
    def getArea(self) -> float:
        return self._sideLength ** 2 * 3.14 / 4
    
    def getPerimeter(self) -> float:
        return self._sideLength * 3.14 * 2
    
    def __str__(self) -> str:
        return f'EquilateralTriangle[sideLength = {self._sideLength}, color = {self._color}, filled = {self._filled}]'

equilateralTriangle = EquilateralTriangle(4)
print(equilateralTriangle)