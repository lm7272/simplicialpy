from .simplicialpy import SimplicialComplex
from .types import Edge, Simplex

from xgi.core.simplicialcomplex import SimplicialComplex as XGISimplicialComplex
from networkx.classes.graph import Graph
from networkx import find_cliques

def complex_from_xgi_complex(sc: XGISimplicialComplex) -> SimplicialComplex:
    facets: list[frozenset[int]] = sc.edges.maximal().members()
    return SimplicialComplex([list(facet) for facet in facets])

def clique_complex_from_list(cliques: list[Edge]) -> SimplicialComplex:
    return SimplicialComplex(facets=cliques)

def clique_complex_from_nx(graph: Graph) -> SimplicialComplex:
    facets: list[Simplex[int]] = find_cliques(graph)
    return clique_complex_from_list(facets)

if __name__ == "__main__":
    clique_complex_from_list([[1,2], [2,3], [1,3]])