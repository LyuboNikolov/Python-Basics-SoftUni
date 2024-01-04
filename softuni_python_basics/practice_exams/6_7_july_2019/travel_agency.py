# city_name = input()
# offer = input()
# vip_discount = input()
# days = int(input())
#
# price = 0
#
# if city_name == 'Bansko' or city_name == 'Borovets':
#     if offer == 'noEquipment':
#         if vip_discount == 'yes':
#             price = 80 * 0.95
#         else:
#             price = 80
#     elif offer == 'withEquipment':
#         if vip_discount == 'yes':
#             price = 100 * 0.9
#         else:
#             price = 100
# elif city_name == 'Varna' or city_name == 'Burgas':
#     if offer == 'noBreakfast':
#         if vip_discount == 'yes':
#             price = 100 * 0.93
#         else:
#             price = 100
#     elif offer == 'withBreakfast':
#         if vip_discount == 'yes':
#             price = 130 * 0.88
#         else:
#             price = 130
# total_price = price * days
# if days < 1:
#     print("Days must be positive number!")
# elif 1 <= days < 8:
#     if (city_name != 'Varna' and city_name != 'Burgas' \
#             and city_name != 'Borovets' and city_name != 'Bansko') \
#             or (offer != 'noEquipment' and offer != 'withEquipment' \
#             and offer != 'withBreakfast' and offer != 'noBreakfast'):
#         print('Invalid input!')
#     else:
#         print(f"The price is {total_price:.2f}lv! Have a nice time!")
# elif days >= 8:
#     if (city_name != 'Varna' and city_name != 'Burgas' \
#             and city_name != 'Borovets' and city_name != 'Bansko') \
#             or (offer != 'noEquipment' and offer != 'withEquipment' \
#             and offer != 'withBreakfast' and offer != 'noBreakfast'):
#         print('Invalid input!')
#     else:
#         total_price = (days - 1) * price
#         print(f"The price is {total_price:.2f}lv! Have a nice time!")
#
#
#
city_name = input()
offer = input()
vip_discount = input()
days = int(input())
city_is_valid = True
offer_is_valid = True

price = 0

if city_name == 'Bansko' or city_name == 'Borovets':
    if offer == 'noEquipment':
        if vip_discount == 'yes':
            price = 80 * 0.95
        else:
            price = 80
    elif offer == 'withEquipment':
        if vip_discount == 'yes':
            price = 100 * 0.9
        else:
            price = 100
    else:
        offer_is_valid = False
elif city_name == 'Varna' or city_name == 'Burgas':
    if offer == 'noBreakfast':
        if vip_discount == 'yes':
            price = 100 * 0.93
        else:
            price = 100
    elif offer == 'withBreakfast':
        if vip_discount == 'yes':
            price = 130 * 0.88
        else:
            price = 130
    else:
        offer_is_valid = False
else:
    city_is_valid = False
if days < 1:
    print("Days must be positive number!")
elif 1 <= days < 8 and city_is_valid and offer_is_valid:
    total_price = price * days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif days >= 8 and city_is_valid and offer_is_valid:
    total_price = (days - 1) * price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print('Invalid input!')
