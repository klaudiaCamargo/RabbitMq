import asyncio

#------------- EXEMPLO COM 'YIELD FROM' E 'AWAIT' -----------

async def print_async_01():
    print('ASYNC 01')

    await asyncio.sleep(0.1)
    print('print depois da yield no ASYNC 01')



async def print_async_02():
    print('ASYNC 02')

    await asyncio.sleep(0.1)
    print('print depois da yield no ASYNC 02')


loop = asyncio.get_event_loop()



tasks = [loop.create_task(print_async_01()),
         loop.create_task(print_async_02())]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)

loop.close()


