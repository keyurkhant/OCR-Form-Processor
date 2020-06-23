import cv2
import pdf2image
import numpy as np

def getROI(pdf):
    #images = pdf2image.convert_from_path(pdf)
    
    #i = 0
    #for img in images:
        #img = np.array(img)
        #print(img.shape)
        #cv2.imshow('temp', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        #cv2.imwrite('form-'+ str(i) + '.jpg', img)
        #i += 1
        
    img = cv2.imread('form-0.jpg', 0)
    print(img.shape)
    
        
getROI('FilledForm.pdf')
