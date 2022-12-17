#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = float(input(" How much was total bill in $ "))
people = int(input(" Split between how many people? ")
)
tip = int(input(" Input tip percentage? 10,12 or 15? "))
tip_as_percent = tip /100
tip_amt = bill * tip_as_percent
total_bill = tip_amt + bill
per_person = total_bill / people
final = round(per_person,2)
final ="{:.2f}".format(per_person)
print(f" each person pays: ${final}")
