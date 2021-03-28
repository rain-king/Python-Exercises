# Description of the exercises
## Chessboard
Given two numbers n and m. Create a two-dimensional array of size (n×m) and
populate it with the characters "`.`" and "`*`" in a checkerboard pattern. The
top left corner should have the character "`.`".

## Diagonals
Given an integer n, produce a two-dimensional array of size `n` by `n` and
complete it according to the following rules, and print with a single space
between characters:
- On the main diagonal write `0`.
- On the diagonals adjacent to the main, write `1`.
- On the next adjacent diagonals write `2` and so forth. 
Print the elements of the resulting array.

## Maximum
Given two integers representing the rows and columns `m` by `n`, and subsequent `m`
rows of `n` elements, find the index position of the maximum element and print
two numbers representing the index `[i, j]` or the row number and the column
number. If there exist multiple such elements in different rows, print the one
with smaller row number. If there multiple such elements occur on the same
row, output the smallest column number.

## Multiply a matrix by a matrix
Given three positive integers `m`, `n` and `r`, `m` lines of `n` elements,
giving an `m` by `n` matrix `A`, and `n` lines of r elements, giving an `n` by
`r` matrix `B`, form the product matrix `AB`, which is the `m` by `r` matrix
whose `(i, k)` entry is the sum <br>
`A[i][1]∗B[1][k] + ... + A[i][n]∗B[n][k]` <br>
and print the result.

## Multiply a matrix by a scalar
Given two positive integers `m` and `n`, `m` lines of `n` elements, giving an
`m` by `n` matrix `A`, followed by one integer `c`, multiply every entry of
the matrix by `c` and print the result. 

## Side diagonal
Given an integer n, create a two-dimensional array of size (n×n) and populate
it as follows, with spaces between each character:
- The positions on the minor diagonal (from the upper right to the lower left
corner) receive 1.
- The positions above this diagonal recieve 0.
- The positions below the diagonal receive 2. 
Print the elements of the resulting array. 

## Snowflake
Given an odd number integer `n`, produce a two-dimensional array of size
`n` by `n`. Fill each element with a single character
string of `"."`. Then fill the middle row, the middle column and
the diagnals with the single character string of `"*"` (an image
of a snow flake). Print the array elements in `n` by `n` rows and columns and
separate the characters with a single space.

## Swap columns
Given two positive integers `m` and `n`, `m` lines of `n` elements, giving an
`m` by `n` matrix `A`, followed by two non-negative integers `i` and `j` less than
`n`, swap columns `i` and `j` of `A` and print the result.  Write a function
`swap_columns(A, i, j)` and call it to exchange the columns.