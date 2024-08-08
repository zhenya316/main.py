# def summa_all(*args):
#     m = args[0]
#     n = 0
#     if isinstance(m, int) or isinstance(m, float):
#         n += int(m)
#     elif isinstance(m, str):
#         n += len(m)
#     elif isinstance(m, list) or isinstance(m, tuple) or isinstance(m, set):
#         if len(m) < 2:
#             summa_all
#         else:
#             for i in m:
#                 if isinstance(i, int) or isinstance(i, float):
#                     n += int(i)
#                 elif isinstance(i, str):
#                     n += len(i)
#
#     if len(m) == 0:
#         return 0
#     else:
#         return n + summa_all(m[1:])

# def summa_all(*m, **n):
#     p = a
#     print(type(m), type(n))
#     print(m, n)
#     print(len(p))
#     for i,j in p.items():
#         print(i,j)
#
#
#
# a = {'a': 1, 'b': 2, 'c': 3}
# summa_all(a)
# a = [(1,2,3)]

def summa_all(j, *m, **n):
    qwe = 0
    for i in a:
        print(i)
        qwe += i

    return qwe


a = (1,2,3)
b = summa_all(a)
print(b)