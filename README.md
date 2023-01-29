# Desafio Back End Cnab
Sua aplicação web DEVE:

Ter uma tela (via um formulário) para fazer o upload do arquivo.

Interpretar ("parsear") o arquivo recebido, normalizar os dados e salvar corretamente a informação em um banco de dados relacional. Preste atenção nas documentações que estão logo abaixo.

Exibir uma lista das operações importadas por lojas, sendo que essa lista deve conter um totalizador do saldo em conta por loja.

Ser escrita obrigatoriamente em Python 3.0+.

Ser simples de configurar e rodar, de preferência dockerizado e funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.


# Passos para incialização:

Preencher o .env com seus dados locais.

Rodar o docker "docker compose up".

Rodar as migrações "python manage.py migrate".

Usar a url http://localhost:8000/.
