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


async def end_when_time_elapsed(mytime = 5.0):
    await asyncio.sleep(mytime)

async def main():
    pass


if __name__ == "__main__":
    with Timer() as timer:
        while(True):
            if timer.check() == "end":
                
                break
            else:
                
                continue
        