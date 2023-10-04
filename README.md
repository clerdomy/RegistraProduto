# RegistraProduto

Foi criado um API de gerenciamento de produtos utilizando Django, um robusto framework web em Python que facilita a criação de aplicações web. A estrutura do backend foi aprimorada ainda mais com a integração do Django REST Framework (DRF)

A arquitetura da aplicação aproveita os recursos do Django para criar modelos de dados eficientes, com um banco de dados que armazena informações sobre os produtos (sqlite), incluindo nome, valor, disponibilidade e descrição.

A API RESTful é construída com o Django REST Framework, permitindo operações CRUD (Create, Read, Update, Delete) para interagir com os dados dos produtos. Isso inclui a capacidade de cadastrar novos produtos, listar produtos existentes, e atualizar ou excluir informações específicas. 


## Pré-requisitos

Certifique-se de ter Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/clerdomy/RegistraProduto.git

2. Vai na pasta 
   cd RegistraProduto

3. Criar um venv
   python -m venv venv

4. SO Windows
    .\venv\Scripts\activate

5. instalação dos requisitos
    pip install -r requirements.txt

6. crie a tabela
    python manage.py migrate cadastro

7. Inicie o servidor de desenvolvimento:
    python manage.py runserver

O aplicativo estará disponível em http://localhost:8000/cadastro/
    



