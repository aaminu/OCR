# Image Analyser and Text Recognition Using Azure Cognitive Service

Two simple modules leveraging on Azure Cognitive Service using Compter Vision API. 

Compatible with Python 3.6+ and above

The modules are:
1. OCR - Performs text recognition on images, files by calling on the "vision/v2.0/ocr"
2. Analyze - Performs imagee analysis and returns caption and words associated to picture


## Requirements
- Create a Free Azure Custom Vision Service Profile
- Create a Custom Vision Service in Azure
- Copy Key and Endpoint
- Update Subscription Key and End-point in your system Environment
                     


## Updating Subscription Key and End-point in your system Environment
for macOs, open your terminal and type to open .bash_profile
```properties
>>$ sublime .bash_profile
```  
Append your Keys and and endpoint to the end of the file i.e

export COGNITIVE_SERVICE_KEY=xxxxxxx5ase711xxxxxx44e345f 
export COGNITIVE_ENDPOINT=https://xxxxxxxxx.cognitiveservices.azure.com/

Please note that the above keys won't work for you as they are just samples.

Save and close the file. Type the following to confirm your changes
```properties
>>$ source .bash_profile
``` 


## Additional Libraries Required
1. request
2. Matplotlib
3. Pillow