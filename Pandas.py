import pandas as pd


#df = pd.read_csv('C:\\Users\\bootbyt\\Desktop\\pokemon_data.csv')
#print(df.head(5))
#print(df.tail(5))

#df_elsx = pd.read_excel('C:\\Users\\bootbyt\\Desktop\\pokemon_data.xlsx')
#print(df_elsx.head(3))

#df = pd.read_csv('C:\\Users\\bootbyt\\Desktop\\pokemon_data.txt', delimiter='\t')
#print(df.head(3))


#df = pd.read_csv('C:\\Users\\bootbyt\\Desktop\\pokemon_data.csv')
#print(df.columns)                           #: show column
#print(df['Name'].tail(8))                  : show last 8 position in colummn"Name'
#print(df[['Name', "HP",'Attack']])
#print(df[['Name', "HP",'Attack']].head(5))
#print(df.iloc[2])                          :show curent row
#print(df.iloc[2,4])                        :show current cell
#for index, row in df.iterrows():
#    print(index, row["Name"])              :show all data in one row
#print(df.loc[df['Type 1'] == "Fire"])      :serch in current column for word (Fire)
#print(df.describe())
#print(df.sort_values('Name'))              :order by
#print(df.sort_values('Name', ascending=False)) :oreder by desc
#print(df.sort_values(['Type 1','Speed'], ascending=[1,1]).head(10))   :order by 2 kolumns ( 1 is True, 0 is False)
#print(df[['Name','Attack','Speed','HP']].sort_values(['Attack','Speed'], ascending=[0,0]).head(10))
#df['Total'] = (df['HP'] + df['Attack'] + df['Speed'])* 10
#print(df[['Name','Attack','Speed','HP','Total']].sort_values(['Total','Attack','Speed'], ascending=[1,0,0]).head(10))
#print(df.drop(columns=['Type 1']))         :dont show column
#df['Total']=df.iloc[:,4:10].sum(axis=1)    #:sum column 4-10 in total
#cols = list(df.columns)
#df = df[cols[0:2] + [cols[-1]] + cols[2:12]] #: curent position column in sheet

#df.to_csv('new_pokemon_data.csv', index=False)          #: save new file
#df.to_csv('new_pokemon_data.txt', index=False, sep='\t')
#df = pd.read_csv('cat.csv')
#print(df)

#print(df.loc[(df['Type 1'] == "Fire") & (df['Type 2'] == 'Flying')])        #:PANDAS and = &, or = |
#f_f = (df.loc[(df['Type 1'] == "Fire") & (df['Type 2'] == 'Flying') & (df['HP'] <= 100)])
#f_f.to_csv('f_f1.csv', index=False)
#f_f.reset_index(drop=True, inplace=True)        #: reset index
#print(df.loc[(df['Name'].str.contains('Mega'))])       # 'Mega' in Name
#print(df.loc[(~df['Name'].str.contains('Mega'))])       # 'Mega' IS NOT in Name

import re           # Regular expression operations
        #filt for word
#print(df.loc[df['Type 1'].str.contains('fire|Grass', flags=re.I, regex=True)])   #flags=re.I  == ignore g G
#print(df.loc[df['Name'].str.contains('^li[a-z]*', flags=re.I, regex=True)])
#print(df.loc[df['Name'].str.contains('[a-z]*ne$', flags=re.I, regex=True)])


#df.loc[df['Type 1'] == 'Grass', 'Legendary'] = True    # if [type 1]  == x   to [typy2] == y

#df = pd.read_csv('new_pokemon_data.csv', sep='\t')
#df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['The','Best']  # if ['position'] = x,  ['position2'] = y

#print(df.groupby(['Type 1']).mean().sort_values('Speed', ascending=False))    # group by and sorting

#df = df.groupby(['Type 1']).sum()

#df['count'] = 1    ###
#df = df.groupby(['Type 1']).count()['count']  ##  count
#df = df.groupby(['Type 1', 'Type 2']).count()['count']

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('new_pokemon_data.csv', sep='\t', chunksize=7):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat(new_df, results)
    print(new_df)