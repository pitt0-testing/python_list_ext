from typing import Any
from typing import TypeVar
from typing import overload

from .lists import List

T = TypeVar("T")


class LoopingList(List[T]):

    @overload
    def __getitem__(self, x: int) -> T:
        ...

    @overload
    def __getitem__(self, x: slice) -> List[T]:
        ...

    def __getitem__(self, x: int | slice) -> Any:
        if isinstance(x, slice):
            return List(self[i] for i in range(x.start, x.stop, x.step))

        elif isinstance(x, int):
            while x >= self.length:
                x -= self.length
            return super().__getitem__(x)

        else:
            raise TypeError(f"list indices must be either int or slice, not {type(x)}")