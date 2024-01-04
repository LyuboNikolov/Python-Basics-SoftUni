deposited_sum = float(input())
deposit_duration_months = int(input())
annual_interest_rate = float(input())

interest = deposited_sum * (((annual_interest_rate / 100) / 12) * deposit_duration_months)
total_sum = deposited_sum + interest

print(total_sum)
