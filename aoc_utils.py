def read_file_of_strings(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for  line in f]