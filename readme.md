# Rest API with Django Rest Framework

- Projeto de API Rest Full em Django com Rest Full Framework. Foi criado uma mini apliação de estoque apenas para simular dados reais que podem ser inseridos via interface gráfica, mas para quem preferir tem um script para polpulação do database no projeto.


## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

- Docker
- Ambiente Linux

### 🔧 Configuração Docker (ambiente ubuntu 22.04)
se você já tem containers rodando na sua máquina pule  a instalação do docker pois isso vai remover seu docker atual.
```
  sudo apt-get remove docker docker-engine docker.io containerd runc
```
```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

```
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```
sudo docker run hello-world
```
 Documentação oficial do  [Docker](https://docs.docker.com/engine/install/ubuntu/) 

## 📦 Rodando a aplicação

 para rodar a aplicação basta usar usar o docker compose:
``` 
docker compose up -d --build
```


 Se você quiser rodar sem o docker, vai ser necessario instalar o postgres em seu ambiente local e alám das libs que estão no requeriments.txt
 end points da api:
```
"estoque-api": "http://localhost:8000/api/v1/estoque-api",
"estoque-api/itens": "http://localhost:8000/api/v1/estoque-api/itens"
```
 O APP disponibiliza um CRUD para cadastro dos dados caso precise, ou pode usar o sql com dados para inserir direto no banco.
 
 - Data Base: estoque
 - Usuario: api

 para acessar o banco use:
 ```
 docker container exec -it <container_id> /bin/bash 

 su postgres 
 
 psql -U api

 ```
 e já pode executar seus scrits.


## 🛠️ Construído com
* [Docker](https://docs.docker.com/) - Para conteinerização
* [Django](https://docs.djangoproject.com/en/4.1/) - Framework Backend
* [Booststrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Framework Frontend
