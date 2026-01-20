import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        min_albums = self._view.txtNumAlbumMin.value
        try:
            min_albums = int(min_albums)
            if min_albums > 0: graph = self._model.build_graph(min_albums)
            else: raise Exception()
        except Exception as e: self._view.show_alert(f"Inserire un valore valido")
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {graph.number_of_nodes()} nodi (artisti), {graph.number_of_edges()} archi"))
        self._view.update_page()
        self._view.ddArtist.disabled = False
        self._view.btnArtistsConnected.disabled = False
        for n in graph.nodes():
            self._view.ddArtist.options.append(ft.DropdownOption(key=n.id,text=n.name))
        self._view.update_page()
    def handle_connected_artists(self, e):
        artist = self._view.ddArtist.value
        collegati = self._model.artisti_collegati(int(artist[0]))
        print(collegati)
        for c in collegati:
            self._view.txt_result.controls.append(ft.Text(f"Collegati: {c.name} nodi (artisti), {c.id}"))
        self._view.update_page()

