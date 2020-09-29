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
## How it was implemented  
* **Step 1:** Data collection. Google was used as a source to collect data. Only 50 images were collected and is being annotated.  
* **Step 2:** These 50 images were augmentated with automatic annotation changes. [Repo](https://github.com/asetkn/Tutorial-Image-and-Multiple-Bounding-Boxes-Augmentation-for-Deep-Learning-in-4-Steps) is taken for help to implement this step. Once this step was implemeted size of images raised to 100. Different set of operation such as scale, rotate, fliplr and guassian blur were applied. CSV file was genereated which contains the pixel values  
* **Step3:** Since we need to train the model using yolo, hence normalized the pixel values in the range 0 to 1.    
* **Step4:** YOLO training is done. Since it has one class, so 2000 iterations are sufficient and steps 1800 are  enough for the training.   
* **Step5:** After training the yolo using darknet coordinates of detected text are looped and images for the detected text are cropped  

