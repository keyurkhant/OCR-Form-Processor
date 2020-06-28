import numpy as np
from datetime import datetime
import re

str = '१4०8२3५४ऽ4'

def replaceStr(str):
    str = str.replace('\n', '')
    str = str.replace(' ', '')
    
    str = str.replace('\\', '1')
    str = str.replace('/', '1')
    str = str.replace(']', '1')
    str = str.replace('[', '1')
    str = str.replace('l', '1')
    str = str.replace('i', '1')
    str = str.replace('(', '1')
    str = str.replace(')', '1')
    
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
    
    return str
    
def replaceRegEx(str):
    str = re.sub('[\\/[]li()]', '1', str)
    
    str = re.sub('[२]', '2', str)
    
    str = re.sub('[B]', '3', str)
    
    str = re.sub('[५ч]', '4', str)
    
    str = re.sub('[sSऽ]', '5', str)
    
    str = re.sub('[+Tt]', '7', str)
    
    str = re.sub('[४]', '8', str)
    
    str = re.sub('[१]', '9', str)
    
    str = re.sub('[oO०v]', '0', str)  

    return str

def replaceText(str):
    str = str.replace('2', 'Z')
    
    str = str.replace('Ч', 'Y')
    
    str = str.replace('0', 'O')
    
replaceStr(str)
#replaceRegEx(str)
    
    
    
    
    
    
    
