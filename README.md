# iCSC23 Course - Multiplatform Programming with Python

## Tutorial

The goal of this tutorial is to try out the Python libraries CFFI, CuPy & PyOpenCL on the toy problem of elementwise matrix multiplication. There are 3 exercises:
- Implement a function in python that multiplies two matrices. Implement the same function in C. Use CFFI to create a C extension module, load it in Python then test it. Compare the execution times of the pure Python and the CFFI implementation for different sizes of matrices.
- Modify the C function with the appropriate CUDA and OpenCL kernel qualifiers to create two GPU kernels. Use CuPy and PyOpenCL to execute the kernels on the GPU. Compare the GPU execution times with different martix sizes and using different block sizes.
- Create a Python wrapper around the C function. The Python script takes as input the desired context (`cpu`, `gpu_cupy` or `gpu_pyopencl`). If the input is GPU, the script parses the C function and turns it into a GPU kernel by adding the relevant qualifiers, loading the relevant library and executing it. Use standard Python libraries for string parsing.

## References & resources

[1] Programming Massively Parallel Processors, David B. Kirk, Wen-mei W. Hwu </br>
https://safari.ethz.ch/architecture/fall2019/lib/exe/fetch.php?media=2013_programming_massively_parallel_processors_a_hands-on_approach_2nd.pdf

[2] CUDA Programming guide </br> 
https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html

[3] OpenCLAPISpecification </br> 
https://registry.khronos.org/OpenCL/

[4] Easy, Effective, Efficient GPU Programming with PyOpenCL and PyCUDA, Andreas Klöckner </br> 
https://www.bu.edu/pasi/courses/gpu-programming-with-pyopencl-and-pycuda/

[5] CFFIdocumentation </br> 
https://cffi.readthedocs.io/en/latest/index.html

[6] CuPydocumentation </br> 
https://docs.cupy.dev/en/stable/index.html

[7] PyOpenCLdocumentation </br> 
https://documen.tician.de/pyopencl/index.html
