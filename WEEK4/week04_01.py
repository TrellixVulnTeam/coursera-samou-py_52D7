import os.path
import tempfile

class File:
    def __init__(self, path_to):
        self.path_to = path_to

        if not os.path.exists(self.path_to):
            open(self.path_to, 'w').close()

        self.f = open(path_to, 'r+')
        self.curr = 0
    
    def read(self):
        with open(self.path_to, 'r') as f:
            return f.read()

    def write(self,line):
        with open(self.path_to, 'w') as f:
            return f.write(line)

    def __str__(self):
        return str(self.path_to)

    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.path_to, 'r') as f:
            f.seek(self.curr)
            line = f.readline()

            if line:
                self.curr = f.tell()
                return line
            else:
                self.curr = 0
                raise StopIteration

    def __add__(self, other):
        tmp_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        with open(tmp_path, 'w') as f:
            for line in self.f:
                f.write(line)
            for line in other.f:
                f.write(line)
        return File(tmp_path)

