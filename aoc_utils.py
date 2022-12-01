def read_file_of_strings(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for  line in f]

def read_file_of_strings_into_one_string(filename):
    with open(filename,'r') as f:
        return f.read()