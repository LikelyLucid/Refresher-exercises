"""
Create a program for a movie cinema. It will be used to
keep track of ticket sales throughout the day. The
program should do the following:
Keep asking for tickets until the end of the day
(maybe ask the user "Do you want to sell
another ticket? (Y/N) ")
Tickets sold are either Adult, Student, Child, or
they use a Gift Voucher.
When a ticket is sold, print the price of
the ticket to the user:
• Adult $12.50
• Student $9.00
• Child $7.00
Gift Voucher is free
When a ticket is sold, keep track of how
many are sold of each type.
At the end of the day, print out the total tickets
sold/used, how many tickets were sold of each
type, and the total value of tickets.
Advanced challenge: Allow the user to cancel
buying a ticket
"""
standard
adult_price = 12.50
student_price = 9.00
child_price = 7.00
gift_price = 0

total_adult_tickets = 0
total_student_tickets = 0
total_child_tickets = 0
total_gift_tickets = 0
total_tickets = 0
total_value = 0

def get_ticket():
    ticket = input("What type of ticket would you like to buy?\n (A)dult, (S)tudent, (C)hild, or (G)ift Voucher?\nX to cancel\n").lower()
    if ticket == "a":
        return "Adult"
    elif ticket == "s":
        return "Student"
    elif ticket == "c":
        return "Child"
    elif ticket == "g":
        return "Gift Voucher"
    elif ticket == "x":
        return "Cancelled"
    else:
        print("Invalid ticket type. Please try again.")
        get_ticket()

def get_quantity():
    quantity = input("How many tickets would you like to buy?\nX to cancel\n")
    if quantity == "x":
        return "Cancelled"
    try:
        return int(quantity)
    except ValueError:
        print("Invalid quantity. Please try again.")
        get_quantity()

def get_total(ticket, quantity):
    if ticket == "Adult":
        return adult_price * quantity
    elif ticket == "Student":
        return student_price * quantity
    elif ticket == "Child":
        return child_price * quantity
    elif ticket == "Gift Voucher":
        return gift_price * quantity
    else:
        return 0


while True:
    ticket = get_ticket()
    if ticket == "Cancelled":
        break
    quantity = get_quantity()
    if quantity == "Cancelled":
        break
    total_value += get_total(ticket, quantity)
    if ticket == "Adult":
        total_adult_tickets += quantity
    elif ticket == "Student":
        total_student_tickets += quantity
    elif ticket == "Child":
        total_child_tickets += quantity
    elif ticket == "Gift Voucher":
        total_gift_tickets += quantity
    total_tickets += quantity

print("Total tickets sold:", total_tickets)
print("Adult tickets sold:", total_adult_tickets)
print("Student tickets sold:", total_student_tickets)
print("Child tickets sold:", total_child_tickets)
print("Gift Voucher tickets sold:", total_gift_tickets)
print("Total sales:", total_value)#
