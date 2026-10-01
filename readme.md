# API de Sistema de Biblioteca 📚

Este projeto foi desenvolvido como atividade de encerramento da Unidade 1 da disciplina. Consiste numa API REST completa para a gestão de empréstimos de livros numa biblioteca, desenvolvida com **Django**, **Django REST Framework (DRF)** e autenticação via **JSON Web Tokens (JWT)**.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Django**
* **Django REST Framework (DRF)**
* **djangorestframework-simplejwt** (Autenticação JWT)

---

## ⚙️ Instruções de Instalação e Execução

### 1. Clonar o repositório
```bash
git clone <LINK_DO_SEU_REPOSITORIO_GIT>
cd biblioteca

### 2. Crtiar e ativar o ambiente virtual
windows (PwerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

Linux / macOS:
Bash
python3 -m venv venv
source venv/bin/activate

##3. Instalar as dependências do projeto
Bash
pip install -r requirements.txt

##4. Aplicar as migrações da base de dados
Bash
python manage.py migrate

##5. Criar o superutilizador (Administrador)
Bash
python manage.py createsuperuser

##6. Executar o servidor de desenvolvimento
Bash
python manage.py runserver

A API ficará disponível em: http://127.0.0.1:8000/api/

Lista de Endpoints Disponíveis

Autenticação (JWT)
POST /api/token/ - Obtém os tokens de Acesso (access) e Atualização (refresh) [Acesso Público]
{
  "username": "admin",
  "password": "sua_senha"
}

POST /api/token/refresh/ - Renova o token de acesso expirado [Acesso Público]
{
  "refresh": "COLE_O_REFRESH_TOKEN_AQUI"
}

Autores
GET /api/autores/ - Lista todos os autores cadastrados [Acesso Público]
POST /api/autores/ - Cadastra um novo autor [Acesso Público]
{
  "nome": "Machado de Assis"
}
GET /api/autores/{id}/ - Detalha as informações de um autor específico [Acesso Público]
PUT /api/autores/{id}/ - Atualiza todos os dados de um autor [Acesso Público]
{
  "nome": "Joaquim Maria Machado de Assis"
}
DELETE /api/autores/{id}/ - Remove um autor do sistema [Acesso Público]
GET /api/autores/com_total_livros/ - [Agregação] Lista os autores com a contagem total de livros associados [Acesso Público]

Categorias
GET /api/categorias/ - Lista todas as categorias de livros [Acesso Público]
POST /api/categorias/ - Cria uma nova categoria [Acesso Público]
{
  "nome": "Ficção Científica"
}
PUT /api/categorias/{id}/ - Atualiza uma categoria
{
  "nome": "Ficção Científica e Fantasia"
}
DELETE /api/categorias/{id}/ - Deleta uma categoria

Livros
GET /api/livros/ - Lista os livros cadastrados exibindo os detalhes do autor aninhado [Acesso Público]
POST /api/livros/ - Cadastra um novo livro [Acesso Público]
{
  "titulo": "Dom Casmurro",
  "autor": 1,
  "categorias": [1]
}

GET /api/livros/disponiveis/ - [Manager Customizado] Retorna apenas os livros com disponibilidade ativa [Acesso Público]
PUT /api/livros/{id}/
{
  "titulo": "Dom Casmurro - Edição Especial",
  "autor": 1,
  "categorias": [1]
}
GET /api/livros/disponiveis/ - [Manager Customizado] Retorna apenas livros com disponibilidade ativa

Perfil do Leitor
GET /api/leitores/ - Lista os perfis de leitores
POST /api/leitores/ - Cadastra um novo perfil de leitor
{
  "user": 1,
  "telefone": "(11) 99999-9999",
  "endereco": "Rua das Flores, 123"
}
PUT /api/leitores/{id}/ - Atualiza as informações do perfil do leitor
{
  "user": 1,
  "telefone": "(11) 98888-8888",
  "endereco": "Avenida Central, 456"
}
DELETE /api/leitores/{id}/ - Remove o perfil do leitor

Empréstimos
GET /api/emprestimos/ - Lista todos os empréstimos registrados [Requer Autenticação JWT]
POST /api/emprestimos/ - Registra um novo empréstimo de livro e aciona o Signal para desativar a disponibilidade do item [Requer Autenticação JWT]
{
  "livro": 1,
  "leitor": 1
}
DELETE /api/emprestimos/{id}/ - Cancela/Exclui o registro de um empréstimo


📸 Evidências e Testes da API
Para conferir os prints das validações de autenticação JWT, tratamento de acessos negados (401 Unauthorized) e requisições autorizadas (200 OK), consulte o documento de evidências localizado na raiz do projeto:
