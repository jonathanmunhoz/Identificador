from imap_tools import MailBox, AND, OR
import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_campo', user='root', password='root')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)

print("__________________________________________________________")
print("Observações:")
print("1) Para garantir o funcionamento do software, é necessário desativar a segurança do seu E-mail.")
print("2) Textos longos não serão armazenados em nosso banco de dados.")
print("__________________________________________________________")

# pegar emails de um remetente para um destinatário
username = input("Digite seu E-mail: ")
password = input("Digite sua senha: ")
print("\n______________________________________")

# lista de imaps: https://www.systoolsgroup.com/imap/
meu_email = MailBox('imap.gmail.com').login(username, password)

# criterios: https://github.com/ikvk/imap_tools#search-criteria
lista_emails = meu_email.fetch(OR(subject=input("Buscar assunto: " ), text=input("Buscar texto: ")))
for email in lista_emails:
    print("Remetente: ", email.from_)
    print("Assunto: ", email.subject)
    print("Mensagem: ", email.text)
    print("Hora: ", email.date_str, "\n______________________________________")
    alterar_dados = "INSERT INTO tb_campo (data, origem, assunto) VALUES ('" + email.date_str + "', '" + email.from_ + "','" + email.subject + "')";
    cursor.execute(alterar_dados)
    con.commit()

print("\nAcima estão todos os e-mails localizados com a palavra-chave.")

input("\nDigite qualquer tecla para encerrar o sistema e de um enter: ")
