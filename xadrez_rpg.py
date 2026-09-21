import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# ==========================================
# RASTREAMENTO GLOBAL DE NOMES ÚNICOS
# ==========================================
USADOS_NOMES = set()

def sortear_nome_unico(tipo):
    if tipo == 'rei':
        candidatos = [n for n in NOMES_REIS if n not in USADOS_NOMES]
        if not candidatos:
            candidatos = [f"ReiSupremo{random.randint(1000, 9999)}"]
    elif tipo == 'rainha':
        candidatos = [n for n in NOMES_RAINHAS if n not in USADOS_NOMES]
        if not candidatos:
            candidatos = [f"Imperatriz{random.randint(1000, 9999)}"]
    else:
        candidatos = [n for n in NOMES_COMUNS if n not in USADOS_NOMES]
        if not candidatos:
            candidatos = [f"Soldado{random.randint(1000, 9999)}"]
    
    escolhido = random.choice(candidatos)
    USADOS_NOMES.add(escolhido)
    return escolhido

# ==========================================
# LISTAS EXPANDIDAS DE NOMES E FALAS
# ==========================================

NOMES_REIS = [
    "Arthur", "Charles", "Leonidas", "Alexandre", "Luís", "Ricardo", "Pedro", 
    "Henrique", "Filipe", "Augusto", "Nero", "Constantin", "Sigismund", "Alaric", 
    "Ragnar", "Bjorn", "Valerius", "Tiberius", "Maximilian", "Vlad", "Ivan", 
    "Casimir", "Gustav", "Erik", "Aethelstan", "Cyrus", "Darius", "Trajan", "Justin",
    "Roger"
]

NOMES_RAINHAS = [
    "Elizabeth", "Victoria", "Cleópatra", "Catarina", "Maria", "Isabella", "Ana", 
    "Boudicca", "Zenobia", "Theodora", "Joan", "Eleanor", "Matilda", "Freydis", 
    "Lagertha", "Agrippina", "Messalina", "Octavia", "Guinevere", "Brunhild", 
    "Olimpias", "Tomyris", "Jing", "Artemisia"
]

NOMES_COMUNS = [
    "João", "José", "Carlos", "Ana", "Julia", "Marcos", "Pedro_C", "Felipe_C", 
    "Joana", "Sofia", "Lucas", "Miguel", "Lara", "Gabriel", "Beatriz", "Mateus", 
    "Laura", "Rafael", "Alice", "Bruno", "Camila", "Diego", "Eduarda", "Fernando", 
    "Gabriela", "Igor", "Juliana", "Leonardo", "Mariana", "Tiago", "Vicente", 
    "Otávio", "Marcelo", "Lorena", "Teresa", "Valéria", "Renato", "Sérgio", "Amanda",
    "Dante", "Enzo", "Clara", "Lorenzo", "Valentina", "Heitor", "Melissa", "Pietro", 
    "Yasmin", "Gael", "Giovanna", "Bernardo", "Nicole", "Thales", "Elena", "Arthur_Jr",
    "Vitor", "Heloisa", "Samuel", "Rebeca", "Caio", "Lívia", "Francisco", "Aline",
    "Breno", "Cibele", "Douglas", "Elisa", "Fabrício", "Giovana", "Humberto", "Ísis", "Pedro A.",
    "Neymar Jr.", "Chris", "Neymar Sr.", "Assassino", "Vampeta", "LinguiçoMan"
]

FALAS_MOVER = [
    "Avançando para a glória!", "Um passo mais perto da vitória.", "Eles não perdem por esperar.", 
    "Marchando para o combate.", "Meu destino me aguarda.", "Sinto o vento no meu rosto.",
    "Que os deuses do xadrez me protejam.", "Ninguém pode me parar!", "Estratégia é tudo.",
    "Devagar e sempre.", "Estou indo, estou indo!", "A guerra chama meu nome.",
    "Espero não pisar em nenhuma mina secreta.", "Movimento tático calculado.", "Pelo meu Rei!",
    "Minhas pernas já doem de tanto andar.", "Indo para a linha de frente.", "Que movimento brilhante.",
    "A morte rasteja pelo tabuleiro.", "Estou sentindo uma energia estranha hoje.", "Pronto para a ação.",
    "Avanço furtivo.", "Deixem comigo!", "Eles não vão nem ver o que os atingiu.", "Mais um dia, mais um passo.",
    "O xadrez é uma dança, e eu sou o dançarino.", "Vamos dominar o centro!", "Tomando posição.",
    "Esperando o momento certo.", "A cada passo, uma nova ameaça.", "As sombras me guiam.",
    "Táticas de guerrilha em ação.", "Pisando no campo de sangue.", "Meu escudo está erguido.",
    "Não temo o que há pela frente.", "A coragem me move.", "Abrindo caminho para os fortes.",
    "A poeira sobe sob meus passos.", "Olhos abertos, vida longa.", "Passos firmes no abismo."
]

FALAS_MATAR = [
    "Morra, escória!", "Menos um no tabuleiro.", "Foi fácil demais.", "Descanse em pedaços.",
    "O sangue mancha o tabuleiro hoje.", "Sinta a fúria da minha lâmina!", "Você era fraco.",
    "Nada pessoal, apenas negócios.", "Sua jornada termina aqui.", "A vitória exige sacrifícios.",
    "Eu sou a própria morte!", "Caiu como um patinho.", "Tome isso, verme!", "Limpei o caminho.",
    "Uma execução perfeita.", "Sua cabeça agora é meu troféu.", "Nem suei para fazer isso.",
    "Que os corvos devorem seus restos.", "O tabuleiro é meu reino, e você era um estorvo.", "Xeque-mate na sua vida.",
    "Você lutou mal e morreu pior ainda.", "Alguém limpe essa sujeira daqui.", "A lâmina cantou e sua cabeça rolou.",
    "Espero que tenha deixado testamento.", "Até no inferno você será perdedor.", "Um golpe limpo e fatal.",
    "Seu sacrifício não será lembrado.", "Eu corto, eu esmago, eu venço.", "Durma para sempre.", "Próximo!",
    "Nem o diabo te aceitaria agora.", "Vire adubo para o tabuleiro.", "Mais um para a cova.",
    "Sua defesa era uma piada.", "O aço frio é seu novo amigo.", "Sinta a dor da derrota eterna.",
    "Adeus ao pó que você era.", "Mais um troféu para a coleção."
]

FALAS_LUTO = [
    "NÃO! Por que os deuses são tão cruéis?!", "Vou vingar sua morte, eu juro!", "A guerra tira tudo de nós...",
    "Meu coração está despedaçado...", "Por que logo você?!", "Eu farei um rio com o sangue de quem te matou!",
    "Não haverá perdão para isso!", "A vida não faz mais sentido sem você no tabuleiro.", "Que dor insuportável!",
    "Eu devia ter te protegido...", "As trevas consumiram minha alma hoje.", "Choro lágrimas de sangue.",
    "Alguém traga ele de volta, por favor!", "Maldito seja esse jogo cruel!", "Como viverei depois disso?",
    "Levarei flores ao seu túmulo virtual.", "O tabuleiro ficou mais escuro hoje.", "Uma estrela se apagou.",
    "Minha fúria agora será implacável!", "A tristeza me consome por inteiro.", "Adeus, nobre alma.",
    "Nunca esquecerei do seu sorriso pixelado.", "Vou banhar o tabuleiro em lágrimas.", "Era a melhor peça de todas nós...",
    "Meu luto se transformará em vingança pura.", "Descanse em paz, guerreiro valente.", "Eu estou quebrado por dentro.",
    "Essa guerra não vale o preço que estamos pagando.", "Silêncio... um grande herói caiu.", "Que a terra lhe seja leve.",
    "As sombras nos abraçam agora.", "Mais uma cova, mais uma dor.", "Não esquecerei seu sacrifício.",
    "Um vazio que peça nenhuma pode preencher.", "Gritarei seu nome aos céus de guerra!"
]

FALAS_AMOR = [
    "Meu coração bate apenas por você.", "Nem essa guerra estúpida nos separará.", "Seus olhos brilham como porcelana.",
    "Dane-se as cores, eu te amo!", "Fugiríamos juntos se pudéssemos?", "Você é a única coisa bela neste tabuleiro.",
    "Meu amor por você é maior que qualquer Xeque-Mate.", "Promete que não vai morrer hoje?", "Se você cair, eu caio junto.",
    "Mesmo em lados opostos, nossas almas estão unidas.", "Daria minha vida pela sua sem pensar duas vezes.",
    "Cada movimento meu é pensando em você.", "Quando isso acabar, casaremos.", "Você ilumina minhas casas escuras.",
    "Esqueça a coroa, você é quem manda no meu coração.", "Um beijo roubado no meio da batalha...", 
    "Sua presença me acalma no meio da matança.", "Amor à primeira vista existe, e você é a prova.",
    "Quero segurar sua mão, mesmo que seja de madeira.", "Você me faz querer ser uma peça melhor.",
    "Nenhuma estratégia supera o que sinto por você.", "Guarde meu coração, pois ele te pertence.",
    "O amor floresce até nos campos de batalha.", "Eu te amarei em todas as partidas que jogarmos.",
    "Minha rainha/rei não é nada perto de você.", "Você é meu refúgio secreto.", "Amo você mais do que amo vencer.",
    "As regras dizem para matar, mas meu coração diz para amar.", "Somos Romeu e Julieta deste xadrez.", "Beije-me, agora!",
    "Estar a seu lado nesses últimos turnos acendeu minha chama.", "Não suporto ficar longe de você outra vez.",
    "Nossa proximidade revelou minha verdadeira paixão."
]

FALAS_ARMA = [
    "Tome chumbo grosso na cara!", "Headshot! Espalhei miolos pelo tabuleiro!", "Hasta la vista, baby.",
    "Comi suas tripas com essa bala de calibre 12!", "Fuzilamento tático concluído com sucesso.",
    "Engole esse míssil guiado!", "Desintegrado com sucesso pelo meu raio laser.", "Chuva de balas!",
    "Um tiro, uma morte sangrenta.", "Puxei o gatilho e a mágica brutal aconteceu.", "Não sobrou nem o pó de você.",
    "Acertei bem no meio dos olhos de longe!", "Armas de fogo vencem espadas, idiota.", "Explodi você em mil pedaços!",
    "O cheiro de pólvora e sangue fresco me excita.", "Varada de sniper atravessando corações!", 
    "Não adiantou correr da minha bazuca.", "Fuzilei sem piedade, que cena linda.", "Seu corpo parece um queijo suíço agora.",
    "Rajada de metralhadora rasgou sua carne!", "Tiro de escopeta à queima-roupa virtual!", "Bum! Adeus, perdedor.",
    "Minha mira é implacável e letal.", "O chumbo quente perfurou sua alma.", "Sangue espirrando pra todo lado, haha!",
    "Nem o hospital resolve o que eu fiz com você.", "Mandei bala até o dedo cansar.", "Granada na sua fuça!",
    "Um buraco no peito para você aprender a lição.", "Eliminação extrema a longa distância!",
    "Eu vi você correndo, mas a bala corre mais rápido.", "Limpei o campo com granadas estilhaçantes!"
]

FALAS_TEMOR_3 = [
    "Fiquem longe dessa aberração!", "Pelos deuses, é um monstro...",
    "Se ele chegar perto, corram para o outro lado!", "I don't want to die to his hands...",
    "Olhem os olhos dele... não há alma ali, só carnificina.", "Ele está rindo enquanto mata!",
    "É o próprio Ceifador disfarçado de peça. Fim dos tempos!",
    "Ninguém sobrevive a um encontro com ele.", "Minhas pernas de madeira tremem só de olhar."
]

FALAS_TEMOR_5 = [
    "Ele já ceifou cinco almas! Fujam!", "É um matadouro ambulante!", 
    "Nossas defesas não significam nada contra esse monstro!", "Estamos todos condenados!"
]

FALAS_TEMOR_7 = [
    "Sete mortes... Os deuses nos abandonaram!", "Ele não é mais uma peça, é um demônio sanguinário!",
    "O tabuleiro está encharcado com o sangue das sete vítimas!"
]

FALAS_TEMOR_9 = [
    "NOVE VIDAS ARRUINADAS! O fim está próximo!", "Piedade! Por favor, tenha piedade de nós!",
    "O ar ao redor dele cheira a morte pura!"
]

FALAS_TEMOR_10 = [
    "A LENDA NEGRA NASCEU! DEZ MORTES!", "Ninguém escapa! É o apocalipse no tabuleiro!",
    "Curvem-se perante o Deus da Morte!"
]

FALAS_MATAR_AMANTE = [
    "O que... O que eu fiz?! Meu amor, não!", "Minhas mãos estão sujas com o sangue de quem eu mais amava!",
    "Eu sou um monstro... Me perdoe, meu amor!", "A guerra me cegou! Eu matei minha alma gêmea!",
    "Não há mais razão para viver num tabuleiro sem você..."
]

FALAS_SOLIDAO = [
    "Ninguém me ama... sou só uma peça descartável nesta guerra fria.",
    "Estou tão sozinho... o eco do tabuleiro é ensurdecedor.",
    "Será que alguém nota que eu choro pixels nesta escuridão?",
    "A solidão é pior do que uma lâmina cravada no meu peito."
]

FALAS_ALIADO_CONSOLO = [
    "Cansado de esperar pelo amor impossível, achei aconchego em quem luta do meu lado.",
    "A guerra é cruel, mas meu aliado secou minhas lágrimas. Estamos juntos agora."
]

FALAS_CASAMENTO = [
    "💍 Juro amar-te e proteger-te até o último xeque-mate!",
    "💍 Com o caos como testemunha, nós nos casamos neste campo de batalha!",
    "💍 Aliança de ferro e alma! Estamos casados perante o destino!"
]

# ==========================================
# LÓGICA DO JOGO E CLASSES
# ==========================================

class Peca:
    def __init__(self, tipo, cor, nome):
        self.tipo = tipo
        self.cor = cor
        self.nome = nome
        self.amor = None
        self.viva = True
        self.id = random.randint(1000, 999999)
        self.kills = 0       
        self.temida = False  
        self.turnos_sem_amante = 0
        self.triste = False
        self.casado = False
        self.cooldown_romance = 0

    def get_simbolo(self):
        simbolos = {
            'branco': {'rei': '♔', 'rainha': '♕', 'torre': '♖', 'bispo': '♗', 'cavalo': '♘', 'peao': '♙'},
            'preto': {'rei': '♚', 'rainha': '♛', 'torre': '♜', 'bispo': '♝', 'cavalo': '♞', 'peao': '♟'}
        }
        return simbolos[self.cor][self.tipo]

class XadrezRPG:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.root.title("Xadrez RPG Dark: Guerra, Sangue e Amor")
        self.root.geometry("1300x800")
        self.root.config(bg="#1e1e1e")
        
        nome_b = simpledialog.askstring("Jogador Branco", "Nome do Jogador das Brancas:", initialvalue="Branco", parent=self.root)
        nome_b = nome_b if nome_b else "Brancas"
        
        nome_p = simpledialog.askstring("Jogador Preto", "Nome do Jogador das Pretas:", initialvalue="Preto", parent=self.root)
        nome_p = nome_p if nome_p else "Pretas"
        self.nomes_jogadores = {'branco': nome_b, 'preto': nome_p}
        
        self.root.deiconify()
        
        self.criar_menu()
        
        self.tamanho_casa = 85
        self.canvas = tk.Canvas(root, width=self.tamanho_casa*8, height=self.tamanho_casa*8, bg="#2b2b2b", highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, padx=30, pady=30)
        self.canvas.bind("<Button-1>", self.clicar)

        self.painel_lateral = tk.Frame(root, bg="#1e1e1e")
        self.painel_lateral.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=30)

        tk.Label(self.painel_lateral, text=f"⚪ {self.nomes_jogadores['branco']}  vs  ⚫ {self.nomes_jogadores['preto']}", 
                 font=("Arial", 11, "bold"), bg="#2d2d2d", fg="#ffcc00", relief="solid", bd=1).pack(fill=tk.X, pady=(0, 10), ipady=5)

        self.btn_reset = tk.Button(self.painel_lateral, text="🔄 Resetar Batalha", font=("Arial", 12, "bold"), 
                                   bg="#444444", fg="white", activebackground="#666666", activeforeground="white", command=self.resetar_jogo)
        self.btn_reset.pack(fill=tk.X, pady=(0, 10))

        self.btn_modo = tk.Button(self.painel_lateral, text="Ativar Modo Arma (Brutal)", font=("Arial", 12, "bold"), 
                                  bg="darkred", fg="white", activebackground="red", activeforeground="white", command=self.alternar_modo)
        self.btn_modo.pack(fill=tk.X, pady=10)
        
        tk.Label(self.painel_lateral, text="Log de Batalha (Chat das Peças)", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="#d4d4d4").pack(pady=5)
        
        self.scroll = tk.Scrollbar(self.painel_lateral)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text = tk.Text(self.painel_lateral, height=27, width=55, yscrollcommand=self.scroll.set, wrap=tk.WORD, 
                                font=("Consolas", 10), bg="#2d2d2d", fg="#ffffff", insertbackground="white")
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.config(command=self.log_text.yview)

        self.log_text.tag_config('amor', foreground='#90EE90')
        self.log_text.tag_config('casamento', foreground='#FF69B4')
        self.log_text.tag_config('solidao', foreground='#00008B')
        self.log_text.tag_config('uniao', foreground='#006400')
        self.log_text.tag_config('casamento_aliado', foreground='#D3D3D3')
        self.log_text.tag_config('divorcio', foreground='#A9A9A9')

        self.iniciar_estado_jogo()

    def criar_menu(self):
        menubar = tk.Menu(self.root)
        ajuda_menu = tk.Menu(menubar, tearoff=0)
        ajuda_menu.add_command(label="Legenda de Cores", command=self.mostrar_legenda_cores)
        menubar.add_cascade(label="Ajuda", menu=ajuda_menu)
        self.root.config(menu=menubar)

    def mostrar_legenda_cores(self):
        janela_legenda = tk.Toplevel(self.root)
        janela_legenda.title("Legenda de Cores do Chat")
        janela_legenda.geometry("440x300")
        janela_legenda.config(bg="#1e1e1e")
        
        tk.Label(janela_legenda, text="Significado das Cores do Chat", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)
        
        legenda_dados = [
            ("#90EE90", "Verde Claro", "Amantes / Paixão romântica"),
            ("#FF69B4", "Rosa", "Casamento / Zueira Bongcloud"),
            ("#00008B", "Azul Escuro", "Solidão / Depressão da peça"),
            ("#006400", "Verde Escuro", "União de consolo (mesmo time)"),
            ("#D3D3D3", "Cinza Claro", "Casamento entre aliados"),
            ("#A9A9A9", "Cinza Escuro", "Separação / Divórcio")
        ]
        
        for hex_code, nome_cor, desc in legenda_dados:
            frame_item = tk.Frame(janela_legenda, bg="#1e1e1e")
            frame_item.pack(fill=tk.X, padx=20, pady=4)
            tk.Label(frame_item, text=f"■ {nome_cor}:", font=("Consolas", 10, "bold"), fg=hex_code, bg="#1e1e1e", width=18, anchor="w").pack(side=tk.LEFT)
            tk.Label(frame_item, text=desc, font=("Arial", 10), fg="white", bg="#1e1e1e", anchor="w").pack(side=tk.LEFT)

    def iniciar_estado_jogo(self):
        global USADOS_NOMES
        USADOS_NOMES.clear()
        
        self.jogo_ativo = True
        self.modo_arma = False
        self.turno = 'branco'
        self.selecionada = None
        self.pos_selecionada = None
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.pecas_vivas = []
        self.proximidade_romance = {}
        self.turnos_casamento_proximo = {}
        
        self.turno_global = 0
        self.divorce_block = 0
        self.cooldown_solidao = 0
        self.cooldown_consolo = 0
        
        self.inicializar_tabuleiro()
        self.desenhar_tabuleiro()
        self.registrar_log(f"🛡️ Batalha Iniciada: {self.nomes_jogadores['branco']} (Brancas) vs {self.nomes_jogadores['preto']} (Pretas)!\nModo Caos / Sem Xeque-Mate ativo.")

    def resetar_jogo(self):
        self.log_text.delete('1.0', tk.END)
        self.btn_modo.config(text="Ativar Modo Arma (Brutal)", bg="darkred", fg="white")
        self.iniciar_estado_jogo()
        self.registrar_log("⏳ O tempo retrocedeu... As almas caídas retornaram. Uma nova guerra se inicia!")

    def registrar_log(self, texto, tag=None):
        if tag:
            self.log_text.insert(tk.END, texto + "\n\n", tag)
        else:
            self.log_text.insert(tk.END, texto + "\n\n")
        self.log_text.see(tk.END)

    def inicializar_tabuleiro(self):
        ordem = ['torre', 'cavalo', 'bispo', 'rainha', 'rei', 'bispo', 'cavalo', 'torre']
        for c in range(8):
            tipo_p = ordem[c]
            peca_p = Peca(tipo_p, 'preto', sortear_nome_unico(tipo_p))
            self.tabuleiro[0][c] = peca_p
            self.pecas_vivas.append(peca_p)
            
            peao_p = Peca('peao', 'preto', sortear_nome_unico('peao'))
            self.tabuleiro[1][c] = peao_p
            self.pecas_vivas.append(peao_p)

            peao_b = Peca('peao', 'branco', sortear_nome_unico('peao'))
            self.tabuleiro[6][c] = peao_b
            self.pecas_vivas.append(peao_b)
            
            tipo_b = ordem[c]
            peca_b = Peca(tipo_b, 'branco', sortear_nome_unico(tipo_b))
            self.tabuleiro[7][c] = peca_b
            self.pecas_vivas.append(peca_b)

    def desenhar_tabuleiro(self):
        self.canvas.delete("all")
        cor_clara = "#8a8a8a"
        cor_escura = "#4a4a4a" if not self.modo_arma else "#7a0000"

        for l in range(8):
            for c in range(8):
                x1, y1 = c * self.tamanho_casa, l * self.tamanho_casa
                x2, y2 = x1 + self.tamanho_casa, y1 + self.tamanho_casa
                cor_fundo = cor_clara if (l + c) % 2 == 0 else cor_escura
                
                if self.pos_selecionada == (l, c):
                    cor_fundo = "#b8860b"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor_fundo, outline="#111111")

                peca = self.tabuleiro[l][c]
                if peca:
                    cor_simbolo = "#000000" if peca.cor == "preto" else "#ffffff"
                    cor_nome = "#ff9999" if peca.cor == "preto" else "#99ccff"
                    texto_nome = peca.nome
                    
                    if peca.casado:
                        texto_nome = f"💍{texto_nome}"
                    elif peca.triste:
                        texto_nome = f"😢{texto_nome}"

                    if peca.temida:
                        if peca.kills >= 10:
                            cor_nome = "#ff00ff"
                            texto_nome = f"🌋 DEUS(A) {texto_nome}"
                        elif peca.kills >= 7:
                            cor_nome = "#ff0000"
                            texto_nome = f"👹 {texto_nome}"
                        elif peca.kills >= 5:
                            cor_nome = "#ff4444"
                            texto_nome = f"💀 {texto_nome} 💀"
                        else:
                            cor_nome = "#ff8888"
                            texto_nome = f"☠️ {texto_nome} ☠️"
                            
                    par_dados = []
                    if peca.amor:
                        par_dados.append(peca.amor.nome)
                    if peca.kills > 0:
                        par_dados.append(f"{peca.kills}x🗡️")
                        
                    if par_dados:
                        texto_nome += f" ({', '.join(par_dados)})"

                    self.canvas.create_text(x1 + self.tamanho_casa//2, y1 + self.tamanho_casa//2 - 10, 
                                            text=peca.get_simbolo(), font=("Arial", 45), fill=cor_simbolo)
                    self.canvas.create_text(x1 + self.tamanho_casa//2, y1 + self.tamanho_casa - 15, 
                                            text=texto_nome, font=("Arial", 9, "bold"), fill=cor_nome)

    def alternar_modo(self):
        self.modo_arma = not self.modo_arma
        if self.modo_arma:
            self.btn_modo.config(text="Desativar Modo Arma (Normal)", bg="#444444", fg="white")
            self.registrar_log("⚠️ ALERTA: MODO ARMA LIGADO! Reis e Peões pegaram fuzis e snipers. Sangue vai jorrar.")
        else:
            self.btn_modo.config(text="Ativar Modo Arma (Brutal)", bg="darkred", fg="white")
            self.registrar_log("☮️ Modo Arma desativado. Facas e espadas de volta às mãos.")
        self.desenhar_tabuleiro()

    def caminho_livre(self, l_orig, c_orig, l_dest, c_dest, board=None):
        if board is None:
            board = self.tabuleiro
        passo_l = (l_dest - l_orig) // max(1, abs(l_dest - l_orig)) if l_dest != l_orig else 0
        passo_c = (c_dest - c_orig) // max(1, abs(c_dest - c_orig)) if c_dest != c_orig else 0
        
        curr_l, curr_c = l_orig + passo_l, c_orig + passo_c
        while (curr_l, curr_c) != (l_dest, c_dest):
            if board[curr_l][curr_c] is not None:
                return False
            curr_l += passo_l
            curr_c += passo_c
        return True

    def movimento_geometrico_valido(self, peca, l_orig, c_orig, l_dest, c_dest, board=None):
        if board is None:
            board = self.tabuleiro
        if l_orig == l_dest and c_orig == c_dest: return False
        alvo = board[l_dest][c_dest]
        if alvo and alvo.cor == peca.cor: return False

        dr = abs(l_dest - l_orig)
        dc = abs(c_dest - c_orig)

        if peca.tipo == 'peao':
            direcao = -1 if peca.cor == 'branco' else 1
            if dc == 0:
                if l_dest == l_orig + direcao and alvo is None: return True
                if l_dest == l_orig + 2 * direcao and alvo is None and l_orig in (1, 6):
                    if board[l_orig + direcao][c_orig] is None: return True
            elif dc == 1 and l_dest == l_orig + direcao and alvo is not None: return True
            return False

        elif peca.tipo == 'torre':
            if dr == 0 or dc == 0: return self.caminho_livre(l_orig, c_orig, l_dest, c_dest, board)
            return False

        elif peca.tipo == 'bispo':
            if dr == dc: return self.caminho_livre(l_orig, c_orig, l_dest, c_dest, board)
            return False

        elif peca.tipo == 'rainha':
            if dr == 0 or dc == 0 or dr == dc: return self.caminho_livre(l_orig, c_orig, l_dest, c_dest, board)
            return False

        elif peca.tipo == 'cavalo':
            if (dr == 2 and dc == 1) or (dr == 1 and dc == 2): return True
            return False

        elif peca.tipo == 'rei':
            if dr <= 1 and dc <= 1: return True
            return False

        return False

    def square_attacked(self, l, c, attacker_cor, board):
        for r in range(8):
            for col in range(8):
                p = board[r][col]
                if p and p.cor == attacker_cor:
                    if self.movimento_geometrico_valido(p, r, col, l, c, board):
                        return True
        return False

    def rei_em_check(self, cor, board=None):
        if board is None:
            board = self.tabuleiro
        kr, kc = None, None
        for r in range(8):
            for col in range(8):
                p = board[r][col]
                if p and p.cor == cor and p.tipo == 'rei':
                    kr, kc = r, col
                    break
            if kr is not None: break
        if kr is None: return False
        oponente = 'preto' if cor == 'branco' else 'branco'
        return self.square_attacked(kr, kc, oponente, board)

    def movimento_legal(self, peca, l_orig, c_orig, l_dest, c_dest):
        # Sem restrição de xeque/proteção de rei
        return self.movimento_geometrico_valido(peca, l_orig, c_orig, l_dest, c_dest)

    def tem_qualquer_movimento_legal(self, cor):
        return True

    def trigger_bongcloud_laugh(self, cor_rei):
        nome_j = self.nomes_jogadores[cor_rei]
        self.registrar_log(f"\n🤡 [BONGCLOUD ALERT] {nome_j} jogou o Rei ridículo! (Movimento icônico do caos)", tag='casamento')
        risos = [
            f"HAHAHA! Olha o {nome_j} correndo risco com o Bongcloud!",
            f"BWAHAHAHA! Gênio ou insano? {nome_j} adora uma palhaçada de Rei!",
            f"KKKKKKK! {nome_j} mandou o Ke2/Ke7 clássico para zoar a partida!",
            f"HEHEHEHE! O exército inteiro aponta para {nome_j} rindo da audácia!",
            f"MUHAHAHA! Alguém avisa o {nome_j} que xadrez sério acabou!"
        ]
        amostra = random.sample(self.pecas_vivas, min(4, len(self.pecas_vivas))) if self.pecas_vivas else []
        for p_rindo in amostra:
            fala_risada = random.choice(risos)
            self.registrar_log(f"🤭 {p_rindo.nome} ri da cara de {nome_j}: '{fala_risada}'", tag='casamento')

    def clicar(self, event):
        if not self.jogo_ativo: return

        c = event.x // self.tamanho_casa
        l = event.y // self.tamanho_casa

        if not (0 <= l <= 7 and 0 <= c <= 7): return

        peca_clicada = self.tabuleiro[l][c]

        if peca_clicada and peca_clicada.cor == self.turno:
            self.selecionada = peca_clicada
            self.pos_selecionada = (l, c)
            self.desenhar_tabuleiro()
            return

        if self.selecionada:
            linha_origem, col_origem = self.pos_selecionada
            alvo = peca_clicada
            
            if self.modo_arma and alvo and alvo.cor != self.turno and self.selecionada.tipo in ['rei', 'peao']:
                self.atirar_de_longe(self.selecionada, alvo, l, c)
                self.processar_fim_turno()
                return

            if self.movimento_legal(self.selecionada, linha_origem, col_origem, l, c):
                is_bongcloud = False
                if self.selecionada.tipo == 'rei' and c == 4 and col_origem == 4:
                    if self.selecionada.cor == 'branco' and linha_origem == 7 and l == 6:
                        is_bongcloud = True
                    elif self.selecionada.cor == 'preto' and linha_origem == 0 and l == 1:
                        is_bongcloud = True

                acao = "matou" if alvo else "moveu"
                
                if acao == "matou":
                    self.matar(self.selecionada, alvo)
                else:
                    fala = random.choice(FALAS_MOVER)
                    status = " ☠️(Temido)" if self.selecionada.temida else ""
                    self.registrar_log(f"👟 {self.selecionada.nome}{status} ({self.selecionada.tipo}): '{fala}'")

                self.tabuleiro[l][c] = self.selecionada
                self.tabuleiro[linha_origem][col_origem] = None
                
                if is_bongcloud:
                    self.trigger_bongcloud_laugh(self.selecionada.cor)

                self.selecionada = None
                self.pos_selecionada = None
                
                self.processar_fim_turno()
            else:
                self.registrar_log(f"⚠️ {self.selecionada.nome} tropeça... Movimento inválido!")

    def verificar_temor(self, peca):
        inimigos = [p for p in self.pecas_vivas if p.cor != peca.cor]
        
        if peca.kills == 3 and not peca.temida:
            peca.temida = True
            self.registrar_log(f"\n🔥 [EVENTO DE TERROR] O tabuleiro congela! {peca.nome} acaba de fazer sua 3ª vítima.")
            self.registrar_log(f"☠️ {peca.nome} ESTÁ SEDENTO POR SANGUE E AGORA É TEMIDO POR TODOS!")
            if inimigos:
                assustado = random.choice(inimigos)
                self.registrar_log(f"😨 {assustado.nome} ({assustado.tipo} inimigo) grita: '{random.choice(FALAS_TEMOR_3)}'\n")
                
        elif peca.kills == 5:
            self.registrar_log(f"\n🩸 [CARNIFICINA] {peca.nome} chegou a 5 mortes! O pânico se espalha!")
            if inimigos:
                self.registrar_log(f"😨 {random.choice(inimigos).nome} grita: '{random.choice(FALAS_TEMOR_5)}'\n")
                
        elif peca.kills == 7:
            self.registrar_log(f"\n💀 [MASSACRE] 7 vítimas! A mera presença de {peca.nome} apodrece as casas do tabuleiro!")
            if inimigos:
                self.registrar_log(f"😱 {random.choice(inimigos).nome} chora: '{random.choice(FALAS_TEMOR_7)}'\n")
                
        elif peca.kills == 9:
            self.registrar_log(f"\n🌑 [DEMÔNIO DESPERTO] 9 abates! As peças começam a tremer incontrolavelmente!")
            if inimigos:
                self.registrar_log(f"🥶 {random.choice(inimigos).nome} implora: '{random.choice(FALAS_TEMOR_9)}'\n")
                
        elif peca.kills == 10:
            self.registrar_log(f"\n🌋 [DEUS DA MORTE] 10 MORTES! {peca.nome} TRANSCENDEU A GUERRA! TODOS SE AJOELHAM EM DESESPERO!")
            if inimigos:
                self.registrar_log(f"✝️ {random.choice(inimigos).nome} sussurra: '{random.choice(FALAS_TEMOR_10)}'\n")

    def atirar_de_longe(self, atirador, alvo, linha_alvo, col_alvo):
        self.registrar_log(f"🔫 [ATAQUE À DISTÂNCIA] {atirador.nome} mira sua arma em {alvo.nome}...")
        
        if atirador.amor == alvo:
            atirador.triste = True
            self.registrar_log(f"\n🖤 [TRAGÉDIA CEGA] Ao puxar o gatilho, {atirador.nome} percebe tarde demais em quem atirou!")
            self.registrar_log(f"😭 {atirador.nome}: '{random.choice(FALAS_MATAR_AMANTE)}'")
            atirador.nome = f"Trágico {atirador.nome}"
        else:
            fala_arma = random.choice(FALAS_ARMA)
            self.registrar_log(f"💥 {atirador.nome}: '{fala_arma}'")
            
        self.registrar_log(f"🩸 O corpo de {alvo.nome} é brutalmente destroçado e cai fora do tabuleiro!")
        
        atirador.kills += 1
        self.tabuleiro[linha_alvo][col_alvo] = None
        self.executar_morte(alvo, atirador)
        self.verificar_temor(atirador)
        
        self.selecionada = None
        self.pos_selecionada = None

    def matar(self, assassino, vitima):
        if assassino.amor == vitima:
            assassino.triste = True
            self.registrar_log(f"\n🖤 [TRAGÉDIA] A LÂMINA CAIU SOBRE A PESSOA ERRADA! {assassino.nome} ATACOU SEU PRÓPRIO AMOR!")
            self.registrar_log(f"😭 {assassino.nome}: '{random.choice(FALAS_MATAR_AMANTE)}'")
            assassino.nome = f"Traidor {assassino.nome}"
        else:
            fala_kill = random.choice(FALAS_MATAR)
            self.registrar_log(f"⚔️ {assassino.nome} massacrou {vitima.nome} corpo a corpo!")
            self.registrar_log(f"😈 {assassino.nome}: '{fala_kill}'")
        
        assassino.kills += 1
        self.executar_morte(vitima, assassino)
        self.verificar_temor(assassino)

    def executar_morte(self, vitima, assassino=None):
        vitima.viva = False
        if vitima in self.pecas_vivas:
            self.pecas_vivas.remove(vitima)

        for peca in list(self.pecas_vivas):
            if peca.amor == vitima:
                peca.triste = True
                peca.amor = None
                peca.casado = False
                peca.cooldown_romance = 3
                if peca == assassino:
                    pass
                else:
                    fala_luto = random.choice(FALAS_LUTO)
                    self.registrar_log(f"💔 DRAMA! {peca.nome} (amante) cai de joelhos em desespero:")
                    self.registrar_log(f"😭 {peca.nome}: '{fala_luto}'")
            elif peca.cor == vitima.cor and random.random() < 0.20:
                fala_luto = random.choice(FALAS_LUTO)
                self.registrar_log(f"😢 {peca.nome} (Aliado): '{fala_luto}'")
            elif peca.cor != vitima.cor and random.random() < 0.05:
                self.registrar_log(f"♟️ {peca.nome} (Inimigo) murmura: 'Era um grande oponente. Descanse.'")

        if vitima.tipo == 'rei' and self.jogo_ativo:
            self.jogo_ativo = False
            vencedor_cor = "Pretas" if vitima.cor == "branco" else "Brancas"
            vencedor_nome = self.nomes_jogadores['preto' if vitima.cor == 'branco' else 'branco']
            msg = f"👑 FIM DE JOGO! O Rei de {self.nomes_jogadores[vitima.cor]} foi ASSASSINADO!\n{vencedor_nome} ({vencedor_cor}) vence a guerra!"
            self.registrar_log("="*40)
            self.registrar_log(msg.upper())
            self.registrar_log("="*40)
            messagebox.showinfo("Fim de Jogo", msg)

    def checar_romance(self):
        posicoes = {}
        for l in range(8):
            for c in range(8):
                p = self.tabuleiro[l][c]
                if p: posicoes[p.id] = (l, c, p)

        pares_atuais = set()

        for id1, (l1, c1, p1) in posicoes.items():
            for id2, (l2, c2, p2) in posicoes.items():
                if id1 >= id2: continue
                if p1.tipo in ['rei', 'rainha'] or p2.tipo in ['rei', 'rainha']: continue
                if p1.cor == p2.cor: continue
                if p1.amor is not None or p2.amor is not None: continue
                if p1.cooldown_romance > 0 or p2.cooldown_romance > 0: continue
                if p1.amor == p2 or p2.amor == p1: continue
                
                if abs(l1 - l2) <= 1 and abs(c1 - c2) <= 1:
                    par = (id1, id2)
                    pares_atuais.add(par)
                    self.proximidade_romance[par] = self.proximidade_romance.get(par, 0) + 1
                    
                    if self.proximidade_romance[par] >= 3:
                        p1.amor = p2
                        p2.amor = p1
                        fala = random.choice(FALAS_AMOR)
                        self.registrar_log(f"❤️ EVENTO DE ROMANCE: Após passarem turnos próximos, {p1.nome} e {p2.nome} se apaixonaram! (amor proibido inimigo!)", tag='amor')
                        self.registrar_log(f"😍 {p1.nome} confessa: '{fala}'", tag='amor')
                        self.proximidade_romance[par] = -999 

        para_remover = [par for par in self.proximidade_romance if par not in pares_atuais and self.proximidade_romance[par] >= 0]
        for par in para_remover: del self.proximidade_romance[par]

    def processar_solidao_e_casamento(self):
        if self.cooldown_solidao > 0:
            self.cooldown_solidao -= 1
        if self.cooldown_consolo > 0:
            self.cooldown_consolo -= 1
        if self.divorce_block > 0:
            self.divorce_block -= 1

        for p in self.pecas_vivas:
            if p.cooldown_romance > 0:
                p.cooldown_romance -= 1

        candidatos_depressao = []
        candidatos_consolo = []

        for p in list(self.pecas_vivas):
            if p.tipo not in ['rei', 'rainha'] and p.amor is None:
                p.turnos_sem_amante += 1
                if p.turnos_sem_amante >= 10 and not p.triste:
                    candidatos_depressao.append(p)
                if p.turnos_sem_amante >= 15:
                    candidatos_consolo.append(p)
            else:
                p.turnos_sem_amante = 0
                if p.amor is not None:
                    p.triste = False

        if candidatos_depressao and self.cooldown_solidao == 0:
            escolhida = random.choice(candidatos_depressao)
            escolhida.triste = True
            self.registrar_log(f"😢 [SOLIDÃO] {escolhida.nome} está deprimido(a) por falta de amor há 10+ turnos!", tag='solidao')
            self.registrar_log(f"💬 {escolhida.nome}: '{random.choice(FALAS_SOLIDAO)}'", tag='solidao')
            self.cooldown_solidao = 5

        if candidatos_consolo and self.cooldown_consolo == 0:
            p = random.choice(candidatos_consolo)
            aliados = [a for a in self.pecas_vivas if a.cor == p.cor and a != p and a.amor is None and a.tipo not in ['rei', 'rainha'] and a.cooldown_romance == 0]
            if aliados:
                aliado = random.choice(aliados)
                p.amor = aliado
                aliado.amor = p
                p.triste = False
                p.turnos_sem_amante = 0
                aliado.turnos_sem_amante = 0
                self.registrar_log(f"🤝 [CONSOLO] {p.nome}, cansado(a) da solidão, uniu-se ao aliado {aliado.nome}!", tag='uniao')
                self.registrar_log(f"💬 {p.nome}: '{random.choice(FALAS_ALIADO_CONSOLO)}'", tag='uniao')
                self.cooldown_consolo = 4

        posicoes = {}
        for l in range(8):
            for c in range(8):
                p = self.tabuleiro[l][c]
                if p: posicoes[p.id] = (l, c, p)

        pares_proximos = set()
        for id1, (l1, c1, p1) in posicoes.items():
            for id2, (l2, c2, p2) in posicoes.items():
                if id1 >= id2: continue
                if p1.amor == p2 and not p1.casado:
                    if max(abs(l1 - l2), abs(c1 - c2)) <= 3:
                        par = (id1, id2)
                        pares_proximos.add(par)
                        self.turnos_casamento_proximo[par] = self.turnos_casamento_proximo.get(par, 0) + 1
                        if self.turnos_casamento_proximo[par] >= 5:
                            p1.casado = True
                            p2.casado = True
                            tag_casamento = 'casamento_aliado' if p1.cor == p2.cor else 'casamento'
                            self.registrar_log(f"💒 [CASAMENTO] Após 5 turnos próximos, {p1.nome} e {p2.nome} casaram-se no front!", tag=tag_casamento)
                            self.registrar_log(f"💍 {p1.nome}: '{random.choice(FALAS_CASAMENTO)}'", tag=tag_casamento)

        para_remover = [par for par in self.turnos_casamento_proximo if par not in pares_proximos]
        for par in para_remover: del self.turnos_casamento_proximo[par]

        if self.turno_global >= 20 and self.turno_global % 20 == 0 and self.divorce_block == 0:
            casais_unicos = []
            vistas = set()
            for p in self.pecas_vivas:
                if p.amor and id(p) not in vistas and id(p.amor) not in vistas:
                    casais_unicos.append((p, p.amor))
                    vistas.add(id(p))
                    vistas.add(id(p.amor))
            
            if casais_unicos:
                p1, p2 = random.choice(casais_unicos)
                p1.amor = None
                p2.amor = None
                p1.casado = False
                p2.casado = False
                p1.cooldown_romance = 3
                p2.cooldown_romance = 3
                self.registrar_log(f"💔 [DIVÓRCIO] O estresse do front rompeu o laço entre {p1.nome} e {p2.nome}!", tag='divorcio')
                self.divorce_block = 10

    def processar_fim_turno(self):
        if not self.jogo_ativo: return
        self.turno_global += 1
        self.checar_romance()
        self.processar_solidao_e_casamento()
        
        # Alternância livre de turno sem checar xeque-mate
        self.turno = 'preto' if self.turno == 'branco' else 'branco'
        self.desenhar_tabuleiro()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = XadrezRPG(root)
    root.mainloop()
