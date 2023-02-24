# iCSC23 Course - Multiplatform Programming with Python

This repository contains all reference materials related to the course.
## Tutorial setup

The tutorial uses the [CERN SWAN](https://swan.web.cern.ch/swan/) service. </br>
To connect you make sure you have a CERN lightweight account. </br>
Once connected you are requested to configure the work environment: In the first dropdown windo select `102b_cuda` then press "Start my session"
 at the bottom.
 
## Tutorial exercises

The goal of this tutorial is to demonstrate the basic usecases of the Python libraries CFFI, CuPy & PyOpenCL. There are 3 exercises:
- Exercise 1: This exercise is about a speeding up a function that computes the n-th Fibonacci number. We will use CFFI to create a C extension module, load it in Python then test it. Then we compare the execution times of the pure Python and the CFFI implementation of the function.
- Exercise 2: This exercise is a demo of CuPy and PyOpenCL. We will create and execute a simple elementwise kernel on the GPU and use the math API of the libraries to perform the same operation purely in Python. We then do a simple benchmark of the execution time on the GPU. Try to make them run as fast as possible.
- Exercise 3: In this exercise we will create a Python wrapper around a C function. The Python script takes as input the desired context (`cpu`, `gpu_cupy` or `gpu_pyopencl`). Then the script parses the C function and turns it into a GPU kernel by adding the relevant qualifiers, then loads the relevant library and executes it. This exercise shows thsat we can write a template and fine tune it for the specific context using Python's string parsing methods.

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

[8] Tool used to create code snippet images </br>
https://carbon.now.sh/pGOnb5JKK7Y83S0VNUCC
