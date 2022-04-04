## Python-Challenge
## Background
In this project, we have two Python challenges, PyBank and PyPoll. Both of these challenges present a real-world situation where the Python scripting skills can be used. 
## PyBank
In this challenge, a Python script was created to analyze the financial records of budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". The first step is to import csv file and read the file and use "next()" function to skip the header row in the Python script, and then to analyze the records to calculate each of the following:
### The total number of months included in the dataset
The first column is "Date" including "date and month", and the total number of months is to count each "Date" and sum the count. The "for" loop was used to read the row[0] which refers to the column "date", and the "len()" function was used to sum the total rows which equals the total months.
### The net total amount of "Profit/Losses" over the entire period
The new empty list "pro_loss=[]" was created, and the "append" method was used to assign the roww[1] which refers to the column "Profit/Losses" to the new list "pro_loss". Then the net total amount of "Profit/Losses" over the entire period is the sum of the new list "pro_loss".
### The changes in "Profit/Losses" over the entire period, and the average of those changes
In the column"Profit/Losses", the differences between the current numbers and the previous numbers are the changes over the entire period. The new empty list "change=[]" was created to get the values of changes. The avarage of changes is the sum of the new list "change" divided by the length ( the total row number) of this list.
### The greatest increase and the greatest decrease in profits (date and amount) over the entire period
The greatest increase is to find the maximum value of the list of "change", and the greatest decrease is to find the minimum value of the list of "change". Go back to the last step which the list "change" was created, the new list "newmonth" was created to get the values of current dates. The "for" loop and "if" condition were used to find the maximum and minimum values and their corresponding dates.
### Below are the analysis results:
[analysisresult_pybank.txt](https://github.com/Yuanphone/python-challenge/files/8411518/analysisresult_pybank.txt)
## PyPoll
In this challenge, a set of poll data called election_data.csv. Our task is to  help a small, rural town modernize its vote counting process.The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The first step is to import csv file and read the file and use "next()" function to skip the header row in the Python script, and then to analyze the records to calculate each of the following:
### The total number of votes cast
The first column is "ID", and the total number of votes cast is to count each "ID" and sum the count. The for "loop" was used to read the row[0] which refers to the column "ID", and the "len()" function was used to sum the total rows which equals the total votes cast.
### A complete list of candidates who received votes and The total number of votes each candidate won
The new list "candi_name" was created to get the values of row[2]. In order to get the unique names of candidates, the "sorted()" function was used to ascend the names amd then another "for" loop and "if" condition were used to get the unique name for each candidate. At the same time, the new list "count_vote" was created to get the vote counts for each candidate.
### The percentage of votes each candidate won
The new list "percentage" was created to get the percentage of the votes counts for each candidate.  A "for" loop should be used and the function is percent_count=round(count_vote[i]/Totalnumber*100,3).
### The winner of the election based on popular vote
The "zip()" was used to combine the two lists "unique_name" and "percentage". A "for" loop and "if" condition were used to find the maximun percentage and find the winner name at the same time.
### Print
Finanlly, to get the print results for lists, a "for" loop is necessary to be used for "print". "f-strings" is a very useful string formmatted method for printing lists.
### Below are the analysis results
[analysis_results_PyPoll.txt](https://github.com/Yuanphone/python-challenge/files/8411526/analysis_results_PyPoll.txt)

These Python scripts are compiled and written for the homework of Data Analytics Bootcamp class at Georgia Institute of Technology. The dataset generated by Trilogy Education Services, LLC. @2020 Trilogy Education Services, a 2U, Inc, brand. All Rights Reserved.





