import os
import csv
from unittest.util import _count_diff_hashable
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
#  The total number of votes cast
    number=[]
    candi_name=[]
    for row in csvreader:
        number.append(row[0])
        candi_name.append(row[2])
    Totalnumber=len(number)
#  A complete list of candidates who received votes, create unique_name for candidates
#  The total number of votes each candidate won
    newsorted=[]
    unique_name=[]
    newsorted=sorted(candi_name)
    unique_name.append(newsorted[0])
    count_vote=[]
    count=1
    for y in range(len(newsorted)-1):
        if newsorted[y+1]!=newsorted[y]:
           candidate=newsorted[y+1]
           unique_name.append(candidate)
           count_vote.append(count)
           count=1
        else:
           count=count+1
    count_vote.append(count)
#  The percentage of votes each candidate won
    maxvote=0
    percentage=[]
    for i in range(len(count_vote)):
        percent_count=round(count_vote[i]/Totalnumber*100,3)
        percentage.append(percent_count)
#   The winner of the election based on popular vote.
    zipped=list(zip(unique_name,percentage))
    for each in range(len(zipped)):
        if max(percentage)==percentage[each]:
            winner=unique_name[each]
    print('Election Results')
    print('------------------------------')
    print("Total Votes:"+ str(Totalnumber))
    print('------------------------------')
    for i in range (len(unique_name)):
         print(f'{unique_name[i]}: {percentage[i]}% ({count_vote[i]})')
    print('------------------------------')
    print(f'winner: {winner}')
    print('------------------------------')








