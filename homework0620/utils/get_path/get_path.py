import os


class GetPath:

    def get_path(self, path):
        r=os.path.abspath(path)
        return r
