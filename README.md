# Making-OCR-from-a-object-detection-model
Making OCR from a object detection model    
![Screenshot from 2020-09-28 18-29-27](https://user-images.githubusercontent.com/39157936/94435316-9b892a00-01b8-11eb-8f28-c6c10b1a253e.png)


To download the weights of the custom trained yolo model please install gdown using pip3 install gdown and use the below command  
```
gdown  https://drive.google.com/uc?id=1vlhdj5AWVwmHNTbqgzKAlfRKVCq14TGC
```
Whereas 1vlhdj5AWVwmHNTbqgzKAlfRKVCq14TGC is the file id. Once these are downloaded make a directory called as backup and place it inside that.  

## What is achieved in this repository  
**Task**: Task is to detect regions in the image where there is text, crop the regions using the coordinates of detected text and then write the text from the image to the text file  
**Dataset**: Custom 50 images of text is taken from google. If anyone wishes to see images please use the [link](https://drive.google.com/drive/folders/1rh9mnJ4qc4VIqR2qLvz0P1SHfwjsse-v?usp=sharing). These images are augmented and transformed into 100 images.  
**Model**: To detect the text regions in the image yolov4 model is used and training is implemented using darknet library.       
           To extract the text from the image, tessaract library is used.   
**Parameters**: During training total loss was confidence loss, bounding boxes loss and label loss. Average loss less than 0.7 is achieved for 2000 iterations and using max_batch =2000 and steps=1800  


           



