import cv2
import cv2.cv as cv
from metamind.api import ClassificationData, ClassificationModel, set_api_key, general_image_classifier

set_api_key("uqXM0XTScBW2y46BI5BSiWpRXLYjEsyEatyYw60zyEpH76KyRf")
classifier = general_image_classifier

jpgs = []    #List of inputs to the classifier, to be populated by video grabs
results = {} #Mapping from input (url? jpg?) to [probability, label]
labels = {}  #Mapping from label to [[inputs][probabilities]]

#Get base64 encoding, which allows an image to work as a URL
def toBase64 (jpg):
    with open(jpg, "rb") as f:
        data = f.read()
        data_string = data.encode("base64")
        return data_string
	# THIS NEEDS TO BE CLOSED AND ONLY OPEN ONCE

def frame_requests():
    count = 0
    for input in jpgs:
        print "Frame: %d" % count
        count += 1
        base64 = toBase64(input)
        output = classifier.predict(['data:image/jpeg;base64,' + base64], input_type='urls')
        probability = output[0].get(u'probability')
        label = output[0].get(u'label')
        results[input] = [probability, label]
        if labels.has_key(label):
            labels[label][0].append(input)
            labels[label][1].append(probability)
        else:
            labels[label] = [[input],[probability]]
        print 'Results[',input,']: ', results[input]
        print 'Labels[',label,']: ', labels[label]

# This function takes in two strings: a file path to a video,
# and a relative path to a directory which it populates with frames.
def grab_frames(video, dest):
    # Pack the video file into an OpenCV data structure.
    vidcap = cv2.VideoCapture(video)

    # Some values that define the behavior of the main loop.
    frame_tot = vidcap.get(cv.CV_CAP_PROP_FRAME_COUNT) # Total number of frames.
    frame_pos = 0 # Sets the frame position to the first frame.
    frame_inc = 100 # Sets the frequency with which a frame is recorded.

    # The main loop.  Takes ~2 minutes for a ~4 minute video.
    while frame_pos < frame_tot:
        # Set the frame position.
        vidcap.set(cv.CV_CAP_PROP_POS_FRAMES, frame_pos)
        # Write the frame to the directory, and push its filename to jpgs.
        cv2.imwrite("%sframe%d.jpg" % (dest, frame_pos / frame_inc), vidcap.read()[1])
        jpgs.append("%sframe%d.jpg" % (dest, frame_pos / frame_inc))
        # Move forward to the next frame we want.
        frame_pos += frame_inc

grab_frames("../resources/test_video.mp4", "../resources/test_video/")
frame_requests()

