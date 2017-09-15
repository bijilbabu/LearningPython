#Name: Nijil K Babu
#PGID: 71721084

#Question 1
print ("Program to calculate the total wholesale cost for 60 copies")
print ("Following assumption are made for the Question 1:")
print ("    1. Cover price of the book:Rs. 200 & Discount provided: 25%")
print ("    2. Shipping Charge for the first copy: Rs. 40")
print ("    3. Addtional cost for the shipping each copy: Rs. 10\n")

book_cost = 200
discount = 0.25
price_book = book_cost - (book_cost * discount)

print ("The cost of the book after discount is Rs.",price_book, "\n")

total=0

n=60

if n > 1:
    total = (price_book + 10 ) * (n - 1) + price_book + 40; 
elif n == 1:
    total = price_book + 40;
        
print ("Total Wholesale cost for 60 copies is Rs.",total)
