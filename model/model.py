import networkx as nx
from database.dao import DAO
from model.artist import Artist as a

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.artists_min_album_dict = {}
        self.generi_dict = {}

    def load_artists_with_min_albums(self,min_albums):
        self.artists_min_album_list = DAO.get_artists_min_albums(min_albums)
        for artist in self.artists_min_album_list:
            self.artists_min_album_dict[artist.id] = artist

    def build_graph(self,min_albums):
        self._graph.clear()
        self.load_artists_with_min_albums(min_albums)
        self._graph.add_nodes_from(self.artists_min_album_list)
        print(self._graph)
        self.load_generi(min_albums)
        for key,genres in self.generi_dict.items():
             for artist in genres:
                 self.artists_min_album_dict[artist].add_genre(key)
        for i in range(len(self.artists_min_album_list)):
            for j in range(i + 1, len(self.artists_min_album_list)):
                p1 = self.artists_min_album_list[i]
                p2 = self.artists_min_album_list[j]
                if len(p1.genre.union(p2.genre)) > 0:
                    self._graph.add_edge(p1, p2, weight=len(p1.genre.union(p2.genre)))
        return self._graph
    def load_generi(self,min_albums):
        self.generi_list = DAO.get_track(min_albums)
        for track in self.generi_list:
            self.generi_dict[track.genre_id] = set()
        for track in self.generi_list:
            self.generi_dict[track.genre_id].add(track.artistid)
        print(self.generi_dict)

    def artisti_collegati(self,artista):
        for a in self.artists_min_album_list:
            if a.id == artista:
                collegati = nx.node_connected_component(self._graph,a)
                return collegati



