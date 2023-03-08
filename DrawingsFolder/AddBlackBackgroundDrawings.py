import numpy as np
import os
import cv2

def resizeImage(drawing, dimensions):
    #print('h, w: ' + str(dimensions[0]) + ' ' + str(dimensions[1]))
    resizeDrawing = cv2.resize(drawing, dimensions, interpolation=cv2.INTER_LINEAR)

    if drawing.shape[0] < drawing.shape[1]:
        resizeDrawing = cv2.rotate(resizeDrawing, cv2.ROTATE_90_CLOCKWISE)

    #cv2.imshow("Resized image", resizeDrawing) # show resize image
    
    return resizeDrawing

def addBlackBackground(drawing, background):
    drawingHeigth = drawing.shape[0]
    drawingWidth = drawing.shape[1]

    backgroundHeigth = background.shape[0]
    backgroundWidth = background.shape[1]

    # compute xoff and yoff for placement of upper left corner of resized image   
    yoff = round((backgroundHeigth-drawingHeigth)/2)
    xoff = round((backgroundWidth-drawingWidth)/2)
    
    # use numpy indexing to place the resized image in the center of background image
    result = background.copy()

    #print('h, w: ' + str(result.shape[0]) + ' ' + str(result.shape[1]))

    result[yoff:yoff+drawingHeigth, xoff:xoff+drawingWidth] = drawing
    
    #cv2.imshow('CENTERED', result) # show result image

    return result

# Main code itself
background = cv2.imread("C:/Users/alvaro.lopez/Downloads/DrawingsFolder/Background.jpeg",cv2.IMREAD_UNCHANGED)
inputPath = 'C:/Users/alvaro.lopez/Downloads/DrawingsFolder/Input/'
outputPath = 'C:/Users/alvaro.lopez/Downloads/DrawingsFolder/Output/'
inputImagesURL = os.listdir(inputPath)
maxSize = 680

os.chdir(outputPath)

for i in inputImagesURL:
    drawing = cv2.imread(inputPath + i, cv2.IMREAD_UNCHANGED)
    
    print('h, w: ' + str(drawing.shape[0]) + ' ' + str(drawing.shape[1]))

    if drawing.shape[0] > drawing.shape[1]:
        height = drawing.shape[0]
        width = drawing.shape[1]

        ratio = maxSize / width
        minSize = int(height * ratio)
    else:
        print('is entering else')
        width = drawing.shape[0]
        height = drawing.shape[1]

        ratio = maxSize / height
        minSize = int(width * ratio)

    print('maxSize, minSize: ' + str(maxSize) + ' ' + str(minSize))

    dimensions = (maxSize, minSize)
    
    resizeDrawing = resizeImage(drawing, dimensions)
    resultImage = addBlackBackground(resizeDrawing, background)
    cv2.imwrite("drawing-" + i, resultImage) # Save final drawings

cv2.waitKey(0)
cv2.destroyAllWindows()
