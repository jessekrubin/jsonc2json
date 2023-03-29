use json_comments::StripComments;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyBytes;
use std::io::{ErrorKind, Read};
use std::vec::Vec;

// Bytes function
#[pyfunction]
fn jsonc2json_bin<'a>(py: Python<'a>, b: &[u8]) -> PyResult<&'a PyBytes> {
    let mut buf = Vec::new();
    let result = StripComments::new(b).read_to_end(&mut buf);

    // raise error if invalid json
    match result {
        Ok(_) => {}
        Err(e) => {
            if e.kind() == ErrorKind::InvalidData {
                return Err(PyValueError::new_err("Invalid JSON"));
            }
        }
    }
    let pbres = PyBytes::new(py, &buf[..]);
    Ok(pbres)
}

// string function
#[pyfunction]
fn jsonc2json_str(string: String) -> PyResult<String> {
    let mut stripped = String::new();
    let result = StripComments::new(string.as_bytes()).read_to_string(&mut stripped);
    match result {
        Ok(_) => {}
        Err(e) => {
            if e.kind() == ErrorKind::InvalidData {
                return Err(PyValueError::new_err("Invalid JSON"));
            }
        }
    }
    Ok(stripped)
}

/// A Python module implemented in Rust.
#[pymodule]
fn libjsonc2json(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add("__version_lib__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(jsonc2json_str, m)?)?;
    m.add_function(wrap_pyfunction!(jsonc2json_bin, m)?)?;
    Ok(())
}
