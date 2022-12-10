
import csv
import pandas as pd
from collections import Counter
with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("+---------------------------------------------------------------------------+")
        for col in row:
            print("|  ",end="")
            print(col.center(16),end="")
            
        print("|")


    df=pd.read_csv("employees.csv")
    salary=df["Salary"]
    positionList=df["Position"].values

    positionOccurences=Counter(positionList)

    print(positionOccurences)

    # print(salary)
    print("")
    print("Total Slaary being paid is: ",salary.sum())
    

