import cv2
from PIL import Image
def search(first, second):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(first)
    large_image = cv2.imread(second)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    # cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    im = Image.open(second)
    im1 = im.crop((MPx, MPy, MPx+ tcols, MPy+trows))
    print((MPx, MPy), (MPx + tcols, MPy + trows))
    # Display the original image with the rectangle around the match.
    # cv2.imshow('output',large_image)
    im1.show()
    im1.save('im1.png')
    # The image is only displayed if we call this
    cv2.waitKey(0)
search('out.png', 'vau.png')

#ну находить квадрат научились
#теперь два вида тестов: с обрезанием и обычный. хотя, стоит поразмыслить. + все это подключить к боту. за утро сделать.