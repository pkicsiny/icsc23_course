# file: "cffi_example_raw.py"
import cffi

ffi_interface = cffi.FFI()

ffi_interface.cdef(
    """
    double sumVec(double*, int);
    """
)

ffi_interface.set_source("_sumVec",
r"""
double sumVec(double* v, int n){
  double sum = 0.0;
  for (int i=0; i<n; i++){
    sum += v[i];
  }
  return sum;
}
"""
)

ffi_interface.compile(verbose=True)

from _sumVec import ffi, lib
import numpy as np

x = np.random.randn(10)
x_cffi = ffi.cast( "double *", ffi.from_buffer(x))

y = lib.sumVec(x_cffi, len(x))
print(y, type(y))
