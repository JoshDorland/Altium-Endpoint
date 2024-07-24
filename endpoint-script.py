netlist_path = 'endpoint_script.NET' #TODO: Make this an actual path somewhere
net_nums = 0 #counter for the total number circuit nets

class Net:
    def __init__(self, num, crkt, harn, col, size, twst=None, shld=None, from_conn=[None, None], to_conn=[None, None]):
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
    
    def connectNets(self, from_conn=[None, None], to_conn=[None, None]):
        if from_conn[0] == "*" or to_conn[0] == "*":
            raise Exception("Designator missing for" + ' ' + self.crkt)
        else:
            self.from_conn = from_conn
            self.to_conn = to_conn

net_1 = Net(1, "GND-01", "RH", "RD", 0.35)
print(net_1.aboutNet())

net_1.connectNets(["X013", 8], ["*", 4])
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


