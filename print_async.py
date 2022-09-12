import asyncio
import time

async def inner_func(n: int) -> int:
    await asyncio.sleep(10-n)
    print(n)
    return 0

async def print_out_async() -> None:
    await asyncio.gather(*(inner_func(i) for i in range(10)))

if __name__ == '__main__':
    t1 = time.perf_counter()
    asyncio.run(print_out_async())
    t2 = time.perf_counter()
    print('Execution Time: {}'.format(int(t2-t1)))