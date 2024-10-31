from .simplicialpy import SimplicialComplex

from collections.abc import Iterable

from networkx.classes.graph import Graph
from networkx import find_cliques
from xgi.core.simplicialcomplex import SimplicialComplex as XGISimplicialComplex

def simplicial_complex_from_xgi(sc: XGISimplicialComplex) -> SimplicialComplex:
    mbrs: list[frozenset[int]] = sc.edges.maximal().members()
    facets = [tuple(facet) for facet in mbrs]
    return SimplicialComplex(facets=facets)

def clique_complex_from_iterable(facets: Iterable[Iterable[int]]) -> SimplicialComplex:
    return SimplicialComplex(facets=facets)

def clique_complex_from_nx(graph: Graph) -> SimplicialComplex:
    facets: list[list[int]] = list(find_cliques(graph))
    return clique_complex_from_iterable(facets)
