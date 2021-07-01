import pandas as pd 
import datetime
import csv 
current_date_and_time = datetime.date.today()
current_date_and_time_string = str(current_date_and_time)
extension = ".csv"
file_name =  current_date_and_time_string + extension
df = pd.read_csv('FinalAttendance_syntax.csv')
df.drop(df.index[0:], inplace = True)
df.to_csv(file_name, index = False)
my_csv = pd.read_csv("Dataforattendance.csv")
column_Name = my_csv.Name
column_Time= my_csv.timeinseconds
column_Id=my_csv.Id
N=len(column_Name)
i=0
print("the total number of enteries present in the DataforAttendance file is ",N)
while i<N:
    j=1
    while j<N:
        if(column_Name[i]==column_Name[j])and(column_Id[i]==column_Id[j]):
            if(column_Time[i]<column_Time[j]):
                entry_time=(column_Time[i])
                exit_time=(column_Time[j])
            else:
                entry_time=(column_Time[i])
                exit_time=(column_Time[j])
            total_time=exit_time - entry_time  
            if(total_time >= 2400):
                with open(file_name,'r+') as f:
                    myDatalist = f.readlines()
                    namelist=[]
                    for line in myDatalist:
                        entry=line.split(',')
                        namelist.append(entry[0])
                    if column_Name[i] not in myDatalist:
                        current_date = datetime.date.today()
                        f.writelines(f'\n{column_Id[i]},{column_Name[i]},{current_date},{"Present"}') 
            elif(total_time==0):
                j=j+1
                continue            
            elif(total_time<2400):
                with open(file_name,'r+') as f:
                    myDatalist = f.readlines()
                    namelist=[]
                    for line in myDatalist:
                        entry=line.split(',')
                        namelist.append(entry[0])
                    if column_Name[i] not in myDatalist:
                        current_date = datetime.date.today()
                        f.writelines(f'\n{column_Id[i]},{column_Name[i]},{current_date},{"Absent"}')                 
        j=j+2
    i=i+1
print("[INFO:THE ATTENDANCE FILE HAS BEEN UPDATED FOR TODAY]")
print("[Erasing the Datforattendance file")
print(".....")
print(".....")
df = pd.read_csv('Dataforattendance.csv')
df.drop(df.index[0:], inplace = True)
df.to_csv('Dataforattendance.csv', index = False)
print("[Erased the data]")