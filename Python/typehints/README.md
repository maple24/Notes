# Table of Contents
- [Table of Contents](#table-of-contents)
  - [reference](#reference)
  - [generic](#generic)
  - [typevar](#typevar)
  - [Mapping](#mapping)

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