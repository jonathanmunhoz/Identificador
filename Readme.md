Projeto:
Este é um sistema que acessa sua conta de email Gmail e além de identificar os emails que contenham as palavras "DevOps", tanto
no assunto quanto no corpo do email, salva as informações dos campos: data, origem e assunto em um banco de dados criado em MySql
Server.
_______________________________________________________________________________________________________________________________
Tecnologias utilizadas:
Python - Linguagem de Programação

MySQL Server - Banco de dados

Mysql.connector - Biblioteca para integração do Banco de Dados

From imap_tools import MailBox, AND, OR - Faz a importação da caixa de mensagens de um email do Gmail
_______________________________________________________________________________________________________________________________
Requisitos:

Ter instalado uma versão recente do Python (Durante o desenvolvimento foi utilizado a versão PyCharm 2021 3.2)

Criar um banco de dados com as informações necessárias, ou utilizar o IP de um computador que esteja configurado corretamente.

Desativar configurações de segurança do seu email do Gmail.
_______________________________________________________________________________________________________________________________
Desenvolvimento do Projeto:

De início, fazemos a conexão com o banco de dados, para que os dados desejados, inseridos pelo usuário, sejam salvos.
E caso a conexão seja bem-sucedida, o sistema irá exibir a mensagem "Conectado ao banco de dados, nome do banco"

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/SRnFcYsR/img1.png" alt="img1"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
O sistema irá exibir algumas mensagens de alerta para o usuário.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/9Q55qMjX/img2.png" alt="img2"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Em seguida, é solicitado que o usuário informe o seu email e senha do Gmail, para realizar o login.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/qBFd4wb3/img3.png" alt="img3"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Após o login do usuário, o comando abaixo é necessário para validar o email do usuário, de acordo com as informações inseridas.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/j2BVcqwX/img4.png" alt="img4"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Para a pesquisa pela palavra-chave desejada, que é "DevOps", o sistema irá validar para o email, se dentro da lista_emails
há algo relacionado a esta busca, e irá escrever na tela o remetente, assunto, mensagem e a hora em que foi enviada a mensagem.
Nesta versão, eu permito que o usuário pesquise pela palavra-chave que desejar.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/BQQ5J5z2/img5.png" alt="img5"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
E para que os dados desejados, sejam salvos no banco de dados, fazemos a execução de um insert na tabela desejada, com as
informações inseridas pelo usuário.

<a href="https://postimg.cc/JsWDwWyV" target="_blank"><img src="https://i.postimg.cc/MpnyQ6qT/img6.png" alt="img6"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Para sair do sistema, é necessário digitar qualquer tecla e apertar o enter.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/KvqPjkXw/img7.png" alt="img7"/></a><br/><br/>

