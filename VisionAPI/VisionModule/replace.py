import numpy as np
from datetime import datetime
import re

str = '१4०8२3५४ऽ4'

def detect(tokens, input):
    for i in input:
        for token in tokens:
            if i == 'Medicare' and token.startswith('MedicareAd'):
                continue
            if token.startswith(i):
                break
            if tokens[-1] == token:
                return i


def replaceNum(str):
    if str != None:
        str = str.replace('\n', '')
        str = str.replace(' ', '')
        str = str.replace(':', '')
        str = str.replace(';', '')
        
        str = str.replace('\\', '1')
        str = str.replace('/', '1')
        str = str.replace(']', '1')
        str = str.replace('[', '1')
        str = str.replace('l', '1')
        str = str.replace('i', '1')
        str = str.replace('(', '1')
        str = str.replace(')', '1')
        str = str.replace('|', '1')
        
        str = str.replace('२', '2')
        
        str = str.replace('B', '3')
        
        str = str.replace('५', '4')
        str = str.replace('ч', '4')
        
        str = str.replace('s', '5')
        str = str.replace('S', '5')
        str = str.replace('ऽ', '5')
        
        str = str.replace('+', '7')
        str = str.replace('T', '7')
        str = str.replace('t', '7')
        
        str = str.replace('४', '8')
        
        str = str.replace('१', '9')
        str = str.replace('g', '9')
        
        str = str.replace('o', '0')
        str = str.replace('O', '0')
        str = str.replace('०', '0')
        str = str.replace('c', '0')  
    #print(str)
    #print(datetime.now() - time1)
    return str
    
def replaceRegEx(str):
    time1 = datetime.now()
    str = re.sub('[\\/[]li()]', '1', str)
    
    str = re.sub('[२]', '2', str)
    
    str = re.sub('[B]', '3', str)
    
    str = re.sub('[५ч]', '4', str)
    
    str = re.sub('[sSऽ]', '5', str)
    
    str = re.sub('[+Tt]', '7', str)
    
    str = re.sub('[४]', '8', str)
    
    str = re.sub('[१]', '9', str)
    
    str = re.sub('[oO०]', '0', str)  
    
    print(datetime.now() - time1)
    
def replaceText(str):
    if str != None:
        str = str.replace(':', '')
        str = str.replace(';', '')
        str = str.replace('-', '')
            
        str = str.replace('2', 'Z')
        
        str = str.replace('2', 'Y')
        
        str = str.replace('*', 'X')
        
        str = str.replace('0', 'O')
        str = str.replace('०', 'O')
        
        str = str.replace('3', 'B')
        
        str = str.replace('5', 's')
        str = str.replace('ऽ', 's')
    
    return str

def handleDate(str):
    if str != None:
        str.replace('\n', ' ')
        str = str.replace(':', '')
        str = str.replace(';', '')
        
        if str.endswith(' '):
            str[-1] = ''
        
        str = str.replace('-', '/')
        str = str.replace('\\', '/')
        str = str.replace('|', '/')
        str = str.replace('(', '/')
        str = str.replace(')', '/')
        str = str.replace('//', '/1')
        str = str.replace('///', '1/1')
        
        str = str.replace('२', '2')
        
        str = str.replace('B', '3')
        
        str = str.replace('५', '4')
        str = str.replace('ч', '4')
        
        str = str.replace('s', '5')
        str = str.replace('S', '5')
        str = str.replace('ऽ', '5')
        
        str = str.replace('+', '7')
        str = str.replace('T', '7')
        str = str.replace('t', '7')
        
        str = str.replace('४', '8')
        
        str = str.replace('१', '9')
        
        str = str.replace('o', '0')
        str = str.replace('O', '0')
        str = str.replace('०', '0')
        str = str.replace('c', '0')  
        if str.count('/') < 2:
            str = str.replace(' ', '/')        
        
    return str

def handleRadio(str, type):
    str = str.replace(':', '')
    str = str.replace(';', '')
    str = str.replace('\'', '')
    str = str.replace('\"', '')
    str = str.replace('.', '')
    str = str.replace(',', '')
    str = str.replace('-', '')
    str = str.replace(' ', '')
    str = str.replace('Ø', '')
    str = str.replace('0', 'O')
    str = str.replace('o', 'O')
    str = str.replace('०', 'O')
    if type == 'sex':
        if str.count('O') < 1:
            str = str.replace('c', 'O')
            str = str.replace('C', 'O')
            
        if str.find('O') < 3:
            return 'Female'
        else:
            return 'Male'
        
        return 'default'
        
    elif type == 'phone':
        tokens = str.split('O')
        if str.count('O') < 2:
            str = str.replace('c', 'O')
            str = str.replace('C', 'O')
        if 'M' in tokens and 'W' in tokens:
            return 'Home'
        elif 'M' in tokens:
            return 'Work'
        elif 'W' in tokens:
            return 'Mobile'
        
        return 'default'
          
    elif type == 'latino':
        if str.count('O') < 1:
            str = str.replace('c', 'O')
            str = str.replace('C', 'O')
            
        if str.find('O') < 2:
            return 'NO'
        else:
            return 'Yes'
        
        return 'default'
        
    elif type == 'race':
        tokens = str.split('O')
            
        output = detect(tokens, ['W', 'B', 'As', 'N', 'Am'])
        if output == 'W':
            return 'White'
        elif output == 'B':
            return 'Black or African-American'
        elif output == 'As':
            return 'Asian'
        elif output == 'N':
            return 'Native Hawaiian or other Pacific Islander'
        elif output == 'Am':
            return 'American Indian or Alaska Native'
        
        return 'White'
                    
    elif type == 'bill':
        if str.count('O') < 1:
            str = str.replace('c', 'O')
            str = str.replace('C', 'O')
            
        if str.find('O') < 2:
            return 'NO'
        else:
            return 'Yes'
        
        return 'default'
  
    elif type == 'relation':
        tokens = str.split('O')
        
        if str.count('O') < 4:
            str = str.replace('c', 'O')
            str = str.replace('C', 'O')
            
        output = detect(tokens, ['Se', 'Sp', 't'])
        if output == 'Se':
            return 'Self'
        elif output == 'Sp':
            return 'Spouse'
        elif output == 't':
            return 'Other'
        
        return 'Self'
        
    elif type == 'insurance':
        tokens = str.split('O')
            
        output = detect(tokens, ['P', 'MedicareAd', 'Medicare', 'Medica', 'T'])
        if output == 'P':
            return 'Private'
        elif output == 'Medicare':
            return 'Medicare'
        elif output == 'MedicareAd':
            return 'Medicare Advantage'
        elif output == 'Medica':
            return 'Medicaid'
        elif output == 'T':
            return 'Tricare'
        
        return 'Private'
        
    return 'default'
    
#replaceStr(str)
#replaceRegEx(str)
    
    
    
    
    
    
    
