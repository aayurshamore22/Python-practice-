def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

word = input("Enter a word: ")
palindrome(word)
