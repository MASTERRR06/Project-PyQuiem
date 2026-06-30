def towerhanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from", a, "to", c)
        return
    towerhanoi(n - 1, a, c, b)
    print("Move disk", n, "from", a, "to", c)
    towerhanoi(n - 1, b, a, c)

n = int(input("Enter n: "))
towerhanoi(n, 'A', 'B', 'C')