# Table of Contents
- [Table of Contents](#table-of-contents)
  - [reference](#reference)
  - [generic](#generic)
  - [typevar](#typevar)

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