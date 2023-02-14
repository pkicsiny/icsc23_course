# file: "pyopencl_example_raw.py"
import numpy as np
import pyopencl as cl
import pyopencl.array as cl_array

ctx = cl.create_some_context(interactive=False)
queue = cl.CommandQueue(ctx)

x1 = np.array([1, 3, 5, 7, 9], dtype=np.float64)
x2 = np.array([2, 4, 6, 8, 10], dtype=np.float64)

x1_dev = cl_array.to_device(queue, x1)
x2_dev = cl_array.to_device(queue, x2)

y_dev = cl_array.zeros(queue, len(x1_dev), dtype=np.float64)

source_str = r"""
__kernel
void mymul(int n,
    __global const double* x1,
    __global const double* x2,
    __global double* y)
{
    int tid = get_global_id(0);
    y[tid] = x1[tid] * x2[tid];
}"""

prg = cl.Program(ctx, source_str).build()
mymul_kernel = prg.mymul
mymul_kernel(queue, (len(x1),), None, np.int32(len(x1)), x1_dev.data, x2_dev.data, y_dev.data)
print(y_dev, type(y_dev), y_dev.dtype)

y = y_dev.get()
print(y, type(y), y.dtype)

