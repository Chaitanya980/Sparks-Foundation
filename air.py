

def airline_schedule(src,dest):
    if(src=="Nashik" and dest=="Pune"):
        print("\nNumber of flights: 4")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nFlight start time : 5am")
        print("\nFlight end time : 7amm")
    elif(src=="Nashik" and dest=="Mumbai"):
        print("\nNumber of flights: 5")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nFlight start time : 5am")
        print("\nFlight end time : 6:30am")
    elif(src=="Mumbai" and dest=="Kerela"):
        print("\nNumber of flights: 6")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nFlight start time : 3am")
        print("\nFlight end time : 7am")
    elif(src=="Mumbai" and dest=="Goa"):
        print("\nNumber of flights: 8")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nFlight start time : 4am")
        print("\nFlight end time : 9am")
    elif(src=="Pune" and dest=="Goa"):
        print("\nNumber of flights: 5")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nFlight start time : 5am")
        print("\nFlight end time : 9:30am")
    else:
        print("\nThere is no direct flight")

def cargo_schedule(src,dest):
    if(src=="Nashik" and dest=="Pune"):
        print("\nNumber of cargo: 4")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nStart time of cargo shipment: 5am")
    elif(src=="Nashik" and dest=="Mumbai"):
        print("\nNumber of cargo: 5")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nStart time of cargo shipment : 5am")
   
    elif(src=="Mumbai" and dest=="Kerela"):
        print("\nNumber of cargo: 6")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nStart time of cargo shipment: 3am")
       
    elif(src=="Mumbai" and dest=="Goa"):
        print("\nNumber of cargo: 8")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nStart time of cargo shipment : 4am")
       
    elif(src=="Pune" and dest=="Goa"):
        print("\nNumber of cargo 5")
        print("\nSource: "+src)
        print("\nDestination : "+dest)
        print("\nStart time of cargo shipment : 5am")
       
    else:
        print("\nThere is no direct flight")

def airline():
    print("*****Airline Scheduling*****")
    print("\nCities : Nashik,Pune,Mumbai,Kerela,Goa")
    src=input("\nEnter the source : ")
    dest=input("\nEnter the destination : ")
    airline_schedule(src,dest)
   
def cargo():
    print("*****Cargo Scheduling*****")
    print("\nCities : Nashik,Pune,Mumbai,Kerela,Goa")
    src=input("\nEnter the source : ")
    dest=input("\nEnter the destination : ")
    cargo_schedule(src,dest)

def main():
    print ("Welcome to Expert System of Airline Scheduling")
    print("Which Schedule do you want to know ? ")
    print("\n1.Airline Scheduling\n2.Cargo Scheduling")
    ch=int(input("Enter the choice : "))
    if(ch==1):
        airline()
    elif(ch==2):
        cargo()
    else:
        print("Invalid choice")

main()
