from estrutura import Biblioteca, Fila

def solicitar_bpm():
    while True:
        entrada = input("BPM (batimentos por minuto): ")
        try:
            bpm = int(entrada)
            if bpm <= 0:
                print("Erro: O BPM deve ser um valor maior que zero.")
            else:
                return bpm
        except ValueError:
            print("Erro: O BPM deve ser um número inteiro válido.")

def main():
    biblioteca = Biblioteca()
    
    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    
    fila_historico = Fila() 

    while True:
        print("\n" + "="*30)
        print("🎶 SISTEMA DE PLAYLIST 🎶")
        print("1. Adicionar música à biblioteca")
        print("2. Remover música da biblioteca")
        print("3. Buscar música")
        print("4. Listar biblioteca completa")
        print("5. Montar fila de reprodução por humor")
        print("6. Reproduzir próxima")
        print("7. Exibir fila de humor")
        print("8. Exibir histórico de reproduções")
        print("9. Estatísticas")
        print("10. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n-- Adicionar Música --")
            titulo = input("Título: ")
            artista = input("Artista: ")
            genero = input("Gênero: ")
            bpm = solicitar_bpm()
            
            nova = biblioteca.inserir(titulo, artista, genero, bpm)
            if nova is None:
                print(f"Erro: A música '{titulo}' de '{artista}' já existe na biblioteca.")
            else:
                print(f"Música '{nova.titulo}' adicionada com sucesso! (ID: {nova.id})")

        elif opcao == "2":
            print("\n-- Remover Música --")
            try:
                id_remover = int(input("Informe o ID da música a ser removida: "))
                if biblioteca.remover(id_remover):
                    print("Música removida com sucesso!")
                else:
                    print("Erro: ID inexistente na biblioteca.")
            except ValueError:
                print("Erro: O ID deve ser um número.")

if __name__ == "__main__":
    main()