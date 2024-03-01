"""
Excel colunm names looks like that:
A B C ... AA AB AC ... BA BB BC ... AAA AAB AAC ...

English alphabet consists of 26 letters
Let's imagine it as a two-dimensional array or square matrix

L   1  2  3  4  ... 26
0   A  B  C  D  ... Z
-------------
    27 28 29 30 ... 52
1   AA AB AC AD ... AZ
2   BA BB BC BD ... BZ
3   CA CB CC CD ... CZ
...
26  ZA ZB ZC ZD ... ZZ
-------------
Total count of elements in square matrix is n x m
where:
n - number of cols
m - number of rows
So - 26 x 26 = 26 ^ 2
-------------
Such principle is applied to three-dimensional matrix: 26 ^ 3 and so on
-------------
ASCII codes range for uppercased alphabet:

Letter  Code        Index determines as
A       65          26^0 * (65 - 64) = 1
B       66          26^0 * (66 - 64) = 2
C       67          26^0 * (67 - 64) = 3
...
Z       90          26^0 * (90 - 64) = 26

AA      -           26^1 * (65 - 64) + 26^0 * (65 - 64) = 27
AB      -           26^1 * (65 - 64) + 26^0 * (66 - 64) = 28
...
BA      -           26^1 * (66 - 64) + 26^0 * (65 - 64) = 53
BB      -           26^1 * (66 - 64) + 26^0 * (65 - 64) = 54
...
CA      -           26^1 * (67 - 64) + 26^0 * (65 - 64) = 79
...
ZA      -           26^1 * (90 - 64) + 26^0 * (65 - 64) = 677
...
AAA     -           26^2 * (65 - 64) + 26^1 * (65 - 64) + 26^0 * (65 - 64) = 703
...
ABA     -           26^2 * (65 - 64) + 26^1 * (66 - 64) + 26^0 * (65 - 64) = 729
...
AAAA    -           26^3 * (65 - 64) + 26^2 * (65 - 64) + 26^1 * (65 - 64) + 26^0 * (65 - 64) = ???
"""

def index_of_colunm(col: str) -> int:
    index = 0
    trace = []
    
    for idx, char in enumerate(reversed(col)):
        trace.append((char, idx))
        index += 26 ** idx * (ord(char) - 64)

    print(f'tracing of calculation "{col}" index:')
    for char, idx in reversed(trace):
        print(f'{char}: 26^{idx} * ({ord(char)} - 64) +')

    return index


print(f'Index: {index_of_colunm('ABA')}')

