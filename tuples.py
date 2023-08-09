contacts =[('Jason','555-0123'), ('carl', '555-0987')]

for (name, phone) in contacts :
    print("{}'s phone number is {}.".format(name,phone))


    airports = [("'O'HARE international Airport", "ORD"),
                 ("Los Angeles International Airport", "LAX"),
                   ("Dallas/Fort Worth International Airport", "DFW"),
                   ("Denver International Airport", "DEN")
                ]
    
for (airport, airport_code) in airports:

    print("The code for {} is {} ." .format(airport,airport_code))