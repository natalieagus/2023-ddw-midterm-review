# Implement a recursive function to find the nth term of a geometric sequence.
# A geometric sequence is a sequence of numbers where each term is found by multiplying the previous term by a fixed, non-zero number called the common ratio.
# The general formula for the nth term of a geometric sequence is: a * r^(n-1), where a is the first term and r is the common ratio.
# Write a Python function called geometric_sequence_term that takes three arguments: the first term a, the common ratio r, and the term number n, and returns the nth term of the geometric sequence.
# For example, geometric_sequence_term(2, 3, 4) should return 54 because the 4th term of the geometric sequence with a first term of 2 and a common ratio of 3 is 54.


def geometric_sequence_term(a, r, n):
    pass


# Test the function
a = 2
r = 3
n = 4
print(
    f"The {n}-th term of the geometric sequence is: {geometric_sequence_term(a, r, n)}"
)
