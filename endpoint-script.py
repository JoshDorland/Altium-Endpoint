netlist_path = 'endpoint_script.NET' #TODO: Make this an actual path somewhere
net_nums = 0 #counter for the total number circuit nets

class Net:
    def __init__(self, num, ckt, harn, col, size, twist, shld):
        self.num = num
        self.ckt = ckt
        self.harn = harn
        self.col = col
        self.size = size
        self.twist = twist
        self.shld = shld
    
 
net_count = ['[', '0', '0', '0', '2', '0', ']']


for i in range(0, 7):
    print(net_count[i])


print(net_count)

# try:
#     netlist_object = open(netlist_path, 'r')
#     line = netlist_object.readline()

#     while line != '':
#         line_list = list(line)
#         print(line_list, end='\n')

#         if line_list[0] == '[':
#             print("true")
#             break 
    
#         line = netlist_object.readline()
        


# finally:
#     netlist_object.close()


