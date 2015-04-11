# Everything in this file requires OpenCV to work.
# Don't try running it unless you have the OpenCV Python module hooked up.
import cv2
import cv2.cv as cv

# This function takes in a string (a file path to a video).
# This function outputs a list of every (frame_inc)th frame of said video.
def grab_frames(video):
    # Pack the video file into an OpenCV data structure.
    vidcap = cv2.VideoCapture(video)

    # Some values that define the behavior of the main loop.
    frame_tot = vidcap.get(cv.CV_CAP_PROP_FRAME_COUNT) # Total number of frames.
    frame_pos = 0 # Sets the frame position to the first frame.
    frame_inc = 100 # Sets the frequency with which a frame is recorded.
    images = [] # Contains the list to return.

    # The main loop.
    while frame_pos < frame_tot:
        # Set the frame position.
        vidcap.set(cv.CV_CAP_PROP_POS_FRAMES, frame_pos)
        # Push the frame at that position to the list.
        images.append(vidcap.read()[1])
        # Move forward to the next frame we want.
        frame_pos += frame_inc

    # This whole process takes ~2 minutes for a ~4 minute video.
    return images

