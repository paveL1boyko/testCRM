#
# print(f'{random.choice([1, 4.4, 55]) = }')
# _str = 'new str raer'
# new_str = match.group() if (match := re.match(r'n\S+', _str)) else None
# print(new_str)
#
#
# # a,b ,c только поизиционные параметры  e, f тольк именнованные парамерты
# def new_str(a, b, c, /, d, *, e, f, **kwargs):
#     return a, b, c, d, e, f, kwargs['name'], kwargs['name2']


# print(f'{new_str(1, 2, 3, d=4, e=5, f=6, **dict(name=1, name2=2)) = }')
# дикт в питоне 3.6 >= упорядочен те

# while value := input('введите что то: '):
#     print(value)

# print([cube for i in range(3) if (cube := (lambda x: x ** 3)(i)) < 20])

# def my_zip_longest(*args, default=None):
#     args = list(map(list, args))
#     while any(args):
#         print(args)
#         yield tuple((i.pop(0) if i else default) for i in args)
#
#
# print(list(my_zip_longest([1, 4, 5, 5], [1])))
# import timeit
# print(min(timeit.repeat(stmt='[abs(i) for i in range(10000)]', number=1000, repeat=5)))
# print(min(timeit.repeat(stmt='list(map(lambda x: abs(x), range(10000)))', number=1000, repeat=5)))
# from tests2 import a
# a.append(1)
# print(a)

# print(a)
#