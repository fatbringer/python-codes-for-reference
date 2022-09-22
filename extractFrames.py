import cv2

inputfilename = 'video.MP4'
vidcap = cv2.VideoCapture(inputfilename)
count = 0
success = True
#fps = int(vidcap.get(cv2.CAP_PROP_FPS))
fps = 30 #assume videos are 30 fps
timeInterval = 5 # time between each screenshot, in seconds

while success:
    success,image = vidcap.read()
    #print('read a new frame:',success)
    if count%(100) == 0 : #you can replace the frame interval manually too
        outputFrameName = inputfilename + "frame" + str(count) + ".jpg"
        print("writing", outputFrameName)
        cv2.imwrite(outputFrameName, image)
    count+=1


# When everything done, release the capture
vidcap.release()
cv2.destroyAllWindows()
print("completed")
