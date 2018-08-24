
# coding: utf-8

# In[1]:


import requests


# In[2]:


import pandas as pd


# In[3]:


import time 


# In[4]:


f = open('algo.csv','r')
data = pd.read_csv(f)


# In[5]:


def coordenadas(direccion):
    time.sleep(1)
    params = {
        'address': direccion,
        'region:': 'chile',
        'sensor': 'false'
    }
    
    req = requests.get('http://maps.googleapis.com/maps/api/geocode/json', params=params)
    res = req.json()
    result = res['results'][0]

    
    dirrecion = dict()
    dirrecion['lat'] = result['geometry']['location']['lat']
    dirrecion['lng'] = result['geometry']['location']['lng']
    dirrecion['address'] = result['formatted_address']
    
    return dirrecion


# In[6]:


data['completo']=data['Direcciones']+","+data['comuna']+","+data['pais']


# In[7]:


stack_a=[]
for x in data['completo']:
    stack_a.append(coordenadas(x))
    

    


# In[8]:


stack_la=[]
stack_lo=[]
for x in stack_a:
    stack_la.append(x['lat'])
    stack_lo.append(x['lng'])


# In[9]:


data['lat']=stack_la
data['log']=stack_lo


# In[10]:


data.drop('completo', axis=1, inplace=True)


# In[11]:


data.to_csv('final.csv', encoding='utf-8', index=False)


# In[12]:


#para exportar datos
f2 = open('final.csv','r')
final = pd.read_csv(f2)

