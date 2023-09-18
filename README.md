# Buster

Projeto backend de uma plataforma de filmes.

O desafio é:

*"Você foi selecionado pelo gestor da sua empresa para desenvolver uma API com o intuito de fazer uma gestão de vendas de filmes que está querendo sair do papel e caneta e planilhas bagunçadas. Nesse projeto você criará uma aplicação para gerenciar usuários, filmes e compras, incluindo autenticação e permissões de rotas para diferentes tipos de usuário."*



## Stack utilizada

Para o estudo foram escolhidas as tecnologias:

**Back-end:** Python, Django, PostgreSQL.

**Testes:** Pytest.

**Ambiente:** Venv.
## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:agnes-lica/Buster-Python.git
```

Entre no diretório do projeto

```bash
  cd KImoveis
```

Inicie o servidor

```bash
# linux:
  source venv/bin/activate

# windows:
  .\venv\Scripts\activate 
```

Instale as dependências

```bash
  pip install -r requirements. txt
```

## Rodando os testes

#### Rodar todos os testes
```bash
 pytest --testdox -vvs
```

#### Rodar testes por tarefas

##### Tarefa 1
```bash
 pytest --testdox -vvs tests/tarefas/t1/
```

##### Tarefa 2
```bash 
 pytest --testdox -vvs tests/tarefas/t2/
```

##### Tarefa 3
```bash 
 pytest --testdox -vvs tests/tarefas/t3/
```

##### Tarefa 4
```bash
 pytest --testdox -vvs tests/tarefas/t4/
```

## Documentação da API

#### Endpoints

| Método   | Endpoint       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `POST`      | `/api/users/` | Criação de usuário|
| `POST`      | `/api/users/login/` | Autenticação do usuário |
| `GET`      | `/api/users/<int:user_id>/` | Busca de usuário por id |
| `PATCH`      | `/api/users/<int:user_id>/` | Atualizar usuário |
| `POST`      | `/api/movies/` | Criação de filme |
| `GET`      | `/api/movies/` | Listagem de filme |
| `GET`      | `/api/movies/<int:movie_id>/` | Busca de filme por id |
| `DELETE`      | `/api/movies/<int:movie_id>/` | Deleção de filme |
| `POST`      | `/api/movies/<int:movie_id>/orders/` | Criação de pedido |


## Contato

Para entrar em contato comigo me mande um e-mail ou uma mensagem nas redes sociais:

- [github](https://www.github.com/agnes-lica)
- [LinkedIn](https://www.linkedin.com/in/agnesmr/)
- E-mail: agnes.lica@gmail.com
