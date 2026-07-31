def main():
    mass = int(input("What is the value of mass? "))
    print("E=mc^2 =", formula(mass))
    
def formula(m):
    c = 300000000
    return m * pow(c, 2)

main()
"""
Eng.Lama Atallah
PS1
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer greater than or equal to 1.
"""
