def age_assignment(*args,**kwargs):
    result = ""
    names = [*args]
    ages = kwargs
    people_info = {}
    for name in range(len(names)):
        current_name = names[name]
        first_letter = current_name[0]
        for person_letter,person_age in ages.items():
            if first_letter == person_letter:
                if current_name not in people_info:
                    people_info[current_name] = person_age
    for person,age in sorted(people_info.items()):
        result += f"{person} is {age} years old.\n"
    return result

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))