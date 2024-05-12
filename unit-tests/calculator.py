def main():
    x = int(input("What's your number? \n"))
    print(f"{x} square is {square(x)}")
    
def square(x: int) -> int:
    return x * x

if __name__ == "__main__":
    main()