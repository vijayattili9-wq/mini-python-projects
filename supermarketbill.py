name = input("Enter yor Name: ")

# list of items
lists='''
Rice      Rs 10/kg
Sugar     Rs 8/kg
Oil       Rs 30/liter
salt      Rs 25/kg
Paneer    Rs 40/kg
Maggie    Rs 12/pack
Boost     Rs 200/bottle
'''
# declaration 
price =0
pricelist =[]
totalprice = 0
finalamount= 0
ilist = []
qlist = []
plist = []

# rate for each item
items = {'rice':10,'sugar':8,'oil':30,'salt':25,'paneer':40,'maggie':12,'boost':200}

while True:
    option = input("press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                 print("Thak you for shopping")
                 break
            elif inp1 =='1':
                item = input("Choose your item: ").lower()
                while True:
                    quntity_input = input("Enter quntity: ")
                    if quntity_input.isdigit():
                        quntity = int(quntity_input)
                        break
                    print("please enter a valid quntity.")

                if item in items:
                     price = quntity * items[item]
                     pricelist.append((item, quntity,items[item],price))
                     totalprice += price
                     ilist.append(item)
                     qlist.append(quntity)
                     plist.append(price)
                else:
                     print("Selected item is not available. Sorry for the inconvension.")   

        if totalprice >0:
            tax = (totalprice *18)/100
            finalamount = tax + totalprice         

        print(25*"=","supermarket",25*"=")
        print(28*" ","Amalapuram")
        print("name:",name, 30*" ","August 20,2026")
        print(75*"-")
        print("Sno",10*" ",'item',8* " ",'quntity',8*" ",'price')
        for i in range(len(pricelist)):
            print(i,13*" ",ilist[i],8*" ",qlist[i],8*" ",plist[i])
        print(75*"-")
        print(50*" ",'total amount:','Rs',totalprice)    
        print("Tax amount",50*" ",'Rs',tax)
        print(75*"-")
        print(50*" ",'Final amount',"Rs",finalamount)
        print(75*"-")
        print(20*" ","Thank you & Visit again")
        print(75*"-")
