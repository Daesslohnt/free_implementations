from typing import List

class PoolManager:
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, traceback):
        self.pool.release(self.obj)

class Reusable:
    def test(self):
        print(f"Using object {id(self)}")

class Pool:

    def __init__(self, size=1):
        self.size = size
        self.free = []
        self.in_use = []

        for _ in range(self.size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if len(self.free) == 0:
            raise Exception("No more object free")
        r = self.free.pop(0)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable) -> None:
        self.in_use.remove(r)
        self.free.append(r)

pool = Pool(2)
# r1 = pool.acquire()
# r2 = pool.acquire()
# r1.test()
# r2.test()
# pool.release(r1)
# r3 = pool.acquire()
# r3.test()
# print("*" * 30)

with PoolManager(pool) as r:
    r.test()

with PoolManager(pool) as r:
    r.test()

with PoolManager(pool) as r:
    r.test()