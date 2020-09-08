# Importando bibliotecas 
from PyQt5 import uic, QtWidgets
import MySQLdb

# Conectando ao banco de dados
try:
    banco = MySQLdb.connect(
        db='usuariopy',
        host='localhost',
        user='root',
        passwd='root' )
except:
    print("Não foi possível se-conectar com o banco de dados...")


# Tela de login
def chama_primeira_tela():
    login = str(primeira_tela.lineEdit.text())
    senha = str(primeira_tela.lineEdit_2.text())
    cursor = banco.cursor()
    # Verificando se o login e senha estão corretos conforme o cadastro feito
    comando_sql = (f"SELECT * FROM usuarios WHERE login= '{login}' and senha='{senha}';")
    cursor.execute(comando_sql)
    resultado = cursor.fetchall()
    # Caso a linha com dados for encontrada, mostra a pagina final.
    if len(resultado) > 0:
        primeira_tela.close()
        quarta_tela.show()
    else:
        primeira_tela.label_4.setText('Incorrect login or password!')

# Chamando a tela de cadastro
def chama_segunda_tela():
    primeira_tela.close()
    segunda_tela.show()

# Chamadno a terceira tela caso o botão de cadastro for clicado
def chama_terceira_tela():
    nome = str(segunda_tela.lineEdit.text()).strip()
    login = str(segunda_tela.lineEdit_2.text()).strip()
    senha = str(segunda_tela.lineEdit_3.text()).strip()
    repetir_senha = str(segunda_tela.lineEdit_4.text()).strip()
    # Inserindo os dados digitados no banco
    if senha == repetir_senha:          
        try:
            cursor = banco.cursor()
            comando_sql = (f"INSERT INTO usuarios (nome, login, senha) VALUES ('{nome}', '{login}', '{senha}')")
            cursor.execute(comando_sql)
            banco.commit() 
            segunda_tela.close()
            terceira_tela.show()     
        except:
            print('Não foi possivel inserir os dados')
    else:
        segunda_tela.label_2.setText('Passwords do not match!')

        
# Voltando para tela inicial caso o botão de logout por clicado
def logout():
    terceira_tela.close()
    primeira_tela.show()

# Conectando a aplicação
app=QtWidgets.QApplication([])
# Carregando os arquivos
primeira_tela=uic.loadUi('primeira_tela.ui')
segunda_tela=uic.loadUi('segunda_tela.ui')
terceira_tela=uic.loadUi('terceira_tela.ui')
quarta_tela=uic.loadUi('quarta_tela.ui')
# Botões de cada pagina que por fim, chama as funções 
primeira_tela.pushButton_2.clicked.connect(chama_segunda_tela)
primeira_tela.pushButton.clicked.connect(chama_primeira_tela)
segunda_tela.pushButton.clicked.connect(chama_terceira_tela)
terceira_tela.pushButton.clicked.connect(logout)
# Colocando mascaras nas senhas
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
segunda_tela.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
segunda_tela.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
# Mostrando a tela inicial
primeira_tela.show()
# Executando a aplicação
app.exec()