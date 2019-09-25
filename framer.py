import cv2
import os
import sys

def framer(vidfile):
    # Opens the Video file
    cap= cv2.VideoCapture(vidfile)

    if cap.isOpened():
        print 'nqma gusto neshto'
    # Set initial timestamp to 1 sec
    # cap.set(cv2.CAP_PROP_POS_MSEC, 1000) -> above is the same
    cap.set(0, 1000)
    i=0
    while(cap.isOpened() and i<3):
        print 'capture ongoing'
        ret, frame = cap.read()
        if ret == False:
            break
        time = cap.get(0)
        print time
        cv2.imwrite(vidfile+'_'+str(i)+'.jpg',frame)
        i+=1
    cap.release()
    cv2.destroyAllWindows()

def main():
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".mp4"):
            filepath = os.path.join(os.getcwd(), sys.argv[1], filename)
            framer(filepath)

main()
