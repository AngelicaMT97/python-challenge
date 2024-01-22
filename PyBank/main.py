import csv

def financial_analysis(csv_path, output_path):
    # Initialize variables
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    profit_loss_changes = []
    dates = []

    # Read CSV file
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip header
        header = next(csv_reader)

        # Loop through rows
        for row in csv_reader:
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total months and total profit/losses
            total_months += 1
            total_profit_losses += profit_loss

            # Calculate profit/loss changes
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                profit_loss_changes.append(change)
                dates.append(date)

            # Update previous profit/loss
            previous_profit_loss = profit_loss

    # Calculate average change
    average_change = round(sum(profit_loss_changes) / (total_months - 1), 2)

    # Find greatest increase and decrease
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    # Find corresponding dates
    increase_date = dates[profit_loss_changes.index(greatest_increase)]
    decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

    # Print financial analysis results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

    # Write financial analysis results to a text file
    with open(output_path, 'w') as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("----------------------------\n")
        output_file.write(f"Total Months: {total_months}\n")
        output_file.write(f"Total: ${total_profit_losses}\n")
        output_file.write(f"Average Change: ${average_change}\n")
        output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

financial_analysis(r'C:\Users\angel\OneDrive\Documentos\Bootcamp\Challenges\Challenge 3\python-challenge\PyBank\Resources\budget_data.csv', r'C:\Users\angel\OneDrive\Documentos\Bootcamp\Challenges\Challenge 3\python-challenge\PyBank\Analysis\Analysis.txt')