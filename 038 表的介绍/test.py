#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
9.4 cp模型/线程
"""
# import time,random
# from multiprocessing import Process, Queue
#
#
# def producer(q, i):
#     # time.sleep(random.random())
#     q.put('hello python, hello world %s' % i)
#
#
# def consumer(q):
#     while True:
#         flag = q.get()
#         if not flag:
#             q.put(None)
#             break
#         # print(flag)
#
# start = time.time()
# q = Queue()
# p_l = []
# for i in range(1, 100):
#     p = Process(target=producer, args=(q, i))
#     p.start()
#     p_l.append(p)
# for i in range(5):
#     Process(target=consumer, args=(q,)).start()
# for p in p_l: p.join()
# q.put(None)
# print(time.time() - start)


"""
JoinableQueue
"""
# import time, random
# from multiprocessing import Process, JoinableQueue
# from threading import Thread
#
#
# def producer(q, i):
#     # time.sleep(random.random())
#     q.put('hello python, hello world %s' % i)
#     q.join()
#
#
# def consumer(q):
#     while True:
#         flag = q.get()
#         # print(flag)
#         q.task_done()
#
# start = time.time()
# task_l = []
# q = JoinableQueue()
# for i in range(1, 100):
#     p = Thread(target=producer, args=(q, i))
#     p.start()
#     task_l.append(p)
# for i in range(5):
#     p = Thread(target=consumer, args=(q,))
#     p.daemon = True
#     p.start()
# for p in task_l: p.join()
# print(time.time() - start)



"""
9.5 锁&池
"""
"""
单例模式
"""
import time
from threading import Thread, Lock


class Singleton:
    __instance = None
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.1)
                cls.__instance = super().__new__(cls)
            return cls.__instance


def main():
    print(id(Singleton()))


for i in range(20):
    t = Thread(target=main)
    t.start()


"""
优先级队列
"""
# from queue import PriorityQueue
# q = PriorityQueue()
# q.put((1, 'ehco'))
# q.put((10, 'henry'))
# q.put((5, 'dean'))
#
# print(q.get())
# print(q.get())
# print(q.get())


"""
进程池
"""
# from concurrent.futures import ProcessPoolExecutor
#
#
# def get_page(i):
#     # print(i)
#     return i
#
#
# pp = ProcessPoolExecutor(5)
# ret = []
# for i in range(10000):
#     res = pp.submit(get_page, i)
#     ret.append(res)
# pp.shutdown()
# for i in ret:
#     print(i.result())

# from concurrent.futures import ThreadPoolExecutor
#
#
# def get_page(i):
#     return i
#
#
# pp = ThreadPoolExecutor(5)
# t = map(get_page, range(1000))
# pp.shutdown()
# for i in t:
#     print(i)

"""
回调函数
"""

"""
9.6 协程
"""
"""
gevent模块
"""
# import gevent
# from gevent import time
#
#
# def func1():
#     print(123)
#     time.sleep(0.1)
#     print(456)
#     return 'func1'
#
#
# def func2():
#     print('hello')
#     time.sleep(0.1)
#     print('henry')
#     return 'func2'
#
#
# f1 = gevent.spawn(func1)
# f2 = gevent.spawn(func2)
# gevent.joinall([f1, f2])
# print(f1.value, f2.value)


"""
gevent实现socket
"""
# import gevent
# from gevent import socket
#
#
# def chat(con):
#     while True:
#         msg = con.recv(1024).decode('utf-8')
#         print(msg)
#         con.send(msg.upper().encode('utf-8'))
#
#
# sk = socket.socket()
# sk.bind(('127.0.0.1', 9000))
# sk.listen()
#
# while True:
#     con, _ = sk.accept()
#     gevent.spawn(chat, con)


"""
asyncio模块
"""
# 启动一个任务

# import asyncio
#
#
# async def func():
#     print(123)
#     await asyncio.sleep(0.1)
#     print(456)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())

# 启动多个任务

# import asyncio
#
#
# async def func1():
#     print(123)
#     await asyncio.sleep(0.1)
#     print(456)
#
#
# async def func2():
#     print('echo')
#     await asyncio.sleep(0.1)
#     print('henry')
#
#
# loop = asyncio.get_event_loop()
# wait_obj = asyncio.wait([func1(), func2()])
# loop.run_until_complete(wait_obj)


# 获取返回值

# import asyncio
#
#
# async def func1():
#     print(123)
#     await asyncio.sleep(0.1)
#     print(456)
#     return 'func1'
#
#
# async def func2():
#     print('echo')
#     await asyncio.sleep(0.1)
#     print('henry')
#     return 'func2'
#
#
# loop = asyncio.get_event_loop()
# t1 = loop.create_task(func1())
# t2 = loop.create_task(func2())
# wait_obj = asyncio.wait([t1, t2])
# loop.run_until_complete(wait_obj)
#
# print(t1.result(), t2.result())


# 获取返回值
# import asyncio
# from random import random
#
#
# async def func(i):
#     await asyncio.sleep(random())
#     return i
#
#
# async def main():
#     task_l = []
#     for i in range(10):
#         t = asyncio.ensure_future(func(i))
#         task_l.append(t)
#     for i in asyncio.as_completed(task_l):
#         ret = await i
#         print(ret)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
