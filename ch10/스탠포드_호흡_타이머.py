import time
import asyncio

class Timer:
    '''
    컨텍스트 매니저로 사용하려고 한다
    '''
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self
    
    def check(self):
        if time.time() - self.start_time > 10:
            return "end"
        else:
            return "still working"

    def __exit__(self, *args):
        



        print("Elapsed time = ", time.time() - self.start_time)

'''
block 함수, 코루틴이 아닌 함수를 비동기로 실행시키고 싶을때
'''

def blocked_func(thread_num, mytime = 5.0):
    start_time = time.time()
    while(True):
        if time.time() - start_time > mytime:
            print(thread_num, "번 쓰레드 종료")
            break

async def end_when_time_elapsed(mytime = 5.0):
    await asyncio.sleep(mytime)



async def main():
    #tasks = asyncio.create_task(end_when_time_elapsed())

    '''tasks = [asyncio.create_task(end_when_time_elapsed(mytime)) for mytime in [10.0, 150.0]]
    await asyncio.gather(*tasks)'''

    loop = asyncio.get_running_loop()
    tasks = [loop.run_in_executor(None, blocked_func, num+1, time) for num, time in enumerate([10.0, 20.0])]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    with Timer() as timer:
        asyncio.run(main())