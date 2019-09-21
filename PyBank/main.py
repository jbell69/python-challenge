# install modules
import csv
import os

#declare variables
total_months = 0
net_amount = 0
previous_revenue = 0
monthly_change = 0
m_change_list = []
total_change = []
months = []

# Set path for file
csvpath = os.path.join("..", "Data", "budget_data.csv")

with open(csvpath, newline='') as bank_csv_file:

    bank_csvreader = csv.reader(bank_csv_file, delimiter=',')
    bank_header = next(bank_csvreader)
    
    for row in bank_csvreader:

        # defining data groups
        months.append(row[0])
        revenue = int(row[1])

        # total number of months
        total_months = total_months + 1

        # sum all profit/losses
        net_amount = net_amount + revenue

        # change in revenue
        if total_months > 1:
            monthly_change = revenue - previous_revenue
            m_change_list.append(monthly_change)

        previous_revenue = revenue

    # calculation for output
    total_change = sum(m_change_list)
    average_change = total_change / (total_months - 1)
    great_inc_profit = max(m_change_list)
    great_dec_profit = min(m_change_list)
    max_month_index = m_change_list.index(great_inc_profit)
    min_month_index = m_change_list.index(great_dec_profit)
    max_month = months[max_month_index]
    min_month = months[min_month_index]

    # print out results
    print ("Financial Analysis")
    print ("------------------------------")
    print (f"Total Months:  {str(total_months)}")
    print (f"Total: ${str(net_amount)}")
    print (f"Average Change: ${str(round(average_change,2))}")
    print (f"Greatest Increase in Profits: {str(max_month)} ${str(great_inc_profit)}")
    print (f"Greatest Decrease in Profits: {str(min_month)} ${str(great_dec_profit)}")


# exporting results to txt file
PyBank_export = open("PyBank.txt", "w")

PyBank_export.write ("Financial Analysis\n")
PyBank_export.write ("------------------------------\n")
PyBank_export.write (f"Total Months:  {str(total_months)}\n")
PyBank_export.write (f"Total: ${str(net_amount)}\n")
PyBank_export.write (f"Average Change: ${str(round(average_change,2))}\n")
PyBank_export.write (f"Greatest Increase in Profits: {str(max_month)} ${str(great_inc_profit)}\n")
PyBank_export.write (f"Greatest Decrease in Profits: {str(min_month)} ${str(great_dec_profit)}\n")

PyBank_export.close()

