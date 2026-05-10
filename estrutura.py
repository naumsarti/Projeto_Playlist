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

class Biblioteca:
    def __init__(self):
        self.head = None
        self._proximo_id = 1
        self.tamanho = 0

    def existe(self, titulo, artista):
        atual = self.head
        while atual is not None:
            m = atual.musica
            if m.titulo.lower() == titulo.lower() and m.artista.lower() == artista.lower():
                return True
            atual = atual.proximo
        return False

    def inserir(self, titulo, artista, genero, bpm):
        if self.existe(titulo, artista):
            return None

        nova_musica = Musica(self._proximo_id, titulo, artista, genero, bpm)
        self._proximo_id += 1
        novo_nodo = NodoLista(nova_musica)

        if self.head is None:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
            
        self.tamanho += 1
        return nova_musica
