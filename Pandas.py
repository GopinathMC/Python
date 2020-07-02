import pandas as pd
file ='..'
df = pd.read_csv(file)
print(df)

df.columns.tolist()#list all columns
df1 = df.drop(columns=['zcmodeid','zcustprdstatus'])

mask = df['prdid'] == 100001442#filtering
print(df[mask])
mask = (df['prdid'].isin([100001442,100127884])) & (df['soldtoid']==1500000473)
print(df.loc[2,['prdid','custid']])#brings 3rd row prdid&custid

new = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
                    'Cost':[10000, 5000, 15000, 2000]}
df4=pd.DataFrame(data=new)

df4['percent'] = df4.apply(lambda x : (x['Cost']*0.1),axis=1)#new column percent
df4['T/F'] = df4['Cost'].apply(lambda x : 'Rich' if x>=10000 else 'Poor')

#applying function without using lambda
def sample_fun(x):
    if(x>=10000):
        return 'Rich'
    elif(x<5000):
        return 'Poor'
    else:
        return 'middle'
    
df4['Decide'] = df4['Cost'].apply(lambda x : sample_fun(x))
df5=df4.drop(columns=['T/F'])
print(df5)

filepath = '..'
recharge_new = pd.read_csv('..',sep='|')

def calendar_year(x,y):
    x=str(x)
    if y in ['June','July','August','September','October','November','December']:
       ans =  'FY'+x[2:4]+str((int(x[2:4])+1))
    else:
        ans = 'FY'+str((int(x[2:4])-1))+x[2:4]
    return ans

recharge_new['fy'] = recharge_new.apply(lambda x : calendar_year(x['calendar_year'],x['financial_month']),axis=1)
print(recharge_new.head(10))

df4['alphaNUM'] = df4['Cost'].apply(lambda x : str(x).isalpha())#return false if there is any numbers in column

fil = df4[df4['alphaNUM'] == True]#filter
print(fil)
if fil.empty:
    print('pass')
else:
    print('chr')
