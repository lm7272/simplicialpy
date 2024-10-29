from .simplicialpy import Simplex, SimplicialComplex
from xgi.core.simplicialcomplex import SimplicialComplex as XGISimplicialComplex
from networkx.classes.graph import Graph
from networkx import find_cliques

def complex_from_xgi_complex(sc: XGISimplicialComplex) -> SimplicialComplex:
    facets = sc.edges.maximal().members()
    return SimplicialComplex([list(facet) for facet in facets])

def clique_complex_from_list(cliques: list[Simplex]) -> SimplicialComplex:
    return SimplicialComplex(facets=cliques)

def clique_complex_from_nx(graph: Graph) -> SimplicialComplex:
    facets: list[Simplex] = find_cliques(graph)
    return clique_complex_from_list(facets)
