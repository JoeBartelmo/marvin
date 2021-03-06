import cv2
import marvin


class CameraCapture(object):
    def __init__(self,cam_id=0,fourcc="MJPG"):
        self.cap = cv2.VideoCapture(cam_id)
        self._fourcc = fourcc
        self._fourcc_val = cv2.VideoWriter_fourcc(*self._fourcc)
        self.__setProp(cv2.CAP_PROP_FOURCC,self._fourcc_val)


    def read(self):
        status = False
        if self.cap.isOpened():
            status,frame = self.cap.read()
        if not status:
            frame = self.__debugFrame()

        return frame

    def __setProp(self,flag,value):
        return self.cap.set(flag,value)

    def __getProp(self,flag):
        return self.cap.get()

    def __debugFrame(self):
        h,w = self.height,self.width
        if isinstance(h,type(None)) or isinstance(w,type(None)):
            h,w = 256,256

        frame = np.zeros( (h,w), dtype=np.uint8 )
        centroid = marvin.centroid(frame)
        frame = cv2.putText(frame,
                            "error opening or reading image",
                            centroid,
                            cv2.FONT_HERSHEY_SIMPLEX,
                            12,
                            (255,255))
        return frame

    #width
    @property
    def width(self):
        return self.__getProp(cv2.CAP_PROP_FRAME_WIDTH)
    @width.setter
    def width(self,value):
        self.__setProp(cv2.CAP_PROP_FRAME_WIDTH,value)

    #height
    @property
    def height(self):
        return self.__getProp(cv2.CAP_PROP_FRAME_HEIGHT)
    @height.setter
    def height(self,value):
        self.__setProp(cv2.CAP_PROP_FRAME_HEIGHT,value)

    #fps
    @property
    def fps(self):
        return self.__getProp(cv2.CAP_PROP_FPS)
    @fps.setter
    def fps(self,value):
        self.__setProp(cv2.CAP_PROP_FPS,value)

    #brightness
    @property
    def brightness(self):
        return self.__getProp(cv2.CAP_PROP_BRIGHTNESS)
    @brightness.setter
    def brightness(self,value):
        self.__setProp(cv2.CAP_PROP_BRIGHTNESS,value)

    #contrast
    @property
    def contrast(self):
        return self.__getProp(cv2.CAP_PROP_CONTRAST)
    @contrast.setter
    def contrast(self,value):
        self.__setProp(cv2.CAP_PROP_CONTRAST,value)

    #hue
    @property
    def hue(self):
        return self.__getProp(cv2.CAP_PROP_HUE)
    @hue.setter
    def hue(self,value):
        self.__setProp(cv2.CAP_PROP_HUE,value)

    #gain
    @property
    def gain(self):
        return self.__getProp(cv2.CAP_PROP_GAIN)
    @gain.setter
    def gain(self,value):
        self.__setProp(cv2.CAP_PROP_GAIN,value)

    #exposure
    @property
    def brightness(self):
        return self.__getProp(cv2.CAP_PROP_EXPOSURE)
    @brightness.setter
    def brightness(self,value):
        self.__setProp(cv2.CAP_PROP_EXPOSURE,value)

    #writer_dims
    @property
    def writer_dims(self):
        return self.width,self.height

    #fourcc
    @property
    def fourcc(self):
        return self._fourcc
    @fourcc.setter
    def fourcc(self,value):
        self._fourcc = value
        self._fourcc_val = cv2.VideoWriter_fourcc(*self._fourcc)
        self.__setProp(cv2.CAP_PROP_FOURCC,self._fourcc_val)
