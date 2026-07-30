def main():
    ans = input("What is the answer to the Great Question of Life, the Universe and Everything?\n").lower().strip()
    great(ans)

def great(n):
    if n == "42" or n == "forty two" or n == "forty-two":
        print("yes!")
    else:
       print("Nahhh:(\nits forty two;)")

main()

"""
Eng.Lama Atallah 
PS1 - deep.py

In deep.py, implement a program that prompts the user for the answer to the 
Great Question of Life, the Universe and Everything, outputting Yes if the 
user inputs 42 or forty-two or forty two. Otherwise output No.
"""
