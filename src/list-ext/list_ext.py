from typing import TypeVar
from typing import Callable, Generator, Sequence


T = TypeVar("T")
R = TypeVar("R")
L = TypeVar("L", bound=Sequence) # used to indicate return type in python 3.12

class MyList(list[T]):
    # NOTE: Creating a list like [i for i in range(_)] is faster than creating a tuple the same way, so stick to lists for now

    @property
    def empty(self) -> bool:
        return self.__len__() == 0

    @property
    def length(self) -> int:
        return self.__len__()

    @property
    def first(self) -> T:
        return self[0]

    @property
    def last(self) -> T:
        return self[-1]

    def contains(self, el: T) -> bool:
        return self.__contains__(el)
    
    def first_or_default(self, default: T) -> T:
        if self.empty:
            return default
        return self[0]
    
    def last_or_default(self, default: T) -> T:
        if self.empty:
            return default
        return self[-1]

    def concat(self, sep: str = ", ") -> str:
        return sep.join(str(el) for el in self)

    def skip(self, element: T) -> Generator[T, None, None]:
        return (el for el in self if el != element)

    def true_for_all(self, predicate: Callable[[T], bool]) -> bool:
        """Return a `bool` that indicates if the predicate is `True` for every element of this list.
        
        A normal `all()` function is more efficient than this method, you should use it instead of this if you can.
        """
        return any(not predicate(el) for el in self)

    def first_where(self, predicate: Callable[[T], bool]) -> T | None:
        for el in self:
            if predicate(el):
                return el
    
    # NOTE: As of python 3.12, functions type parameter will come out and the methods below should have an L type parameter

    # when type parameters will come out this will become a @staticmethod
    def new(self, old: Sequence[T]) -> "MyList"[T]:
        return MyList(el for el in old)

    def where(self, predicate: Callable[[T], bool]) -> "MyList"[T]:
        return MyList(el for el in self if predicate(el))

    def select(self, predicate: Callable[[T], R]) -> "MyList"[R]:
        return MyList(predicate(el) for el in self)
