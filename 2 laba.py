a = input("""Make your choice :
 1. The number of numbers in the text.
 2. Sort by words.                  
 """)
if a == "1":
  alph =    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
  s = input("Input your text:")
  for i in range(26):
    print(alph[i], " =",s.count(alph[i]))


elif a == "2":
    b = input("Input you text:")
    b = b.split()
    b = sorted(b)
    b = " ".join(b)
    words = set()
    res = ' '
    for word in b.split():
        if word not in words:
            res = res + word + " "
            words.add(word)


    print(res)

else:
    pass