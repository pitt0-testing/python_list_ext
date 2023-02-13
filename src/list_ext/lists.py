from __future__ import annotations

from typing import TypeVar
from typing import Callable, Generator, Sequence


T = TypeVar("T")
R = TypeVar("R")
L = TypeVar("L", bound=Sequence) # used to indicate return type in python 3.12

class List(list[T]):
    # NOTE: Creating a list like [i for i in range(_)] is faster than creating a tuple the same way, so stick to lists for now

    @property
    def empty(self) -> bool:
        """Returns whether the `List` is empty.
        """
        return self.__len__() == 0

    @property
    def single(self) -> bool:
        """Returns wheter the `List` has only one item.
        """
        return self.__len__() == 1

    @property
    def multiple(self) -> bool:
        """Returns wheter the `List` hast 2 or more items.
        """
        return not (self.empty or self.single)

    @property
    def length(self) -> int:
        """Returns the length of the `List`.
        """
        return self.__len__()

    @property
    def capacity(self) -> int:
        """Returns the length of the `List` -1.
        """
        return self.__len__() - 1

    @property
    def first(self) -> T:
        """Returns the first element of the `List`.
        """
        return self[0]

    @property
    def last(self) -> T:
        """Returns the last element of the `List`.
        """
        return self[-1]

    def contains(self, el: T) -> bool:
        """Checks if an element is in the `List`.
        """
        return self.__contains__(el)
    
    def first_or_default(self, default: T) -> T:
        """Returns the first element of the `List`.
        
        If the `List` is empty, returns the `default` element."""
        if self.empty:
            return default
        return self[0]
    
    def last_or_default(self, default: T) -> T:
        """Returns the last element of the `List`.
        
        If the `List` is empty, returns the `default` element."""
        if self.empty:
            return default
        return self[-1]

    def concat(self, sep: str = ", ") -> str:
        """Returns a `string` containing all the elements of the `List`.

        The elements are separated by the `sep` parameter, default to ", ".
        """
        return sep.join(str(el) for el in self)

    def skip(self, element: T) -> Generator[T, None, None]:
        return (el for el in self if el != element)

    def true_for_all(self, predicate: Callable[[T], bool]) -> bool:
        """Return a `bool` that indicates if the predicate is `True` for every element of this `List`.
        
        A normal `all()` function is more efficient than this method, you should use it instead of this if you can.
        """
        return any(not predicate(el) for el in self)

    def first_where(self, predicate: Callable[[T], bool]) -> T | None:
        """Return the first element that encounters a specific condition, expressed in the `predicate`.
        """
        for el in self:
            if predicate(el):
                return el
    
    # NOTE: As of python 3.12, functions type parameter will come out and the methods below should have an L type parameter

    # when type parameters will come out this will become a @staticmethod
    @classmethod
    def new(cls, old: Sequence[T]) -> List[T]:
        """Returns a new `List` contatining all the elements from the `old`.
        """
        return cls(el for el in old)

    def where(self, predicate: Callable[[T], bool]) -> List[T]:
        """Returns a new `List` containing all the elements meeting a specific condition, expressed in the `predicate`.
        """
        return List(el for el in self if predicate(el))

    def select(self, predicate: Callable[[T], R]) -> List[R]:
        """Returns a new `List` containing the result of the `predicate` function, given all the elements of the `List`.
        """
        return List(predicate(el) for el in self)
