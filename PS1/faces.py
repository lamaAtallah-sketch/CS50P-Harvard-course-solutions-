def main():
    reply = input("Input: ")
    print("Output:", convert(reply))
    

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
"""
Eng.Lama Atallah
Make a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁.
Then, in that same file, implement a main function that prompts the user for input, passes that input to convert, and prints the result.
"""
