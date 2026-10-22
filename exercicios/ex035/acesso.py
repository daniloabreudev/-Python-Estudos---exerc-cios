import sqlite3
busca  = input("Quem você está ptocurando?").strip()

try:
    with sqlite3.connect('meubanco1.db') as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        for amigo in cur:
            if not amigo['nome'] or not amigo['nome'].strip():
                print(f"VAZIO!")
            else:
                print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")

except sqlite3.Error as e:
    print(f"Falha no banco: {e}")
except Exception as e:
    print(f"Ago deu errado: {e}")

