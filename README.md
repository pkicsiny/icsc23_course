# iCSC23 Course - Multiplatform Programming with Python

This repository contains reference materials for the course and instructions on how to set up the tutorial environment. </br>
- The folder `lecture_examples` contains code snippets that were shown during the lecture. These are not part of the tutorial and are stored here for reference only so that you can try them out at home.
- The folder `tutorial` contains the tutorial exercises. Please follow the steps below for the setup.

## Tutorial setup

Click on the banner below:

[![SWAN](https://swan.web.cern.ch/sites/swan.web.cern.ch/files/pictures/open_in_swan.svg)](https://swan-k8s.cern.ch/user-redirect/download?projurl=https%3A%2F%2Fgithub.com%2Fpkicsiny%2Ficsc23_course.git)
    
- This connects you to the CERN SWAN service where you will be requested to configure the work environment: In the first dropdown window select `102b Cuda 11.7.1 (GPU)` and press "Start my session"
 at the bottom. You don't have to change the other settings.
- The repository will be automatically cloned to your CERNBox SWAN directory. Navigate to the `tutorial/exercises` folder & have fun!
 
## Tutorial exercises

The goal of the tutorial is to demonstrate the basic usecases of the Python libraries CFFI, CuPy & PyOpenCL. There are 3 exercises:
- __Exercise 1:__ This exercise is about a speeding up a Python function that computes the n-th Fibonacci number. We will use CFFI to create a C extension module, load it in Python then test it. Then we compare the execution times of the pure Python and the CFFI implementation.
- __Exercise 2:__ This exercise is a demo of CuPy (`exercise_2a`) and PyOpenCL (`exercise_2b`). We will create and execute a simple elementwise kernel on the GPU and use the math API of the libraries to perform the same operation purely in Python. We then do a simple profiling of the execution time on the GPU.
- __Exercise 3:__ This exercise is about templating, i.e. we will simply create a Python wrapper around a C function. The wrapper takes as input the desired context (`cpu`, `gpu_cuda` or `gpu_opencl`) then the script parses the C function and turns it into a CPU or GPU kernel by adding the relevant qualifiers, then loads the relevant library and executes it on the requested platform. This exercise is meant to show that we can write our performance critical C code only once and use Python's string parsing methods to fine tune it for a specific context.

Exercises 1 and 3 contain parts where you are asked to fill in some code. For these you may find the solutions in the `tutorial/exercise_solutions` folder.
## References & resources

[1] Programming Massively Parallel Processors, David B. Kirk, Wen-mei W. Hwu </br>
https://safari.ethz.ch/architecture/fall2019/lib/exe/fetch.php?media=2013_programming_massively_parallel_processors_a_hands-on_approach_2nd.pdf

[2] CUDA Programming guide </br> 
https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html

[3] OpenCL API Specification </br> 
https://registry.khronos.org/OpenCL/

[4] Easy, Effective, Efficient GPU Programming with PyOpenCL and PyCUDA, Andreas Kl??ckner </br> 
https://www.bu.edu/pasi/courses/gpu-programming-with-pyopencl-and-pycuda/

[5] CFFI documentation </br> 
https://cffi.readthedocs.io/en/latest/index.html

[6] CuPy documentation </br> 
https://docs.cupy.dev/en/stable/index.html

[7] PyOpenCL documentation </br> 
https://documen.tician.de/pyopencl/index.html

[8] Tool used to create code snippet images for the lecture </br>
https://carbon.now.sh/
