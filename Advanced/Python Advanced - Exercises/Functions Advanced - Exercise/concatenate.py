def concatenate(*args,**kwargs):
    sentence = ""
    for word in args:
        sentence += word
    for key,value in kwargs.items():
        if key in sentence:
            sentence = sentence.replace(key,value)
    return sentence


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))