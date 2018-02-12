import csv
import UrlGeoloc

class Write_map:
    
    def __init__(self):
        self.urlGeoloc = UrlGeoloc.UrlGeoloc()

    def check_duplicate_of_map_node(self, graph_node):
        # graph_node = self.write_graph_node()

        duplicate = {}
        for key, value in graph_node.items():
            geoloc = self.urlGeoloc.get_url_geoloc(key)
            dup_key = str(geoloc['lat'])+','+str(geoloc['lng'])
            try:
                duplicate[dup_key] = [geoloc['country'], geoloc['state'], geoloc['city']]
            except:
                duplicate[dup_key] = [geoloc['country'], geoloc['state'], geoloc['city']]
        return duplicate

    def write_map_node(self, file_name, graph_node):
        print("write map_node")
        csv_file = open(file_name+"/map/node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['node_lat', 'node_lng', 'contry', 'state', 'city'])

        duplicate = self.check_duplicate_of_map_node(graph_node)
        
        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], value[0], value[1], value[2]])

        csv_file.close()



    def check_duplicate_of_map_edge(self, graph_edge):
        # graph_edge = self.write_graph_edge()

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(splited[0]) + ',' + str(splited[1]) + ',' + str(geoloc['lat']) + ',' + str(geoloc['lng']) + ',' + str(
                geoloc2['lat']) + ',' + str(geoloc2['lng'])
            try:
                duplicate[dup_key] += value
            except:
                duplicate[dup_key] = value
        return duplicate

    def write_map_edge(self, file_name, graph_edge):
        print("write map_edge")
        csv_file = open(file_name + "/map/edge.csv", 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_ip', 'dst_ip', 'src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'count'])

        duplicate = self.check_duplicate_of_map_edge(graph_edge)

        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow(
                [splited[0], splited[1], splited[2], splited[3], splited[4], splited[5], value])

        csv_file.close()