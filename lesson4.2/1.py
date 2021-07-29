
def foo(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield "Четное"
        else:
            yield i


for i in foo(10):
    print(i)
