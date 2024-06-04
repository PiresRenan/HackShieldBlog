# HackShield

HackShield é uma aplicação web desenvolvida em Flask, um microframework em Python, que utiliza o banco de dados SQLite para armazenar e gerenciar dados de usuários e postagens. Este projeto oferece uma plataforma simples e eficiente para a criação e gerenciamento de um blog, permitindo que os usuários registrem contas, façam login, criem, editem e excluam postagens, além de interagirem com as postagens por meio de comentários.

## Funcionalidades

- **Autenticação de Usuários**: Cadastro de novos usuários, login e logout.
- **Gerenciamento de Postagens**: Criação, edição e exclusão de postagens.
- **Interação de Usuários**: Comentários nas postagens, permitindo a interação entre usuários.
- **Perfil de Usuário**: Cada usuário possui um perfil onde pode visualizar suas postagens e informações pessoais.
- **Painel Administrativo**: Controle de conteúdo e usuários pelo administrador.

## Tecnologias Utilizadas

- **Flask**: Microframework para desenvolvimento web em Python.
- **SQLite**: Banco de dados relacional leve e fácil de usar.
- **Jinja2**: Template engine para renderização de páginas HTML.
- **WTForms**: Biblioteca para criação e validação de formulários.
- **Bootstrap**: Framework CSS para estilização responsiva e moderna.

## Pré-requisitos

- Python 3.x instalado no sistema.

## Passo a passo para configuração e execução

### 1. Clonar o repositório

Primeiramente, faça o clone deste repositório para o seu ambiente local:

``` sh
git clone https://github.com/PiresRenan/HackShieldBlog.git    
```

### 2. Criar um ambiente virtual
Crie um ambiente virtual Python:
``` sh
python3 -m venv venv
```

### 3. Ativar o ambiente virtual
Para ativar o ambiente virtual, execute o comando apropriado conforme o seu sistema operacional:

No Windows:
``` sh
venv\Scripts\activate
```
No macOS/Linux:
```sh
source venv/bin/activate
```

### 4. Instalar as dependências
Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:
```sh
pip install -r requirements.txt
```

### 5. Executar o programa
Finalmente, execute o arquivo main.py para iniciar o programa:
```sh
python app.py
```
### Contribuição
Para contribuir com este projeto, por favor siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
3. Faça as suas alterações.
4. Commit suas alterações (git commit -m 'Adiciona nova funcionalidade').
5. Envie para o branch (git push origin feature/nova-funcionalidade).
6. Abra um Pull Request.