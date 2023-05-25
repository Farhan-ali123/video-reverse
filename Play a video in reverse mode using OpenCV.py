import cv2

# videoCapture method of cv2 return video object

# Pass absolute address of video file
# cap = cv2.VideoCapture("C:\\Users\\user\\Desktop\\newp\\venv\\resources\\cricket.mp4")
#
# # read method of video object will return
# # a tuple with 1st element denotes whether
# # the frame was read successfully or not,
# # 2nd element is the actual frame.
#
# # Grab the current frame.
# check, vid = cap.read()
#
# # counter variable for
# # counting frames
# counter = 0
#
# # Initialize the value
# # of check variable
# check = True
#
# frame_list = []
#
# # If reached the end of the video
# # then we got False value of check.
#
# # keep looping until we
# # got False value of check.
# while (check == True):
#     # imwrite method of cv2 saves the
#     # image to the specified format.
#     cv2.imwrite("frame%d.jpg" % counter, vid)
#     check, vid = cap.read()
#
#     # Add each frame in the list by
#     # using append method of the List
#     frame_list.append(vid)
#
#     # increment the counter by 1
#     counter += 1
#
# # last value in the frame_list is None
# # because when video reaches to the end
# # then false value store in check variable
# # and None value is store in vide variable.
#
# # removing the last value from the
# # frame_list by using pop method of List
# frame_list.pop()
#
# # looping in the List of frames.
# for frame in frame_list:
#
#     # show the frame.
#     cv2.imshow("Frame", frame)
#
#     # waitkey method to stopping the frame
#     # for some time. q key is presses,
#     # stop the loop
#     if cv2.waitKey(25) and 0xFF == ord("q"):
#         break
#
# # release method of video
# # object clean the input video
# cap.release()
#
# # close any open windows
# cv2.destroyAllWindows()
#
# # reverse the order of the element
# # present in the list by using
# # reverse method of the List.
# frame_list.reverse()
#
# for frame in frame_list:
#     cv2.imshow("Frame", frame)
#     if cv2.waitKey(25) and 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()





















import cv2

# Load the video
video_path = 'C:\\Users\\user\\Desktop\\newp\\venv\\resources\\cricket.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Create VideoWriter object to save the reversed video
output_path = 'reversed_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Iterate over the frames in reverse order and write them to the output video
for frame_idx in range(total_frames-1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        # Reverse the frame horizontally
        reversed_frame = cv2.flip(frame, 1)
        out.write(reversed_frame)
    else:
        break

# Release the resources
cap.release()
out.release()

print("Video reversed successfully.")