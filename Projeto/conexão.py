from PyQt5 import uic, QtWidgets
import MySQLdb


def conectar():
    """
    Função para conectar no servidor
    """
    conn = MySQLdb.connect(
    db='cadastro',
    host='localhost',
    user='root',
    passwd='root'         
    )
    return conn


# Primeira tela
def chama_primeira_tela():
    primeira_tela.label_4.setText('')
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    primeira_tela.close()
    quarta_tela.show()
    

def chama_segunda_tela():
 
    nome = str(segunda_tela.lineEdit.text())
    sobrenome = str(segunda_tela.lineEdit_2.text())
    email = str(segunda_tela.lineEdit_3.text())
    senha = str(segunda_tela.lineEdit_4.text())
    primeira_tela.close()
    segunda_tela.show() # Clicando o botao vai mostrar a segunda tela
    
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute(f"INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('{nome}', '{sobrenome}', '{email}', '{senha}')")
    conn.commit()

    if cursor.rowcount == 1:
        print('Inserido com sucesso')
    else:
        print('Não foi possivel inserir')

    
def chama_terceira_tela():
    segunda_tela.close()
    terceira_tela.show() 


def chama_quarta_tela():
    primeira_tela.close()
    quarta_tela.show()

def logout():
    terceira_tela.close()
    primeira_tela.show()

# Importando os arquivos
app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi('primeira_tela.ui')
segunda_tela=uic.loadUi('segunda_tela.ui')
terceira_tela=uic.loadUi('terceira_tela.ui')
quarta_tela=uic.loadUi('quarta_tela.ui')

# Botoes
primeira_tela.pushButton.clicked.connect(chama_primeira_tela) 
primeira_tela.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(chama_terceira_tela)
terceira_tela.pushButton.clicked.connect(logout)
primeira_tela.pushButton.clicked.connect(chama_quarta_tela)

# Mostrando e fazendo executar a tela
primeira_tela.show()
app.exec()
