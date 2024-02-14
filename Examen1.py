import tkinter as tk
import ply.lex as lex

palabras_reservadas = ['public', 'static', 'void', 'int', 'printf','programa','end','read']

tokens = ['PALABRA_RESERVADA', 'IDENTIFICADOR', 'DELIMITADOR', 'OPERADOR', 'NUMERO'] + [word.upper() for word in palabras_reservadas]

t_DELIMITADOR = r'[(){};."",]'
t_OPERADOR = r'[=+]'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in palabras_reservadas:
        t.type = 'PALABRA_RESERVADA'
    else:
        t.type = 'IDENTIFICADOR'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter no válido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    lexer.input(codigo)

    token_totales = []
    for tok in lexer:
        token_totales.append((tok.lineno, tok.value, tok.type))

    resultado_texto.delete("1.0", tk.END)
    for numero_linea, token, tipo in token_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n{tipo.capitalize()} {token}\n")

ventana = tk.Tk()
ventana.geometry("500x580")
ventana.title("Analizador Léxico")
ventana.config(bg="#12657f")

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=60, y=40)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#121b29", fg="white", command=analizar_codigo)
boton_analizar.place(x=60, y=240)

resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
resultado_texto.place(x=60, y=300)

entrada_texto.insert(tk.END, "programa suma(){\n     int  a,b,c;\n     int  a,b,c;\n     read a;\n     read b\n     c=a+b;\nprintf (\"la suma es\")\n  end;\n}")

ventana.mainloop()
