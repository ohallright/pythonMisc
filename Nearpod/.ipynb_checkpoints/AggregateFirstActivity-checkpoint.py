import glob
import pandas as pd

# get user dir
userDir = '\\'+input('User in C: directory:')
directory = r'C:\Users'+userDir+'\Downloads'

# get user write file name
userFile = '\\'+input('File Name (in downloads):')
writeLoc = r'C:\Users'+userDir+'\Downloads'+userFile+'.xlsx'

## begin
print('    Begin Processing')

# create base df
aggregateData = pd.DataFrame(columns=['Name','Date','OEQ'])

for i in glob.glob(directory+'/session*'):
    print(i)
    
    file = i
    # read zipped csv
    df = pd.read_csv(file, encoding='latin1')

    # get column name for class opening activity
    val = 0
    for col in df.columns: 
        if val == 6: # get seventh column, class starting activity 
            activityCol = col
        val = val +1    

    # convert import into 
    base = df[ ['Name','Date',activityCol] ]
    baseNames = base.rename(columns={activityCol: "OEQ"})
    baseNames.drop_duplicates()

    # if there's a value then 1, else 0
    baseNames['Participation'] = 0 # student entered nothing
    baseNames.loc[baseNames['OEQ'].notnull(), 'Participation'] = 1 # student entered something
    baseNames.loc[baseNames['OEQ'] == '-', 'Participation'] = 0 # student "entered" nothing, default is '-'
    classRecords = baseNames.drop(columns=['OEQ'])

    
    # append class records with aggregate df
    aggregateData = aggregateData.append(classRecords, ignore_index=True)    
    
# create rowId
aggregateData = aggregateData.drop(columns=['OEQ'])
aggregateData = aggregateData.reset_index()
aggregateData = aggregateData.rename(columns={'index': 'rowId'})

# write file
aggregateData.to_excel(writeLoc, index=False)

# finish, print success 
print('')
print('Complete, written to ',writeLoc)
input()