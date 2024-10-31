from .simplicialpy import SimplicialComplex

from collections.abc import Iterable

from networkx.classes.graph import Graph
from networkx import find_cliques
from xgi.core.simplicialcomplex import SimplicialComplex as XGISimplicialComplex

def complex_from_xgi_complex(sc: XGISimplicialComplex) -> SimplicialComplex:
    mbrs: list[frozenset[int]] = sc.edges.maximal().members()
    facets = [tuple(facet) for facet in mbrs]
    return SimplicialComplex(facets=facets)

def clique_complex_from_iterable(cliques: Iterable[Iterable[int]]) -> SimplicialComplex:
    return SimplicialComplex(facets=cliques)

def clique_complex_from_nx(graph: Graph) -> SimplicialComplex:
    facets: list[list[int]] = list(find_cliques(graph))
    return clique_complex_from_iterable(facets)

if __name__ == "__main__":
    clique_complex_from_iterable([[1,2], [2,3], [1,3]])