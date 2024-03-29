# Accelerating Monte Carlo simulations with Numba

It is well known that Python is slow compared to some other languages such as C++ or Java. As a Data Scientist, I wasn't bothered by this too much until I started experimenting with Monte Carlo simulations: running millions of simulations can be very time-consuming. 

Writing high-performance Python code for these simulations can be a challenge, even for experienced developers. [Numpy](https://numpy.org/) is the first big step towards faster code because it allows you to capitalize on calculations with arrays, and the core of the package is well-optimized C code. For the record, I also experimented with [parallel processing](https://docs.python.org/3/library/multiprocessing.html), but the results were far from impressive.

Looking for something even more efficient, I eventually found [Numba](https://numba.pydata.org): a JIT compiler that translates a subset of Python and NumPy code into fast machine code. And all you have to do to make it work is to apply the Numba decorator to a Python function, that's all. At first, it sounds too good to be true.

So I decided to give Numba a try and see how it worked in practice. But instead of writing boring functions with meaningless heavy calculations, I decided to run Monte Carlo simulations on the Martingale Strategy. The strategy itself will be explained in the notebook, but you don't have to follow the whole thought process: you can skip to the comparison of execution times of normal Python vs. Numba-modified functions.

We'll try to answer the following questions:
- Can Numba make the code significantly faster?
- Are Numba's limitations a hindrance to the code-writing process?
- Even though it is known that the Martingale Strategy has a negative expected value, what is the probability of winning x2 or x10 of your initial pot with it?

[1.monte_carlo_martingale](1.monte_carlo_martingale.ipynb): this notebook contains everything you need to answer these questions: code, comments and final results.


## Installation

> Tested on Python version: 3.9.10

To run the notebook: create a new virtual environment and activate it. Install [JupyterLab or Jupyter Notebook](https://jupyter.org/install) (recommended). Alternatively, you can use [VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [DataSpell](https://www.jetbrains.com/dataspell/) etc.

To install the dependencies: run `pip install --user -r requirements.txt` in your virtual environment. 

Alternatively, instead of the two steps above, it is recommended to use [Poetry](https://python-poetry.org/). Both "pyproject.toml" and "poetry.lock" files can be found in the root directory. 

Run `poetry install` and then `poetry shell` to create a shell and activate the new virtual environment (with all the dependencies installed). In this shell, `jupyter notebook` command will work by default.
