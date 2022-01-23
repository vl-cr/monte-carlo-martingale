# Accelerating Monte Carlo simulations with Numba

It is well known that Python is slow compared to some other languages such as C++ or Java. As a Data Scientist, I wasn't bothered by this too much until I started experimenting with Monte Carlo simulations: running millions of simulations can be very time-consuming. 

Writing high-performance Python code for these simulations can be a challenge, even for experienced developers. [Numpy](https://numpy.org/) is the first big step toward faster code because it allows you to capitalize on calculations with arrays, and the core of the package is well-optimized C code. For the record, I also experimented with [parallel processing](https://docs.python.org/3/library/multiprocessing.html), but was not impressed with the results.

Looking for something even more efficient, I eventually found [Numba](https://numba.pydata.org): a JIT compiler that translates a subset of Python and NumPy code into fast machine code. And all you have to do to make it work is to apply the Numba decorator to a Python function, that's all. At first it sounds too good to be true.

So I decided to give Numba a try and see how it worked in practice. But instead of writing boring functions with meaningless heavy calculations, I decided to run Monte Carlo simulations on the Martingale Strategy. The strategy itself will be explained in the notebook, but you don't have to follow the whole thought process: you can skip to the comparison of execution times of normal Python vs. Numba-modified functions.

So we'll try to answer the following questions:
- How much faster is the code when using Numba?
- Are Numba's limitations a hindrance to the code-writing process?
- Even if it is well known that the Martingale Strategy has a negative expected value, what is the probability of winning x2 or x10 of your pot with it?

The `1.monte_carlo_martingale_strategy` notebook contains everything you need to answer these questions: code, comments and final results.

---

To run the notebook: run `pip install -r requirements.txt` in a virtual environment to install the dependencies. Alternatively, you can use [Poetry](https://python-poetry.org/) for that.
