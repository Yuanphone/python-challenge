import os
import csv

csvpath=os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
# The total number of months included in the dataset
    month=[]
    pro_loss=[]
    for row in csvreader:
        month.append(row[0])
        pro_loss.append(int(row[1]))
    Totalmonth=len(month)
# The net total amount of "Profit/Losses" over the entire period
    Total_net=sum(pro_loss)
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
  # note:average=sum(pro_loss[i+1]-pro_loss[i])/Totalmonth /*wrong
  # note:avarage=Total_net/len(pro_loss) /*wrong
    newmonth=[]
    change=[]
    for i in range(len(pro_loss)-1):
        newchange=pro_loss[i+1]-pro_loss[i]
        change.append(newchange)
        nextmonth=month[i+1]
        newmonth.append(nextmonth)
        average=round(sum(change)/len(change),2)
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
    maxincrease=0 
    maxdecrease=0 
    monthrange=0
    monthrange2=0
    for x in range(len(change)-1):
        if change[x]>maxincrease:
            maxincrease=change[x]
            monthrange=newmonth[x]
        elif change[x]<maxdecrease:
             maxdecrease=change[x]
             monthrange2=newmonth[x]       
    print('Financial Analysis')
    print('------------------------------')
    print("Total Months:"+ str(Totalmonth))
    print(f"Total: ${Total_net}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {monthrange} (${maxincrease})")
    print(f"Greatest Decrease in Profits: {monthrange2} (${maxdecrease})")











 