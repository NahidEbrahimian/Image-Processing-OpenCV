# 04noisey_OCR_characters

Crop all characters in noisy image:

1. Median filter
3. **dilation** and **findContours** to extract lines
4. **findContours** in each line to extract charecters 
5. Compare each character with other characters in line to extract **_"i"_** and **_double quotation_** characters correctly

![noisey_OCR](https://github.com/n-ebrahimian/object-detection-using-contour_finder/blob/main/04noisey_OCR_characters/Inputs/noisey_OCR.jpg)

#

![noisey_OCR](https://github.com/n-ebrahimian/object-detection-using-contour_finder/blob/main/noisey_OCR_characters/noisey_OCR.jpg)
