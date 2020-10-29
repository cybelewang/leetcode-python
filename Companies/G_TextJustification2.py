"""
Read string from large file and yield string ending with whitespace and size <= chunk_size
Example: "my really big files that spans a lot of lines that may contain long words like congratulations", chunk_size = 20 will result:
my really big files 
that spans a lot of 
lines that may 
contain long words 
like 
congratulations
"""
def read_in_chunks(file_object, chunk_size = 30):
    pre_data = ''
    while True:
        read_in = ''
        if len(pre_data) < chunk_size:
            read_in = file_object.read(chunk_size)

        data = pre_data + read_in
        if not data:
            break

        # check if reaches end of file
        if len(data) < chunk_size:
            yield data
            break

        # data size >= chunk_size
        # search for last whitespace index
        i, last_whitespace = 0, -1
        while i < chunk_size:
            if data[i] == ' ':
                last_whitespace = i
            i += 1

        if last_whitespace > -1:
            # has whitespaces - return as many words as possible
            i = last_whitespace + 1
            pre_data = data[i:]
            yield data[:i]
        else:
            # not have whitespaces - raise error
            raise Exception("{0} exceeds chunk size limit {1}".format(data, chunk_size))

with open('really_big_file.dat') as f:
    for piece in read_in_chunks(f, 20):
        print(piece)
