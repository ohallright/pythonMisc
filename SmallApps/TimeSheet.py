import pandas as pd
from datetime import datetime, timedelta
#requires xlrd
#requires openpyxl


fileLocation = r'M:\Ryan L\Private\timesheets\TimesheetImport_.xlsx'
emplNumber = str('00337092') #Ryan L
principalCode = str('61') #Jonathan G

df = pd.read_excel(fileLocation,converters={'Empnbr':str,'ClientSuffix':str,'TypeOfWork':str,'PrincipalCode':str,'BillingRateCode':str})

col = df["Date"]
max_value = col.max()
nextDateTS = max_value + timedelta(days=1)
typeOfWork = '00'

if nextDateTS.weekday() >= 5: #if weekend then go to Monday
    nextDateTS = nextDateTS + timedelta(days=2)

print(nextDateTS)
nextDateTSDisplay = nextDateTS.strftime("%m/%d/%Y") #convert date to string    
print("Entering timesheet for: "+nextDateTSDisplay)

## inputs
nextDateTS_input = input("   Or is it a different date? (mm/dd/yyyy): ")
clientCode = input("Enter ClientCode (0009MSC01): ")
# 0009HOL01-01 #holiday
# 0009HOL01-02 floating holiday  # change client suffix to 02
# 0009MKT01 #marketing, article work
# 0009MSC04 #volunteer time
# 0009PTO01 PTO
# 0106SUM01 March 19, start Jan 18

hoursTS = input("Enter Hours (7.5): ") 

if nextDateTS_input:
    nextDateTS =  datetime.strptime(nextDateTS_input, '%m/%d/%Y')
if not clientCode:
    clientCode = '0009MSC01'
if not hoursTS:
    hoursTS = 7.5
if clientCode == '0106SUM01':
    typeOfWork = '08'    
    
data = {'Empnbr':  emplNumber,
        'Date': nextDateTS, #variable
        'ClientCode': clientCode, #variable
        'ClientSuffix': '01', 
        'TypeOfWork': typeOfWork, 
        'PrincipalCode': principalCode, 
        'BillingRateCode': '00', 
        'Hours': hoursTS, #variable
        'Note': '', 
        'Units': 0, 
        'IgnoreYN': 'N', 
       }


newData = df.append(data, ignore_index=True)
newData.to_excel(fileLocation, sheet_name ='TIMEDATA',index=False)

# print entered data
nextDateTSDisplay = nextDateTS.strftime("%m/%d/%Y") #convert date to string    
print('Completed: ',nextDateTSDisplay,clientCode,str(hoursTS)+'hrs')
input()
