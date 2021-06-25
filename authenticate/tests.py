# # #
# # # print(f'{random.choice([1, 4.4, 55]) = }')
# # # import re
# # #
# # # _str = 'new str raer'
# # # # match := re.match(r'n\S+', _str)
# # # new_str = match.group() if (match := re.match(r'n\S+', _str)) else None
# # # print(new_str)
# #
# # #
# # # a,b ,c только поизиционные параметры  e, f тольк именнованные парамерты
# # # def new_str(c, f, *, d, **kwargs):
# # #     return c, d, f
# # #
# # #
# # # new_str(1, 3, d=34, **dict(a=3, ab=4))
# #
# # # print(f'{new_str(1, 2, 3, d=4, e=5, f=6, **dict(name=1, name2=2)) = }')
# # # дикт в питоне 3.6 >= упорядочен те
# # #
# # # while value := input('введите что то: '):
# # #     print(value)
# #
# # # print([cube for i in range(3) if (cube := (lambda x: x ** 3)(i)) < 20])
# #
# # # def my_zip_longest(*args, default=None):
# # #     args = list(map(list, args))
# # #     while any(args):
# # #         print(args)
# # #         yield tuple((i.pop(0) if i else default) for i in args)
# # #
# # #
# # # print(list(my_zip_longest([1, 4, 5, 5], [1])))
# # # import timeit
# # # print(min(timeit.repeat(stmt='[abs(i) for i in range(10000)]', number=1000, repeat=5)))
# # # print(min(timeit.repeat(stmt='list(map(lambda x: abs(x), range(10000)))', number=1000, repeat=5)))
# # # from tests2 import a
# # # a.append(1)
# # # print(a)
# #
# # # print(a)
# # #
# # # def get(self, *args, **kwargs):
# # #     pass
# # #
# # # get(4334, hekk=34)
# # # def ff():М) = }')
# # # import abc
# # #
# # #
# # # class ABS(abc.ABC):
# # #     def __init__(self):
# # #         pass
# # #
# # #     @abc.abstractmethod
# # #     def hello(self):
# # #         return
# #
# # # a = 3
# # # b = 3
# # # print(hash(a), hash(b),id(a), id(b) )
# # # a = list((2,3,4,5,6))
# # # for i in a:
# # #     a.remove(i)
# # # print(a)
# #
# #
# # # assert 2 + 2 == 5, "Houston we've got a problem"
# # # class A:
# # #     pass
# # #
# # #
# # # class C(A):
# # #     pass
# # #
# # #
# # # class B():
# # #     pass
# # #
# # #
# # # class D(A, C):
# # #     pass
# # #
# # #
# # # d = D()
# # # import dataclasses
# # # @dataclasses
# # # class GG:
# # #     name: str
# # #     age:
# # # a = [1, 2, 4, '55']
# # # print(sorted(a, key=lambda x: int(x) if isinstance(x, str) else x))
# # #
# # # x = 10
# # # y = 'Hi'
# # # z = 'Hello'
# # # print(y)
# # # breakpoint()
# # # print(z)
# # #
# # import sqlalchemy
# # from sqlalchemy import create_engine
# # engine = create_engine('sqlite:///college.db', echo=True)
# # conn = engine.connect()
# # conn.
# # class BaseModel(Base):
# import multiprocessing
# import os
# # import sqlite3
# #
# # connection = sqlite3.connect('/home/pavel/PycharmProjects/testCRM/db.sqlite3')
#
#
# # conn = connection
# # cur = conn.cursor()
#
# # with connection as conn:
# #     cur = conn.cursor()
# #     cur.execute("""
# #     Select country, count(*) count_country, city
# #     from authenticate_address
# #     group by country;
# #     """)
# #
# #     # cur.execute("""
# #     # INSERT INTO authenticate_address
# #     # (country, city, street, house, flat, post_office)
# #     # VALUES
# #     # ('Islands', 'Lake Scott', 'New', '100','45', '2240021');
# #     # """)
# #     conn.commit()
# #     print(cur.fetchall())
# #     cur.close()
#
#
# # import io
# #
# # print(type(open('tests.py')))
# # io_ = io.open('tests.py')
# # print(type(io_))
# # class GG:
# #     pass
# # GG.mro(
# #
# # class HELload:
# #     pass
# #
# #     def __str__(self):
# #         return f'{type(self).__name__}, {type(self).__class__}' \
# #                f'{type(self)}'
# #
# #
# # def takes_context(tuple_: HELload) -> HELload:
# #     return tuple_()
# #
# #
# # print(takes_context(HELload))
#
#
# # def flat_list(lol):
# #     for item in lol:
# #         if isinstance(item, list):
# #             yield from flat_list(item)
# #         else:
# #             yield item
# #
# # a = flat_list([1, [[[[[4]]]], [4, 5]]])
# # # print(set())
# # print(next(a))
# # print(next(a))
# # def name(param: dict[str, int]) -> int:
# #     return sum(param.values())
# #
# # print(name(dict(nam=1.2, nam2=24)))
#
#
# #
# # @decor
# # def hellp():
# #     return '22'
# # print(hellp()) # in decor 22
# # print(hellp.__closure__[0].cell_contents()) # 22
# #
#
#
# # def timer(func):
# #     def wrapper(*args, **kwargs):
# #         import time
# #         start = time.time()
# #         res = func(*args, **kwargs)
# #         print(f'end {time.time() - start}')
# #         return res
# #
# #     return wrapper
#
# import multiprocessing
#
# def count(n):
#     while n > 0:
#         n -= 1
#     print(f'end {multiprocessing.current_process()}')
#
# def multiproces():
#     count_n = 100000000
#     cpy_count = multiprocessing.cpu_count() // 2
#     for i in range(cpy_count):
#         p = multiprocessing.Process(target=count, args=(count_n,))
#         p.start()
#
# # multiproces()
# if __name__ == '__main__':
#
#     # from timeit import Timer
#     # t = Timer("multiproces()", "from __main__ import multiproces")
#     # print( t.timeit())
#     multiproces()
#     # import time
#     # start = time.time()
#     # while multiprocessing.active_children():
#     #     pass
#     # else:
#     #     print(f'end {time.time() - start} {os.getpid()}')
#
