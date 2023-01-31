import csv
sales_report=open('sales.csv', 'r')
sales=csv.reader(sales_report, delimiter= ',')
next(sales)
sales_outfile=open('salesreport.csv', 'w')
customer_ID=''
Grand_total=0
sales_outfile.write('CustID, Total\n')
for row in sales:
    if row[0] !=customer_ID:
            sales_outfile.write(customer_ID+','+str(Grand_total)+'\n')
            print(row[0])
            print(Grand_total)
            Grand_total=0
            customer_ID= row[0]
    subtotal=float(row[3])
    taxamt=float(row[4])
    freight=float(row[5])
    total=subtotal+taxamt+freight
    Grand_total += total
