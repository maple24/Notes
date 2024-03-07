# Table of Contents

- [Table of Contents](#table-of-contents)
  - [reference](#reference)
  - [generic](#generic)
  - [typevar](#typevar)
  - [Mapping](#mapping)
  - [Type\[class\]](#typeclass)
  - [NamedTuple](#namedtuple)
  - [overload](#overload)
  - [sequence](#sequence)
  - [collection](#collection)
  - [reveal\_type](#reveal_type)

## reference

[reference](https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb)

## generic

```python

```

## typevar

```python
from typing import List, TypeVar

T = TypeVar("T")

def first(container: List[T]) -> T:
    print(container)
    return "a" # mypy raises: Incompatible return value type (got "str", expected "T")
  
if __name__ == "__main__":
    list_one: List[str] = ["a", "b", "c"]
    print(first(list_one))
'''
In the above example even though the only container argument passed to the function has elements of type str, and we return a str, mypy raises an “Incompatible return value type” error, as it was expecting a return value of generic type T .We only define T as the content type for the container parameter in this function, so the return value must come from the container.
'''
```

```python
from typing import Dict, TypeVar

K = TypeVar("K")
V = TypeVar("V")

def get_first(container: Dict[K, V]) -> K:
    return list(container.keys())[0]
  
if __name__ == "__main__":
    test: Dict[str, int] = {"k": 1}
    print(get_first(test))

T = TypeVar("T", str, int) # T can only represent types of int and str
T = TypeVar("T", bound=int) # T can only be an int or subtype of int, bool is a subtype of int
```

## Mapping

```python
class _MetaDataTableCol(str, Enum):
    """Enumeration for metadata table column names."""

    SELECTED = "Selected"
    RUN_ID = "run_id"
    MAP_ID = "map_id"
    RECORDING_ID = "recording_id"
    _INDEX = "index"

    def __str__(self) -> str:
        return self.value

_MetaDataTableRow = Mapping[_MetaDataTableCol, Union[int, str, bool]]
# Mapping type provides similar feature as Dict, but it is immutable
# There is a mutable one which is MutableMapping
def _get_map_evaluation_table_info(evaluation_sets: List[KpiTestResultBasicInfo]) -> List[_MetaDataTableRow]:
```

## Type[class]

```python
# In case we would like to pass an type/class to an function, we should use Type[].
def get_entries(
    mdm_query: str,
    namespace_name: str,
    namespace_model: Type[NamespaceModel],
    data_to_dataframe_input_dict: Callable[[NamespaceModel, List[SearchResponseFile]], dict],
) -> StoredData:

# I would like to validate data with difference pydantic models, so here I use Type[] to indicate that should be a type or class.
# If Type[] is not used, it suggests an instance.
```

## NamedTuple

```python
# The difference between a NamedTuple class and a simple class is that a NamedTuple instance is immutable.
from typing import NamedTuple
class Person(NamedTuple):
    name = "maple"

p = Person()
p.name = "john"
# This will raise a read-only error!
```

## overload
>
> Function overloading is a powerful concept in programming that allows a programmer to define multiple functions with the same name but different parameters or argument types.

> Sometimes the types of several variables are related, such as “if x is type A, y is type B, else y is type C”. Basic type hints cannot describe such relationships, making type checking cumbersome or inaccurate. We can instead use @typing.overload to represent type relationships properly.

[How to Use @overload](https://adamj.eu/tech/2021/05/29/python-type-hints-how-to-use-overload/)

```python
from __future__ import annotations

from collections.abc import Sequence
from typing import overload

@overload
def double(input_: int) -> int:
    ...

@overload
def double(input_: Sequence[int]) -> list[int]:
    ...

"""
The first two @overload definitions exist only for their type hints. Each definition represents an allowed combination of types. These definitions never run, so their bodies could contain anything, but it’s idiomatic to use Python’s ... (ellipsis) literal.
"""

"""
The third definition is the actual implementation. In this case, we need to provide type hints that union all the possible types for each variable. 
"""

def double(input_: int | Sequence[int]) -> int | list[int]:
    if isinstance(input_, Sequence):
        return [i * 2 for i in input_]
    return input_ * 2

x = double(12)
reveal_type(x)

y = double([1, 2])
reveal_type(y)
```

## sequence
>
> Sequence types in Python are used to represent collections of items where the order of elements matters. They can be indexed and sliced. Python provides several built-in sequence types, including lists, tuples, range objects, strings, and bytes.

> You can use it if there is no way to specify if it should be a list or string or tuple, etc.

```python
from collections.abc import Sequence

# this will be deprecated in the future
from typing import Sequence

def foo(seq: Sequence[str]):
    for i in seq:
        print(i)
```

## collection
>
> Python collection, unlike a sequence, does not have a deterministic ordering. Examples include sets and dictionaries.

> In a collection, while ordering is arbitrary, physically, they do have an order.

> Every time we visit a set, we get its items in the same order. However, if we add or remove an item, it may affect the order.

## reveal_type
>
> When working with type hints, it is often useful to debug the types of variables. Type checkers allow you to do this with reveal_type() and reveal_locals().

```python
items = [1, None]
reveal_type(items)
# Then when we run our type checker, in this case Mypy.
# >> mypy example.py
# >> example.py:2: note: Revealed type is 'builtins.list[Union[builtins.int, None]]'
```
