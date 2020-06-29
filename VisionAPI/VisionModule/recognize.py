# Import required libraries and modules
import cv2 as cv
import numpy as np
from VisionModule import OCR as ocr  # Optical Character Recognition Module
from VisionModule import ROIGeneration as roi  # Region of Interest Generation
from VisionModule import ContourGenerator as cg  # Contour Generation
from VisionModule import removeNoise as rn  # Text processing 1
from VisionModule import replace #  Text processing 2


def recognize(image):
    '''
    This function take an argument as image(numpy array).
    
    This is core of whole process. It find contour of main image and
    generate Region of Interest from image (required bounding boxes)
    and apply ocr detection on it.

    Detected values are return as dictionary (JSON Format).
    '''

    (x, y, w, h) = cg.getContour(image) # Generate Contour and return it's X & Y points.
    img1 = image[y:y+h,x:x+w]
    imglist = roi.getROI(img1)  # Generate Images from contoured image.
    
    # Two dictionary for final store.
    data = dict()
    data2 = dict()
    
    # Procedure of following code,
    # 1. Taken each ROI,
    # 2. Detect characters for that ROI,
    # 3. Process text which are recognized
    # 4. Append in dictionary

    img = imglist[0]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = replace.replaceText(text)
    data['hco_name1'] = data2['hco_name2'] = text
    #print(text)

    img = imglist[1]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = replace.replaceText(text)
    data['provider_name1'] = text
    data2['pr_name2'] = text
    #print(text)

    img = imglist[2]
    img = rn.removeBox(img)
    text = ocr.Document_Text_Recognize(img)
    text = replace.replaceNum(text)
    text = text.ljust(10, '0')
    data['pr_npi1'] = data2['pr_npi2'] = text
    #print(text)

    img = imglist[3]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text = text.replace(';', '')
    data['pr_address1'] = text
    #print(text)

    img = imglist[4]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text = text.replace(';', '')
    data['pr_city1'] = text
    #print(text)

    img = imglist[5]
    text = ocr.Text_Recognize(img)
    text = replace.replaceNum(text)
    data['pr_phone1'] = text
    #print(text)

    img = imglist[6]
    text = ocr.Document_Text_Recognize(img)
    text = replace.replaceNum(text)
    data['pr_fax1'] = data2['pt_fax2'] = text
    #print(text)

    img = imglist[7]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text1 = text
    text = text.replace('\'', ' ')
    text = text.replace('\"', ' ')
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    if (text == ''):
        data['icd_code1'] = 'default'
        data['icd_other1'] = ''
        data2['icd_code2'] = "Z12.11 & Z12.12"
    else:
        data['icd_code1'] = 'other'
        data['icd_other1'] = data2['icd_code2'] = text1
    #print(text)

    img = imglist[8]
    text = ocr.Document_Text_Recognize(img)
    text = replace.handleDate(text)
    data['order_date1'] = text

    img = imglist[9]
    text = ocr.Text_Recognize(img)
    text = replace.replaceNum(text)
    data['pt_id1'] = text
    #print(text)

    img = imglist[10]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = replace.replaceText(text)
    data['pt_fname1'] = text
    #print(text)

    img = imglist[11]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = replace.replaceText(text)
    data['pt_lname1'] = text
    data2['pt_name2'] = data['pt_fname1'] + ' ' + data['pt_lname1']
    #print(text)

    img = imglist[12]
    text = ocr.Text_Recognize(img)
    text = replace.handleDate(text)
    data['pt_dob1'] = data2['pt_dob2'] = text
    #print(text)

    img = imglist[13]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'sex')
    data['pt_sex1'] = data2['pt_sex2'] = text
    #print(text)

    img = imglist[14]
    text = ocr.Document_Text_Recognize(img)
    text = replace.replaceNum(text)
    data['pt_phone1'] = data2['pt_phone2'] = text
    #print(text)
    
    img = imglist[15]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'phone')
    data['pt_phonetype1'] = text
    #print(text)

    img = imglist[16]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(' ', '')
    text = replace.replaceText(text)
    data['pt_lang1'] = text
    #print(text)

    img = imglist[17]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text = text.replace(';', '')
    data['pt_saddress1'] = text
    #print(text)

    img = imglist[18]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text = text.replace(';', '')
    data['pt_scity1'] = text
    data2['pt_saddress2'] = data['pt_saddress1'] + ', ' + data['pt_scity1']
    #print(text)

    img = imglist[19]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text1 = text
    text = text.replace('\'', ' ')
    text = text.replace('\"', ' ')
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    text = text.replace('-', ' ')
    if text.isspace():
        data['pt_baddress1'] = data['pt_saddress1']
        data['pt_bcity1'] = data['pt_scity1']
    else:
        data['pt_baddress1'] = text1
        #print(text1)

        img = imglist[20]
        text = ocr.Document_Text_Recognize(img)
        text = text.replace('\n', ' ')
        text = text.replace(':', '')
        text = text.replace(';', '')
        data['pt_bcity1'] = text
        #print(text)

    img = imglist[21]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'latino')
    data['pt_latino1'] = text
    #print(text)

    img = imglist[22]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'race')
    data['pt_race1'] = [text]
    #print(text)

    img = imglist[23]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'bill')
    data['pt_bill1'] = text
    #print(text)

    img = imglist[24]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = replace.replaceText(text)
    data['poly_name1'] = data2['poly_name2'] = text
    #print(text)

    img = imglist[25]
    text = ocr.Text_Recognize(img)
    text = replace.handleDate(text)
    data['poly_dob1'] = data2['poly_dob2'] = text
    #print(text)

    img = imglist[26]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'relation')
    data['pt_relation1'] = text
    #print(text)

    img = imglist[27]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = replace.replaceText(text)
    data['insurance_carrier1'] = data2['insurance_carrier2'] = text
    #print(text)

    img = imglist[28]
    text = ocr.Text_Recognize(img)
    text = replace.handleRadio(text, 'insurance')
    data['insurance_type1'] = data2['insurance_type2'] = text
    #print(text)

    img = imglist[29]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = text.replace(':', '')
    text = text.replace(';', '')
    data['claim_address1'] = text
    #print(text)

    img = imglist[30]
    text = ocr.Text_Recognize(img)
    text = replace.replaceNum(text)
    data['sub_id1'] = data2['sub_id2'] = text
    #print(text)

    img = imglist[31]
    text = ocr.Document_Text_Recognize(img)
    text = replace.replaceNum(text)
    data['group_number1'] = data2['group_number2'] = text
    #print(text)

    img = imglist[32]
    text = ocr.Document_Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = replace.replaceText(text)
    data['plan1'] = text
    #print(text)

    img = imglist[33]
    text = ocr.Text_Recognize(img)
    text = replace.replaceNum(text)
    data['auth_code1'] = text
    data2['hcp_sign2'] = "Yes"
    #print(text)

    img = imglist[34]
    text = ocr.Text_Recognize(img)
    text = replace.handleDate(text)
    data['final_date1'] = text
    #print(text)

    # End of Code
    
    #----------------------------------------------------------
    # TO check ,how each ROI is generate, uncomment this section.
    # This portion is optional.

    #count = 1
    #for img in imglist:	
    #	text = ocr.Text_Recognize(img)
    #	cv.imwrite('result/img'+str(count)+'.jpg' , img)
    #	file = open('result/text'+str(count)+'.txt' , 'a')
    #	file.write(text)
    #	file.close()
    #	count += 1
    
    #----------------------------------------------------------

    final = {'form1': data , 'form2': data2}    # Final Dictionary(JSON Format)

    return final

def SecondRecognize(image):
    '''
    This function take an argument as image(numpy array).
    
    This is core of whole process. It find contour of main image and
    generate Region of Interest from image (required bounding boxes)
    and apply ocr detection on it.

    Detected values are return as dictionary (JSON Format).
    '''

    (x, y, w, h) = cg.getContour(image) # Generate Contour and return it's X & Y points.
    img1 = image[y:y+h,x:x+w]
    imglist = roi.getSecondROI(img1)  # Generate Images from contoured image.
    
    # One dictionary for final store.
    data = dict()
    
    # Procedure of following code,
    # 1. Taken each ROI,
    # 2. Detect characters for that ROI,
    # 3. Process text which are recognized
    # 4. Append in dictionary

    img = imglist[0]
    text = ocr.Text_Recognize(img)
    text = text.replace('\n', ' ')
    text = replace.replaceNum(text)
    data['colo_number2'] = text
    #print(text)

    img = imglist[1]
    text = ocr.Text_Recognize(img)
    text = replace.handleDate(text)
    data['es_date2'] = text
    #print(text)

    final = {'form2' : data}

    return final