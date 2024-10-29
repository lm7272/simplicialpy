from typing import TypeVar

Vertex = TypeVar("Vertex", bound = int)
Edge = TypeVar("Edge", bound = tuple[Vertex[int], Vertex[int]])
Simplex = TypeVar("Simplex", bound = list[Vertex[int]])