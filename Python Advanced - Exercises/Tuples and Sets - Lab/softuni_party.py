count_guests = int(input())

reservation = {input() for _ in range(count_guests)}
guests_who_came = input()

while guests_who_came != "END":
    reservation.remove(guests_who_came)
    guests_who_came = input()

print(len(reservation))
print("\n".join(sorted(reservation)))

# count_guests = int(input())
# regular_guests = set()
# vip_guests = set()
# guests_that_came = set()
# for _ in range(count_guests):
#     guest_code = input()
#     if guest_code.startswith(tuple('0123456789')):
#         vip_guests.add(guest_code)
#     else:
#         regular_guests.add(guest_code)
# command = input()
# while command != "END":
#     guests_that_came.add(command)
#     command = input()
# sorted(vip_guests)
# sorted(guests_that_came)
# print(len(vip_guests - guests_that_came) + len((regular_guests - guests_that_came)))
# print("\n".join(vip_guests - guests_that_came))
# print("\n".join(regular_guests - guests_that_came))