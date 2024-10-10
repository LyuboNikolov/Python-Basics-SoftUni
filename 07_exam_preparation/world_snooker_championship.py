tournament_stage = input()
ticket_type = input()
tickets_count = int(input())
photo_with_trophy = input()
price = 0

if ticket_type == "Standard":
    if tournament_stage == "Quarter final":
        price = 55.50
    elif tournament_stage == "Semi final":
        price = 75.88
    elif tournament_stage == "Final":
        price = 110.10
elif ticket_type == "Premium":
    if tournament_stage == "Quarter final":
        price = 105.20
    elif tournament_stage == "Semi final":
        price = 125.22
    elif tournament_stage == "Final":
        price = 160.66
elif ticket_type == "VIP":
    if tournament_stage == "Quarter final":
        price = 118.90
    elif tournament_stage == "Semi final":
        price = 300.40
    elif tournament_stage == "Final":
        price = 400

total_sales = tickets_count * price

if total_sales > 4000:
    total_sales *= 0.75
else:
    if total_sales > 2500:
        total_sales *= 0.9

    if photo_with_trophy == "Y":
        total_sales += tickets_count * 40

print(f"{total_sales:.2f}")
