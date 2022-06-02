#Circle Class

from shape import Shape

class Circle(Shape):
    def __init__(self, radius:float=1.0, color:str = "red", filled:bool = True):
        super().__init__(color, filled)
        self._radius = radius
        
    def getRadius(self) -> float:
        return self._radius
    
    def setRadius(self, radius:float):
        self._radius = radius
        
    def getArea(self) -> float:
        return self._radius ** 2 * 3.14
    
    def getPerimeter(self) -> float:
        return self._radius * 2 * 3.14
    
    def __str__(self) -> str:
        return f'Circle[radius = {self._radius}, color = {self._color}, filled = {self._filled}]'