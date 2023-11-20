# Extracting Data From Fax Formatted Form Using OCR

## Objective: 

In the era of digitalization, most of the things are done on digital devices and platforms. But many areas where there is still manual work is used like form fillings of any individuals. There are technologies like Optical Character Recognition to convert image format into text but lack effectiveness, it doesn’t use. Here we try our best to make an effective product which used to take standard fax formatted form of patients and store it in a database for future use.

## How to run application:

1. Extract zip file or clone a given github repository into your system.

       https://github.com/keyurkhant/OCR-Auto-Form.git

2. Install virtual environment python package & create a virtual environment named VisionAPI into   OCR-Auto-Form and activate the virtual environment.

3. Install VisionAPI/requirements.txt into virtual environment using following command:

       pip install -r requirements.txt
 
4. For Windows and Mac OS, install Poppler which is given into a zip file.

   Note: There are many dependencies which can't be included into requirements.txt file or platform dependant. So install it as required. 
 
5. Run final.py flask application. 

6. URI is stored in final.py file & MongoDB Compass access:
    Username and Password are given into instruction file.

7. For Google Vision API, you can use default configuration of our cloud account. But future use install and configure API from Google Cloud Console.

   API Credential JSON File : VisionAPI/VisionModule/ServiceAccountToken.json

   This VisionAPI gives 1000 API calls free each month and charges $1.5 after for each 1000 calls. 

   Default configuration(Our Account) has $50 credit. Using it you can process around 950 forms.

   For Configuration of your own Cloud VisionAPI into the system.

   Reference: https://cloud.google.com/vision/docs/setup 
   
## Working Prototype Video
   
> Refer this Video - [Extracting Data From Fax Formatted Form Using OCR](https://www.youtube.com/watch?v=U1aXWvxhYAk)
