import os
import random

class Thanos:
    def __init__(self, path):
        self.path = path


    def snap_fingers(self):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                files.append(os.path.join(r, file))

        random.shuffle(files)

        for i in range(int(len(files)/2)):
            os.remove(files[i])
