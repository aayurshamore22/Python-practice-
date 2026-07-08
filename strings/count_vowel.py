def  vowels(text):
      count = 0 
      for i in text.lower():
          if i in "aeiou":
               count += 1
      print("vowels:", count)
                 
text = input("Enter text: ")
vowels(text)                 
