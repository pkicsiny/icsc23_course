# file: "cffi_example_sum.py"
import cffi
import time

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
, libraries=["m"]
, extra_compile_args=["-ffast-math", "-O3"]
, extra_link_args=["-ffast-math", "-O3"]
)

ffi_interface.compile(verbose=True)

from _sumVec import ffi, lib
import numpy as np

for n in [int(1e1), int(1e2), int(1e3), int(1e4), int(1e5), int(1e6), int(1e7), int(1e8)]:
    x = np.random.randn(n)
    x_cffi = ffi.cast( "double *", ffi.from_buffer(x))

    start = time.time()
    y = lib.sumVec(x_cffi, len(x))
    end = time.time()
    print("vector length", n)
    print("cffi:", end - start, "[s]")

    start = time.time()
    y_np = x.sum()
    end = time.time()
    print("numpy:", end - start, "[s]")
    assert np.allclose(y_np, y)
