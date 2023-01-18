from collections import deque

vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

rose = []
tulip = []
lotus = []
daffodil = []

flower_found = False

while not flower_found and consonants and vowels:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    if current_vowel in "rose" and current_vowel not in rose:
        rose.append(current_vowel)
        if len(rose) == 4:
            print("Word found: rose")
            flower_found = True
            if flower_found:
                break

    if current_consonant in "rose" and current_consonant not in rose:
        rose.append(current_consonant)
        if len(rose) == 4:
            print("Word found: rose")
            flower_found = True
            if flower_found:
                break

    if current_vowel in "tulip" and current_vowel not in tulip:
        tulip.append(current_vowel)
        if len(tulip) == 5:
            print("Word found: tulip")
            flower_found = True
            if flower_found:
                break

    if current_consonant in "tulip" and current_consonant not in tulip:
        tulip.append(current_consonant)
        if len(tulip) == 5:
            print("Word found: tulip")
            flower_found = True
            if flower_found:
                break

    if current_vowel in "lotus" and current_vowel not in lotus:
        lotus.append(current_vowel)
        if len(lotus) == 5:
            print("Word found: lotus")
            flower_found = True
            if flower_found:
                break

    if current_consonant in "lotus" and current_consonant not in lotus:
        lotus.append(current_consonant)
        if len(lotus) == 5:
            print("Word found: lotus")
            flower_found = True
            if flower_found:
                break

    if current_vowel in "daffodil" and current_vowel not in daffodil:
        daffodil.append(current_vowel)
        if len(daffodil) == 5:
            print("Word found: daffodil")
            flower_found = True
            if flower_found:
                break

    if current_consonant in "daffodil" and current_consonant not in daffodil:
        daffodil.append(current_consonant)
        if len(daffodil) == 5:
            print("Word found: daffodil")
            flower_found = True
            if flower_found:
                break

if not flower_found:
    print("Cannot find any word!")
if vowels:
    print("Vowels left: ", end="")
    print(*vowels, sep=" ")
if consonants:
    print("Consonants left: ", end="")
    print(*consonants, sep=" ")
