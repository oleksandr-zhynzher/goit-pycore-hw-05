def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]
    
    return fibonacci



fibonacci = caching_fibonacci()

print(f"fibonacci(5) = {fibonacci(5)}")    
print(f"fibonacci(10) = {fibonacci(10)}")  
print(f"fibonacci(15) = {fibonacci(15)}")  
print(f"fibonacci(20) = {fibonacci(20)}")  
