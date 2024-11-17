Python wrapper on top of Rust crate [simplicial_topology](https://lib.rs/crates/simplicial_topology).

Simple lightweight implementation of simplicial complexes that are stored as a collection of facets of various dimensions. Simple operations (adding simplices, union of complexes) and computations (Betti numbers) are exposed.

# Installation

# Basic Usage
```python
>>> import simplicialpy as sp
>>> sc = sp.SimplicialComplex([[1,2,3], [1,2,4], [1,3,4], [2,3,4]])
>>> sc.betti_numbers
[1, 0, 1]
>>> sc.compute_betti_number(2)
1
>>> sc.add_simplex([1,2,3,4])
>>> sc.betti_numbers
[1, 0, 0, 0]
>>> sc2 = sp.SimplicialComplex([[1, 2, 5]])
>>> sc.union(sc2)
SimplicialComplex(Vertices: [[5], [1], [2], [3], [4]], Facets: [[1, 2, 3, 4], [1, 2, 5]])
```