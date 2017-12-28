import cv2
import numpy as np
import marvin



class FrameContainer(object):
    """
    UNTESTED!

    Individual Frame Container for each raw frame read off the camera, the purpose
    of this class is to store and compute frame specific about a certain frame
    such as keypoints & descriptors, frame with distorted correction, etc

    inputs::
        src (np.ndarray): the source frame, probably the raw frame off the camera
        metadata (dict): the metadata at the time of frame capture,
                        see 'CameraCapture.getAllMetadata()' or 'CameraCapture.readFrameAndMetadata()'
        ORB (cv2.ORB): ORB keypoint detect if desired, if left as None then an ORB
                    detector will be built an used internally with default parameters
                    https://docs.opencv.org/3.0-beta/modules/features2d/doc/feature_detection_and_description.html

    attributes::
        src (np.ndarray): the source frame, probably the raw frame off of camera
        id (string): the frame id, structured "cam_id:frame_number"
        metadata (dict): input metadata dictionary
        ORB (cv2.ORB): the ORB keypoint detector used to generate keypoints and descriptors of the frame
        cache (dict): dictionary containing all data that has already been computed
                    about the frame, so that cpu cycles aren't used wastefully

    properties::
        keypoints (np.ndarray): array of keypoints directly from ORB.detect(),
                computed only as needed and cached
        descriptors (np.ndarray): array of descriptors for each keypoints directly from ORB.compute()
                computed only as needed and cached, computes keypoints at the same time as a necessity
        #PLACEHOLDER
        undistorted (np.ndarray): PLACEHOLDER -- eventually will be the source frame remapped to undistort the image



    """
    def __init__(self,src,metadata,ORB=None):
        self.src = src
        self.id = metadata["id"]
        self.metadata = metadata
        if isinstance(ORB,cv2.ORB):
            self.ORB = ORB
        else:
            self.ORB = cv2.ORB_create()

        self.cache = {"src":self.src,
                      "keypoints",None,
                      "descriptors",None,
                      "undistorted":,None,
                      "frame_with_keypoints",None}

    @property
    def keypoints(self):
        if self.cache["keypoints"] == None:
            self.cache["keypoints"] = self.ORB.detect(self.src)

        return self.cache["keypoints"]

    @property
    def descriptors(self):
        if self.cache["descriptors"] == None:
            self.cache["descriptors"] = self.ORB.compute(self.src,self.keypoints)

        return self.cache["descriptors"]

    @property
    def undistorted(self):
        pass
        #PLACEHOLDER FUNCTION -- requires computing the distortion maps


    @property
    def frame_with_keypoints(self):
        if self.cache["frame_with_keypoints"] == None:
            self.cache["frame_with_keypoints"] = self.ORB.drawKeypoints(self.src, kp, None, color=(0,255,0))

        return self.cache["frame_with_keypoints"]