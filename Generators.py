def show():
    n=1
    while n<=5:
        sq=n*n
        yield sq
        n=n+1
val=show()
for i in val:
    print(i)


