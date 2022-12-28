def even_odd_filter(**kwargs):
    for key,value in kwargs.items():
        if key == "even":
            kwargs['even'] = (list(filter(lambda x: x % 2 ==0,value)))
        elif key == "odd":
            kwargs['odd'] = (list(filter(lambda x: x % 2 != 0,value)))
    return kwargs

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))