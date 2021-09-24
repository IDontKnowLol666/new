import args
import cv2
# defining prototxt and caffemodel paths
detector_model = args.detector_model
detector_weights = args.detector_weights

# load model
detector = cv2.dnn.readNetFromCaffe(detector_model, detector_weights)
capture = cv2.VideoCapture(0)

while True:
    # capture frame-by-frame
    success, frame = capture.read()

    #...

    # get frame's height and width
    height, width = frame.shape[:2]  # 640×480

    # resize and subtract BGR mean values, since Caffe uses BGR images for input
    blob = cv2.dnn.blobFromImage(
        frame, scalefactor=1.0, size=(300, 300), mean=(104.0, 177.0, 123.0),
    )
    # passing blob through the network to detect a face
    detector.setInput(blob)
    # detector output format:
    # [image_id, class, confidence, left, bottom, right, top]
    face_detections = detector.forward()
