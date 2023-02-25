# file: "cupy_example_raw.py"
import numpy as np
import cupy as cp

x1 = np.array([1, 3, 5, 7, 9], dtype=np.float64)
x2 = np.array([2, 4, 6, 8, 10], dtype=np.float64)

x1_dev = cp.array(x1)
x2_dev = cp.array(x2)

y_dev = cp.zeros_like(x1_dev)

source_str = r"""
extern "C"{
__global__
void mymul(int n,
    const double* x1, const double* x2, double* y)
{
    int tid = blockDim.x * blockIdx.x + threadIdx.x;
    if (tid < n){
      y[tid] = x1[tid] * x2[tid];
    }
}
}"""

module = cp.RawModule(code=source_str)
mymul_kernel = module.get_function("mymul")

blocksize = 2
n_blocks = int(np.ceil(len(x1) / blocksize))
mymul_kernel(grid=(n_blocks,), block=(blocksize,), args=(np.int32(len(x1)), x1_dev, x2_dev, y_dev))
print(y_dev, type(y_dev), y_dev.dtype)

y = y_dev.get()
print(y, type(y), y.dtype)
