# Exp1_5 - Write a program to calculate the electricity bill (accept number of units from user) according to the 
# following 
#        Unit                              Price  
#        First 100 units                   no charge 
#        Next 100 units                    Rs 5 per unit  
#        After 200 units                   Rs 10 per unit 


units = int(input("Enter the number of units: "))
final_bill_amt = 0


if (units<100):
    charge = 0
elif(units<=200):
    charge=5
    final_bill_amt=(units-100)*charge
else:
    charge=10
    final_bill_amt = 5*100+(units-200)*charge

print("Total charge is: ",final_bill_amt)


