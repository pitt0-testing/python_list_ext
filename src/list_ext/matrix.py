from __future__ import annotations

from typing import Any
from typing import overload


class Vector(list[int]):

    def __str__(self):
        return f"Vector <{self}>"

class Equation(list[str]):

    def __str__(self):
        return f"Equation of indices <{self}>"

 

class Matrix(list[list[int]]):

    @overload
    def __getitem__(self, x: int, y: int) -> int:
        ...

    @overload
    def __getitem__(self, x: slice, y: int) -> Equation:
        ...

    @overload
    def __getitem__(self, x: int, y: slice) -> Vector:
        ...

    @overload
    def __getitem__(self, x: slice, y: slice) -> Matrix:
        ...

    def __getitem__(self, x: int | slice, y: int | slice) -> Any:
        return super().__getitem__(y).__getitem__(x)