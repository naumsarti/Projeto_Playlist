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

    def remover(self, id_musica):
        atual = self.head
        anterior = None

        while atual is not None:
            if atual.musica.id == id_musica:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
            
        return False

    def buscar(self, termo):
        atual = self.head
        eh_id = False
        termo_id = -1
        
        try:
            termo_id = int(termo)
            eh_id = True
        except ValueError:
            pass

        while atual is not None:
            if eh_id and atual.musica.id == termo_id:
                return atual.musica
            elif not eh_id and atual.musica.titulo.lower() == termo.lower():
                return atual.musica
            atual = atual.proximo
            
        return None

    def listar_completa(self):
        atual = self.head
        if atual is None:
            print("A biblioteca está vazia.")
            return

        print("--- Biblioteca Completa ---")
        while atual is not None:
            m = atual.musica
            print(f"ID: {m.id} | {m.titulo} - {m.artista} | Gênero: {m.genero} | BPM: {m.bpm}")
            atual = atual.proximo

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)
        if self.tail is None:
            self.head = novo_nodo
            self.tail = novo_nodo
        else:
            self.tail.proximo = novo_nodo
            self.tail = novo_nodo
        self.tamanho += 1
    
    def dequeue(self):
        if self.head is None:
            return None
        
        musica_removida = self.head.musica
        self.head = self.head.proximo
        
        if self.head is None:
            self.tail = None
            
        self.tamanho -= 1
        return musica_removida
