# Plate-Numbers-Detection
Plate Numbers Detection using OpenCV with a little tweak to make picture a little bit easier to query and detect numbers/letters from picture.

First of, setup your environment to number using 
```bash
conda activate number
```
Next, run the file number_plate.py using python3
```bash
python3 number_plate.py
```
Show a picture contains the number license plate to the camera, the ROI could retrived the 'data' which is a box contains the number plate.

Next, use EasyOCR to detect and get the number data from that cropped image of the license plate

Install easyocr if you have not
```bash
!pip install easyocr
```
Import every needed library
```bash
import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
```
Upload the image, `path/img`
```bash
Image("/content/scaned_img_2.jpg")
```
You can change indicate specific language for easyocr via `reader = easyocr.Reader(['en']`

Print out the output
```bash
output = reader.readtext('/content/scaned_img_2.jpg')
output
```
You can look at the `ReadPlatesLicenseUsingEasyOCR.ipynb` file for example and execution.
