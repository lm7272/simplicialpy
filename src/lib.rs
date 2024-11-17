use pyo3::prelude::*;

use simplicial_topology::simplicial_complex::simplicial_complex::SimplicialComplex;
use simplicial_topology::simplicial_complex::simplex::{Simplex, Facet};

#[pyclass(name = "SimplicialComplex")]
#[derive(Clone)]
struct SimplicialComplexWrapper {
    sc: SimplicialComplex
}

fn facets_as_vec(facets: Vec<Facet>) -> Vec<Vec<usize>> {
    facets.into_iter().map(|f| f.vertices).collect()
}

#[pymethods]
impl SimplicialComplexWrapper {
    #[new]
    fn init(facets: Vec<Vec<usize>>) -> Self {
        SimplicialComplexWrapper { sc: SimplicialComplex::new_from_vec(facets) }
    }

    #[getter]
    fn dimension(&self) -> isize {
        self.sc.dimension()
    }

    fn is_connected(&self) -> bool {
        self.sc.is_connected()
    }

    fn add_simplex(&mut self, simplex: Vec<usize>) {
        self.sc.add_simplex(Facet::new(simplex))
    }

    fn union(&mut self, other: Self) -> Self {
        Self { sc: self.sc.union(&other.sc) }
    }

    #[pyo3(signature = (dimensions=None))]
    fn compute_betti_numbers(&self, dimensions: Option<Vec<usize>>) -> Vec<i32> {
        match dimensions {
            Some(dimensions) => {dimensions.into_iter().map(|dim| self.sc.kth_betti_number(dim)).collect()}
            None => {self.sc.betti_numbers()}
        }  
    }

    fn k_faces(&self, dim: usize) -> Vec<Vec<usize>> {
        facets_as_vec(self.sc.k_faces(dim))
    }

    #[getter]
    fn facets(&self) -> Vec<Vec<usize>> {
        facets_as_vec(self.sc.facets.clone())
    }

    #[getter]
    fn simplices(&self) -> Vec<Vec<usize>>{
        let sc_dim = self.dimension();
        if sc_dim < 0 {
            return Vec::new()
        }
        (1..(sc_dim+1)).flat_map(|dim| self.k_faces(dim.try_into().unwrap())).collect()
    }

    fn __str__(&self) -> PyResult<String> {
        Ok(format!("SimplicialComplex of dimension {} with {} facets.", self.dimension(), self.sc.facets.len()))
    }

    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("SimplicialComplex(Vertices: {:?}, Facets: {:?})", self.k_faces(0), self.facets()))
    }

    fn compute_betti_number(&self, dimension: usize) -> i32 {
        let betti_number = self.compute_betti_numbers(Some(vec![dimension]));
        match betti_number.first() {
            Some(first) => {*first}
            None => {0}
        }
    }

    #[getter]
    fn betti_numbers(&self) -> Vec<i32> {
        self.compute_betti_numbers(None)
    }
}

#[pymodule]
fn simplicialpy(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<SimplicialComplexWrapper>()?;
    Ok(())
}
