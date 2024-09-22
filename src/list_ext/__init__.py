from typing import Callable, Generator, overload


class List[T](list[T]):

    def is_empty(self) -> bool:
        """Returns whether the `List` is empty."""
        return self.__len__() == 0

    @property
    def length(self) -> int:
        """Returns the length of the `List`."""
        return self.__len__()

    @property
    def capacity(self) -> int:
        """Returns the length of the `List` -1."""
        return self.__len__() - 1

    @overload
    def first(self) -> T: ...

    @overload
    def first(self, default: T) -> T: ...

    def first(self, default: T | None = None) -> T:
        if self.__len__() > 0:
            return self.__getitem__(0)
        if default is not None:
            return default
        raise IndexError

    def contains(self, el: T) -> bool:
        """Checks if an element is in the `List`."""
        return self.__contains__(el)

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

    def find(self, predicate: Callable[[T], bool]) -> T | None:
        """Return the first element that encounters a specific condition, expressed in the `predicate`."""
        for el in self:
            if predicate(el):
                return el

    def filter(self, predicate: Callable[[T], bool]) -> Generator[T, None, None]:
        """Returns a new `List` containing all the elements meeting a specific condition, expressed in the `predicate`."""
        return (el for el in self if predicate(el))

    def map[R](self, predicate: Callable[[T], R]) -> Generator[R, None, None]:
        """Returns a new `List` containing the result of the `predicate` function, given all the elements of the `List`."""
        return (predicate(el) for el in self)

