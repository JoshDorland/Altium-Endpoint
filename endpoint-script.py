netlist_path = 'endpoint_script.NET' #TODO: Make this an actual path somewhere
net_nums = 0 #counter for the total number circuit nets

class Net:
    def __init__(self, num, crkt, harn, col, size, twst=None, shld=None, from_conn=None, to_conn=[]):
        self.num = num
        self.crkt = crkt
        self.harn = harn
        self.col = col
        self.size = size
        self.twst = twst
        self.shld = shld
        self.from_conn = from_conn
        self.to_conn = to_conn
    
    def aboutNet(self):
        about_net = [self.num, self.crkt, self.harn, self.col, self.size, self.twst, self.shld, self.from_conn, self.to_conn]
        return about_net
    
    def connectNets(self, to_conn):
        self.to_conn.append(to_conn)

net_1 = Net(1, "GND-01", "RH", "RD", 0.35, from_conn="X013")
print(net_1.aboutNet())

net_1.connectNets("X022")
print(net_1.aboutNet())
    
# for i in range(0, 7):
#     print(net_count[i])


# print(net_count)

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


