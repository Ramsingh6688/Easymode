def five_series(n):
    a = 1
    
    while n>0:
        print(a)
        a = n** 2
        n = n-1
five_series(5)


##3

def new_series(n):
    a = 2
    while n>0:
        print(a)
        a = a+2
        n = n-1
new_series(10)


##4

def generate_square_numbers(limit):
    squares = []
    num = 2
    while num <= limit:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            squares.append(num)
        num += 1
    return squares


##8

def generate_series(n):
    series = []
    num = 0
    increment = 1
    for _ in range(n):
        series.append(num)
        num += increment
        increment += 2
    return series

def main():
    n = 10
    series = generate_series(n)
    print("Sample Output:", " ".join(map(str, series)))

if __name__ == "__main__":
    main()