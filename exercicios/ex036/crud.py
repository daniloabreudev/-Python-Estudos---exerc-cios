import sqlite3

NOME_BANCO = "cadastro.db"

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS pessoas (cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL,altura REAL NOT NULL);")
            return  True
    except sqlite3.Error as erro:
        print(f"FAlha na criação do banco: {erro}")
        return  False

def cadastrar_pessoa() -> bool:
    print("\n === NOVO CADASTRO DE PESSOA ===")

    #leitura e validação dos dados
    val_nome = input("NOME: ").strip()
    if not val_nome:
        print("[ERRO] I nome é um campo obrigatório!")
        return False

    val_altura = input("ALTURA:(metros) ").strip().replace(",", ".")
    if not val_altura:
        print("[ERRO] A altura é um campo obrigatório")
        return False
    try:
        altura = float(val_altura)
        if altura <= 0.30 or  altura > 2.70:
            print("[ERRO] Valor incoerente para altura!")
            return False
    except ValueError:
        print("[ERRO] A altura precisa ser um número")
        return False
    #cadastr0 no banco de dados
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?)",(val_nome, altura))
            print(F"Cadastro de {val_nome} adicionado com sucesso!")
            return True
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha no cadastro do banco: {erro}")
        return False
def listar_pessoas() -> bool:
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_pessoa_por_nome() -> bool:
    pass