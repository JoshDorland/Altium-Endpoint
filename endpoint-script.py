file_path = 'endpoint_script.NET'

try:
    file_object = open(file_path, 'r')

    for line in file_object:
        if (line.read(6) == '[00001]'):
            print("true")
        else:
            print("false")

        print(line, end ='')
finally:
    file_object.close()


