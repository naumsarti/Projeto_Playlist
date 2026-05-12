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
        print("   SISTEMA DE PLAYLIST")
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

        elif opcao == "3":
            print("\n-- Buscar Música --")
            termo = input("Informe o ID ou Título da música: ")
            musica = biblioteca.buscar(termo)
            if musica:
                print("\nMúsica Encontrada:")
                print(f"ID: {musica.id} | {musica.titulo} - {musica.artista} | Gênero: {musica.genero} | BPM: {musica.bpm}")
            else:
                print("Música não encontrada.")

        elif opcao == "4":
            print("\n")
            biblioteca.listar_completa()

        elif opcao == "5":
            print("\n-- Montando Filas de Reprodução --")
            fila_relaxar.limpar()
            fila_focar.limpar()
            fila_animar.limpar()
            fila_treinar.limpar()

            atual = biblioteca.head
            musicas_enfileiradas = 0

            while atual is not None:
                m = atual.musica
                if m.bpm <= 80:
                    fila_relaxar.enqueue(m)
                elif 81 <= m.bpm <= 120:
                    fila_focar.enqueue(m)
                elif 121 <= m.bpm <= 160:
                    fila_animar.enqueue(m)
                else:
                    fila_treinar.enqueue(m)
                    
                atual = atual.proximo
                musicas_enfileiradas += 1

            if musicas_enfileiradas == 0:
                print("A biblioteca está vazia. Nenhuma fila foi montada.")
            else:
                print("Filas montadas com sucesso baseadas na biblioteca atual!")

        elif opcao == "6":
            print("\n-- Reproduzir Próxima --")
            print("Humores: 1-Relaxar | 2-Focar | 3-Animar | 4-Treinar")
            humor = input("Escolha o humor da fila: ")
            
            musica_tocada = None
            if humor == "1":
                musica_tocada = fila_relaxar.dequeue()
            elif humor == "2":
                musica_tocada = fila_focar.dequeue()
            elif humor == "3":
                musica_tocada = fila_animar.dequeue()
            elif humor == "4":
                musica_tocada = fila_treinar.dequeue()
            else:
                print("Opção de humor inválida.")
                continue

            if musica_tocada is None:
                print("Erro: A fila escolhida está vazia. (Dica: Use a opção 5 para montar as filas).")
            else:
                print(f"▶ Reproduzindo agora: {musica_tocada.titulo} - {musica_tocada.artista} ({musica_tocada.bpm} BPM)")
                fila_historico.enqueue(musica_tocada)

        elif opcao == "7":
            print("\n-- Exibir Fila de Humor --")
            print("Humores: 1-Relaxar | 2-Focar | 3-Animar | 4-Treinar")
            humor = input("Escolha o humor da fila: ")
            
            print("\n--- Fila Atual ---")
            if humor == "1":
                fila_relaxar.exibir()
            elif humor == "2":
                fila_focar.exibir()
            elif humor == "3":
                fila_animar.exibir()
            elif humor == "4":
                fila_treinar.exibir()
            else:
                print("Opção inválida.")

        elif opcao == "8":
            print("\n-- Histórico de Reproduções --")
            fila_historico.exibir()

        elif opcao == "10":
            print("Encerrando o Sistema de Playlist. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()