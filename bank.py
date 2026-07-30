def main():
    greet=input("Greet us dear user:)\n").lower().strip()
    greeting(greet)
    
def greeting(ans):
    if ans.startswith("hello"):
        print("$0")
    elif ans.startswith("h"):
        print("$20")
    else:
        print("$100")
    
main()
"""
Eng.Lama Atallah
PS1
In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with "hello", output $0. 
If the greeting starts with an "h" (but not "hello"), output $20. 
Otherwise, output $100. 
Ignore any whitespace around the user's input and make the greeting case-insensitive.
"""
