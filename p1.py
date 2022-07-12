# Solve the problem from the first set here
# problem 3

def digits_in_list(n, k, l):  # this function puts the digits of n in list l

    for i in range(0, k):
        l.append(n % 10)
        n = n // 10


def nr_digits(n):  # this function just count the number of digits of n
    k = int(0)
    while n:
        k = k + 1
        n = n // 10
    return k


def sort(l, k):  # just s sort function
    for i in range(0, k):
        for j in range(0, k):
            if (l[i] < l[j]):
                b = l[i]
                l[i] = l[j]
                l[j] = b


def result_creation(l, k):  # this function just combine the sorted list in one number
    m = int(0)
    for i in range(0, k):
        m = m * 10 + l[i]
    return m


def function():
    l = []
    n = int(input())
    p = nr_digits(n)
    digits_in_list(n, p, l)
    sort(l, p)
    n = int(result_creation(l, p))
    print(n)


function()
