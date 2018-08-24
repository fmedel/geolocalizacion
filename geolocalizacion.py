
# coding: utf-8

# In[1]:


import requests


# In[2]:


import pandas as pd


# In[3]:


import time 


# In[4]:


f = open('algo.csv','r')
geo = pd.read_csv(f)


# In[5]:


def obtener_coordenadas2(direccion):
    time.sleep(1)
    params = {
        'address': direccion,
        'region:': 'chile',
        'sensor': 'false'
    }
    
    req = requests.get('http://maps.googleapis.com/maps/api/geocode/json', params=params)
    res = req.json()
    result = res['results'][0]

    
    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']
    geodata['address'] = result['formatted_address']
    
    return {
        'latitud': geodata['lat'],
        'longitud':  geodata['lng'],
        'direccion': geodata['address'] 
    }
    


# In[6]:


geo['completo']=geo['Direcciones']+","+geo['comuna']+","+geo['pais']


# In[7]:


stack_a=[]
for x in geo['completo']:
    stack_a.append(obtener_coordenadas2(x))
    

    


# In[8]:


stack_la=[]
stack_lo=[]
for x in stack_a:
    stack_la.append(x['latitud'])
    stack_lo.append(x['longitud'])


# In[9]:


geo['lat']=stack_la
geo['log']=stack_lo


# In[10]:


geo.drop('completo', axis=1, inplace=True)


# In[11]:


geo.to_csv('final.csv', encoding='utf-8', index=False)

