# iCSC23 Course - Multiplatform Programming with Python

## Installation
#### Requirements
- Python: >v3.7.0
- [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit): >v10.2
-
'pip install cffi'
'pip install cupy-cuda11x'

## Tutorial

The goal of this tutorial is to play around with the Python libraries CFFI, CuPy & PyOpenCL using the toy problem of elementwise matrix multiplication. There are 3 exercises:
- Exercise 1: Implement a function in Python that multiplies two matrices. Implement the same function in C. Use CFFI to create a C extension module, load it in Python then test it. Compare the execution times of the pure Python and the CFFI implementation for different sizes of matrices.
- Exercise 2: Modify the C function with the appropriate CUDA and OpenCL kernel qualifiers to create two GPU kernels. Use CuPy and PyOpenCL to execute the kernels on the GPU. Compare the GPU execution times with different martix sizes and using different block sizes. Try to make them run as fast as possible.
- Exercise 3: Create a Python wrapper around the C function. The Python script takes as input the desired context (`cpu`, `gpu_cupy` or `gpu_pyopencl`). If the input is GPU, the script parses the C function and turns it into a GPU kernel by adding the relevant qualifiers, loading the relevant library and executing it. Use standard Python libraries for string parsing.

## References & resources

[1] Programming Massively Parallel Processors, David B. Kirk, Wen-mei W. Hwu </br>
https://safari.ethz.ch/architecture/fall2019/lib/exe/fetch.php?media=2013_programming_massively_parallel_processors_a_hands-on_approach_2nd.pdf

[2] CUDA Programming guide </br> 
https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html

[3] OpenCL API Specification </br> 
https://registry.khronos.org/OpenCL/

[4] Easy, Effective, Efficient GPU Programming with PyOpenCL and PyCUDA, Andreas Klöckner </br> 
https://www.bu.edu/pasi/courses/gpu-programming-with-pyopencl-and-pycuda/

[5] CFFI documentation </br> 
https://cffi.readthedocs.io/en/latest/index.html

[6] CuPy documentation </br> 
https://docs.cupy.dev/en/stable/index.html

[7] PyOpenCL documentation </br> 
https://documen.tician.de/pyopencl/index.html
