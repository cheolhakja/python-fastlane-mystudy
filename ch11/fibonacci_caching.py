
cache_data = [0]*100

def caching(func):
    def execute(num):
        return func(num)

    return execute

@caching
def fibonacci(num):
    if num < 2:
        return num
    
    else:
        if not cache_data[num] == 0:
            return cache_data[num]
        else:
            tmp = fibonacci(num - 1) + fibonacci(num - 2)
            cache_data[num] = tmp
            return tmp
        
cache_data[0] = 0
cache_data[1] = 1
print(fibonacci(4))