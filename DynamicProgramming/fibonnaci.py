def fib(n):
    prev, curr = 0, 1

    if n <= 1:
        return n

    for i in range(2, n+1):
        tot = prev + curr
        prev = curr
        curr = tot

    return curr

def main():
    
    for i in range(10):
        print(fib(i))

if __name__ == "__main__":
    main()