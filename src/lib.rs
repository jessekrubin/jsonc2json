use std::io::{ErrorKind, Read};
use std::vec::Vec;

use json_comments::StripComments;

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::pybacked::{PyBackedBytes, PyBackedStr};
use pyo3::types::PyBytes;

#[derive(FromPyObject)]
pub enum BytesOrString {
    Str(PyBackedStr),
    Bytes(PyBackedBytes),
}

/// Strip comments from JSON bytes and return JSON as a bytes object
#[pyfunction]
fn jsonc2json_bin<'a>(py: Python<'a>, b: &[u8]) -> PyResult<Bound<'a, PyBytes>> {
    let mut buf = Vec::new();
    let result = StripComments::new(b).read_to_end(&mut buf);
    match result {
        Ok(_) => {
            let py_bytes = PyBytes::new_bound(py, &buf);
            Ok(py_bytes)
        }
        Err(e) => {
            if e.kind() == ErrorKind::InvalidData {
                Err(PyValueError::new_err("Invalid JSON"))
            } else {
                Err(PyValueError::new_err("Unknown error"))
            }
        }
    }
}

/// Strip comments from JSON string and return JSON as a string
#[pyfunction]
fn jsonc2json_str(string: String) -> PyResult<String> {
    let mut stripped = String::new();
    let result = StripComments::new(string.as_bytes()).read_to_string(&mut stripped);
    match result {
        Ok(_) => Ok(stripped),
        Err(e) => {
            if e.kind() == ErrorKind::InvalidData {
                Err(PyValueError::new_err("Invalid JSON"))
            } else {
                Err(PyValueError::new_err("Unknown error"))
            }
        }
    }
}

/// A Python module implemented in Rust.
#[pymodule]
#[pyo3(name = "_jsonc2json")]
fn libjsonc2json(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version_lib__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(jsonc2json_str, m)?)?;
    m.add_function(wrap_pyfunction!(jsonc2json_bin, m)?)?;
    Ok(())
}
