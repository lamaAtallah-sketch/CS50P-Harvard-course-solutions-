def main():
    num=int(input("Type the number u wanna check its parity: "))
    if is_even(num):
        print("even!")
    else:
        print("odd!")
        
def is_even(n):
    return n%2==0
main()
