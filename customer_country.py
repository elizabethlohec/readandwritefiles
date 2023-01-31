import csv
customer_file=open('customers.csv','r')
customers=csv.reader(customer_file, delimiter= ',')
next(customers)
customer_outfile=open('customer_country.csv','w')
writer = csv.writer(customer_outfile, delimiter= ',')
for something in customers:
   customer_outfile.write(something[1]+','+something[2]+','+something[4]+'\n')
