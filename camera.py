from time import time


class Camera (object):
    def __init__(self):
        self.frames = [ open(f +  '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frames(self):
        return self.frames[int(time()) %3]
