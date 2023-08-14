# Codeleap

O Codeleap é um projeto de API construído com Django e Django Rest Framework. Essa API permite a criação, leitura, atualização e exclusão de posts.

## Tecnologias Utilizadas

- Python
- Django
- Django Rest Framework

## Como Utilizar

Siga as instruções abaixo para configurar e executar o projeto localmente:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode verificar a versão do Python digitando o seguinte comando no terminal:

`python --version`

2. Se o Python não estiver instalado, você pode baixá-lo em https://www.python.org/downloads/.

`git clone https://github.com/luckraw/codeleap.git`

3. Navegue até o diretório do projeto:

`cd codeleap`

4. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv env
source env/bin/activate
```


5. Execute as migrações do Django:

```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

- Agora você pode acessar a API em `http://localhost:8000/careers/` e usar as seguintes rotas:

`GET /careers/` : Retorna uma lista de todos os posts.

`POST /careers/` : Cria um novo post.

`GET /careers/{post_id}/` : Retorna os detalhes de um post específico.

`PATCH /careers/{post_id}/` : Atualiza um post existente.

`DELETE /careers/{post_id}/` : Exclui um post existente.

**Certifique-se de substituir** `{post_id}` pelo **ID real** do post que você deseja buscar, atualizar ou excluir.

