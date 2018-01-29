"""
start timestamp
end timestamp
src ip
src port
dst ip
dst port
No packets
length of data(bytes)
"""

class tcpFlow:
    # def check_for_syn(self):
    def __init__(self):
        self.tcp_flow_list = {}
        self.udp_flow_list = {}

    def add_packet(self, retrieved_data):
        protocol = retrieved_data["protocol"]
        return protocol
        # if protocol == "TCP":
        #     add_tcp_flow
        # elif protocol == "UDP":

    def add_tcp_flow(self, tcp_flow_key, tcp_flow_value):
        reversed_tcp_flow_key = [tcp_flow_key[1], tcp_flow_key[0]]
        if tcp_flow_key in self.tcp_flow_list:
           print("key found")
            # self.tcp_flow_list[tcp_flow_key] = tcp_flow_value
        elif reversed_tcp_flow_key in self.tcp_flow_list:
            print("reversed key found")
            # self.tcp_flow_list[reversed_tcp_flow_key] = tcp_flow_value
        else:
            print("key not found")
            self.tcp_flow_list[tcp_flow_key] = tcp_flow_value

    def add_udp_flow(self, udp_flow_key, udp_flow_value):
        self.udp_flow_list[udp_flow_key] = udp_flow_value

