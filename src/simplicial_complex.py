from simplicialpy import Simplex, SimplicialComplex
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

if __name__ == "__main__":
    sc = SimplicialComplex([[1,2,3]])
    sc2 = SimplicialComplex(sc.k_faces(1))
    print(sc)
    print(sc2)
    betti_numbers = sc.compute_betti_numbers()
    print(betti_numbers)
    print(sc2.betti_numbers)
    sc3: SimplicialComplex = sc.union(SimplicialComplex(SimplicialComplex([[1,2,4]]).k_faces(1)))
    print(sc3)
    print(sc3.betti_numbers)