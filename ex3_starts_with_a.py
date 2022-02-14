# Write a function statts_with_A(word) that prints true if the given word starts to "A", or false if it does not.

def starts_with_a(word):
    word.upper()
    if word[0] == "A":
        return True
    else:
        return False
if starts_with_a("Aardvark"):
    print("The word starts with an A")
else:
    print("The word does not start with an A")