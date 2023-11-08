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

## Fromat

- `n` is number of facilities
- `opt` is an optimal cost value
- `d_(i,j)` is a distance value between location `i` and `j`
- `w_(k,l)` is a weight value between facility `k` and `l`

```txt
n opt
d_(1,1), d_(1,2), ..., d_(1,n)
d_(2,1), d_(2,2), ..., d_(2,n)
...
d_(n,1), d_(n,2), ..., d_(n,n)
w_(1,1), w_(1,2), ..., w_(1,n)
w_(2,1), w_(2,2), ..., w_(2,n)
...
w_(n,1), w_(n,2), ..., w_(n,n)
```

Example:

```txt
5 50
0 1 1 2 3
1 0 2 1 2
1 2 0 1 2
2 1 1 0 1
3 2 2 1 0
0 5 2 4 1
5 0 3 0 2
2 3 0 0 0
4 0 0 0 5
1 2 0 5 0
```


## URL

These instances are cited from:
- http://mistic.heig-vd.ch/taillard/problemes.dir/qap.dir/qap.html
- https://qaplib.mgi.polymtl.ca/