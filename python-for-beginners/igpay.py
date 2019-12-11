def igpay(word):
    ...:     vowel = ["a", "e", "i", "o", "u"]
    ...:     firstLetter = word[0]
    ...:     if firstLetter in vowel:
    ...:         print(word + "ay")
    ...:     else:
    ...:         newWord = word[1:]
    ...:         newWord = newWord + firstLetter + "ay"
    ...:         print(newWord)
