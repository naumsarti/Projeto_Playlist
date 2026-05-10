class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Musica:
    def __init__(self, id_musica, titulo, artista, genero, bpm):
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

