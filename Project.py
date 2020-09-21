

itemsquantity = {'sugar' : 131, 'Bread (sliced)': 311, 'Bread (unsliced)':229,
'Egg' :545, 'Three crown (tin)' :201, 'Peak milk (tin)': 230, 'Peak milk (sachet)' :791,
'Bournvita (sachet)': 611, 'Milo (tin)':367, 'Peak milk (Large Sachet)':889,
'Milo (Large Sachet)': 934, 'Bournvita (Large Sachet)': 758, 'Custard (small sachet)': 383,
'Corn flakes (small sachet)': 647, 'Golden morn (small sachet)': 121, 'Detergent (small Wawu)': 198,
'Detergent (small Aerial)': 354, 'Detergent (Big Wawu)': 323,'Detergent (Big Aerial)': 222,
'Corn flakes (big sachet)': 341, 'Golden morn (Large sachet)': 458, 'Sprite (small)':134,
'Pepsi (small)': 674, 'Fanta (small)': 757, 'Lacasera (small)':127, 'Sprite (big)': 956, 
'Pepsi (big)': 374, 'Fanta (big)': 267, 'Lacasera (big)': 786, 'Coke (big)': 546}

itemsprice = {'Sugar':'$50','Bread (sliced)': '$200','Bread (unsliced)':'$150', 'Egg': '$50','Three crown (tin)': '$150',
'Peak milk (tin)': '$120','Peak milk (sachet)': '$50','Bournvita (sachet)':'$50', 'Milo (tin)':'$500','Peak milk (Large Sachet)': '$700',
'Milo (Large Sachet)':'$700','Bournvita (Large Sachet)': '$100', 'Custard (small sachet)': '$200', 'Corn flakes (small sachet)':'$150',
'Golden morn (small sachet)':'$100', 'Detergent (small Wawu)':'$120', 'Detergent (small Aerial)':'$115', 'Detergent (Big Wawu)':'$200',
'Detergent (Big Aerial)': '$250', 'Corn flakes (big sachet)':'$750', 'Golden morn (Large sachet)':'$650', 'Sprite (small)':'$80',
'Pepsi (small)':'$80','Fanta (small)':'$80', 'Lacasera (small)':'$80', 'Sprite (big)':'$150', 'Pepsi (big)':'$150', 'Fanta (big)':'$150',
'Lacasera (big)':'$150', 'Coke (big)':'$150'}

price = itemsprice
quantity = itemsquantity


#inbuilt functions to change the price of any items
#for a,b in itemsprice.items():
    #itemsprice.update({'Egg':'$70'})
    
#inbuilt functions to add new items with their prices
#for a,b in itemsprice.items():
    #itemsprice.update({'woda':'$70'})
    
#inbuilt functions to add more items with their prices
#for a,b in itemsquantityquantity:
    #itemsquantity.update({'pancake':50})




print("Welcome to Mr Adamu's retail market")
b = range(0,3)
print ("1. Items\n2. Available quantity\n3. Exit")
navigate = 'press the respective number to start shopping:'
launching = int(input(navigate))
for p,q in enumerate(itemsprice.items()):
    if launching == 1:
        print(p,q)
for p,q in enumerate(itemsquantity.items()):
    if launching == 2:
        print (p,q)
Back = int(input("press 1 to return: "))
for p,q in enumerate(itemsprice.items()):
    if Back == 1:
        print (p,q)
#else:
    #break

mylist1 =[]
mylist2 = []
mylist3 = []
i = 0
total = 0
collation = 'Select items:'
counting = ('select quantity:')
while i < 2:
    purchased =str(input(collation))
    quantity= int(input(counting))
    i += 1
    for p,q in itemsprice.items():
        if purchased == p:
            mylist3.append(quantity)
            for o in range(0,quantity):
                mylist1.append(p)
                mylist2.append(q)
            else:
                continue
        else:
            pass

#for p,q in itemsquantity.values():
    #updated_quantity = p - counting
#print(itemsquantity)

for k in mylist2:
    total += k
    if len(mylist1) < 5:
        discount = 0.2 * total
        Total_price = (total + discount)
    elif len(mylist1) > 10:
        discount = 0.3* total
        Total_price = (total + discount)
    elif len(mylist1) >10 and total> 800:
        discount = 0.3 * total
        Total_price = (total + disocunt + 800)
    else:
        Total_price = total

totalq = 0
for e in mylist3:
    totalq += e
    Total_quantity = totalq

#Total gain = Total payment - Costprice

print('The list of prices is %s' %(mylist2)) 
print ("The total items selected are %s " %(mylist1))
print('The total payment is $%.2f' %(Total_price))


receipt = ("RECEIPT OF PAYMENT:", "Items purchased: %s" %(mylist1),"Total quantities: %i" %(Total_quantity),
           "Correspondong prices: %s" %(mylist2), "Total payment: $%.2f" %(Total_price))
for count, item in enumerate(receipt):
	print(count, item)
