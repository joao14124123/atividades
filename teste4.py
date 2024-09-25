def test(n):
    if n <= 0:
        return False
    else:
        return True

def sum(n,a,p):
    if n == 0:
        return 0
    else:
        return (-1) ** a/ ((p + sum(n - 1, a + 1, p + 2) ** 3) * 32) ** (1 / 3)

n = int(input("Enter the number of the term you want to calculate: "))

if test(n):
    a = 2
    p = 1

    print("Total: ", sum(n, a, p))
else:
    print("Error")