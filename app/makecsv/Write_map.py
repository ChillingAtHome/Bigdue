import csv
import os
try:
    import UrlGeoloc
except ImportError:
    from app.makecsv import UrlGeoloc

class Write_map:
    
    def __init__(self):
        self.remove_map_csv_file_list()
        self.urlGeoloc = UrlGeoloc.UrlGeoloc()

    def check_duplicate_of_map_node(self, graph_node):
        duplicate = {}
        for key, value in graph_node.items():
            geoloc = self.urlGeoloc.get_url_geoloc(key)
            if geoloc['lat'] is None:
                print("IP : "+key+" is not found address")
                continue

            dup_key = str(geoloc['lat'])+','+str(geoloc['lng'])
            try:
                duplicate[dup_key] = [geoloc['country'], geoloc['state'], geoloc['city']]
            except:
                duplicate[dup_key] = [geoloc['country'], geoloc['state'], geoloc['city']]
        return duplicate

    def write_map_node(self, graph_node, filename):
        print("write map_node")
        
        csv_file = open(
            "static/data/map/"+filename+"_node.csv",
            mode = 'w',
            encoding = 'utf-8')
        writer = csv.writer(csv_file)
        
        writer.writerow([
            'node_lat',
            'node_lng',
            'country',
            'state',
            'city'])

        duplicate = self.check_duplicate_of_map_node(graph_node)
        
        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow([
                splited[0],
                splited[1],
                value[0],
                value[1],
                value[2]])

        csv_file.close()

    def check_duplicate_of_map_edge(self, graph_edge):
        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            
            if (geoloc['lat'] is None) or (geoloc2['lat'] is None):
                continue

            dup_key = str(geoloc['lat']) + ',' + str(geoloc['lng']) + ',' + str(
                geoloc2['lat']) + ',' + str(geoloc2['lng'])
            try:
                duplicate[dup_key]['packet_num'] += value['packet_num']
            except:
                duplicate[dup_key] = {
                    'packet_num' : value['packet_num'],
                    'timestamp' : value['timestamp']
                    }

        return duplicate

    def write_map_edge(self, graph_edge, filename):
        print("write map_edge")
        
        csv_file = open(
            "static/data/map/"+filename+"_edge.csv",
            mode = 'w',
            encoding = 'utf-8')
        writer = csv.writer(csv_file)

        writer.writerow([
            'src_lat',
            'src_lng',
            'dst_lat',
            'dst_lng',
            'count',
            'timestamp'])

        duplicate = self.check_duplicate_of_map_edge(graph_edge)
        
        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow([
                splited[0],
                splited[1],
                splited[2],
                splited[3],
                value['packet_num'],
                value['timestamp']
                ])

        csv_file.close()

    def remove_map_csv_file_list(self):
        file_path = os.getcwd()+'/static/data/map/'
        for file in os.listdir(file_path):
            if file.endswith('.csv'):
                os.remove(file_path+file)