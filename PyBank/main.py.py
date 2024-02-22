import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

line_count = 0
total_profit_loss = 0 
previous_profit_loss = 0
changes =[]
months = []


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header 
    next(csvreader, None)

    for row in csvreader: 
        # Count the months (lines)
        line_count += 1
        # Count total profit/loss
        total_profit_loss += int(row[1])

        current_profit_loss = int(row[1])

        current_month = row[0] 

        # Calculate the change in profit/loss
        if line_count > 1:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            months.append(current_month)

        total_profit_loss += current_profit_loss
        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = round(sum(changes) / len(changes),2) if len(changes) > 0 else 0

# Find the index of the greatest increase in profits
greatest_increase_index = changes.index(max(changes))

# Retrieve the corresponding month and the greatest increase in profits
greatest_increase_month = months[greatest_increase_index]
greatest_increase_profit = max(changes)

# Find the index of the greatest  Decrease in profits
greatest_decrease_index = changes.index(min(changes))

# Retrieve the corresponding month and the greatest  Decrease in profits
greatest_decrease_month = months[greatest_decrease_index]
greatest_decrease_profit = min(changes)



print('Financial Analysis')
print("---------------------------")
print("Number of Months:", line_count)
print("Total:", "$", total_profit_loss)
print("Average Change:", "$", average_change)
print("Greatest Increase in Profits:", greatest_increase_month, "($", greatest_increase_profit, ")")
print("Greatest Decrease in Profits:", greatest_decrease_month, "($", greatest_decrease_profit, ")")

# Set variable for output file
output_file = os.path.join("Analysis", "financial_analysis_final.csv")

with open(output_file, 'w') as file:
    file.write('Financial Analysis\n')
    file.write("---------------------------\n")
    file.write(f"Number of Months: {line_count}\n")
    file.write(f"Total: $ {total_profit_loss}\n")
    file.write(f"Average Change: $ {average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} ($ {greatest_increase_profit})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} ($ {greatest_decrease_profit})\n")

print(f"Results exported to {output_file}")
