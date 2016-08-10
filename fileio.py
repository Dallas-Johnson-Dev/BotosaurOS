class filehandler:

    def readall(self, filepath):
        with open(filepath, "r") as f:
            return f.readall()

    def arrayfromfile(self, filepath):
        contentlist = []
        with open(str(filepath), "r") as f:
            contentlist = f.read().splitlines()
        return contentlist