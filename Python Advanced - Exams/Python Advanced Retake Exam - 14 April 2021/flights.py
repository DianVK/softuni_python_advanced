def flights(*args):
    destinations = {}

    for item in range(0, len(args) - 1, 2):
        destination_name = args[item]
        if destination_name == "Finish":
            break
        count_people = int(args[item + 1])
        if destination_name not in destinations:
            destinations[destination_name] = 0
        destinations[destination_name] += count_people

    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
