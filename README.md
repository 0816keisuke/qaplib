# QAPLIB

The Quadratic Assignment Problem (QAP) is one of the combinatorial optimization problems.

In this problem, a set of $n$ facilities and a set of $n$ locations are given, and some distance is defined between each facilities and some flow is defined between each location.

The objective is to find an assignment of facilities to locations that minimizes the sum of the product of the flows between each facility and the distance to which each facility is assigned.

Let us define a set of F of $n$ facilities as $F=\{f_1, f_2, ..., f_n\}$.

The object function is expressed as follows:

$$
\sum_{F} w(f_i, f_j)d(f_i, f_j)
$$

## Hot to Use

To download the repository:

```shell
git clone https://github.com/0816keisuke/qaplib.git
```

To get all instances:

```shell
python3 get_instance.py
```