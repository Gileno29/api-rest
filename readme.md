# Rest API with Django Rest Framework

- Projeto de API Rest Full em Django com Rest Full Framework. Foi criado uma mini apliação de estoque apenas para simular dados reais que podem ser inseridos via interface gráfica, mas para quem preferir tem um script para polpulação do database no projeto.

------------------------------- English Version -------------------------------

- Full Rest API project in Django with Rest Full Framework. A mini inventory application has been created only to simulate real data that can be entered via graphical interface, but for those who prefer have a script for polpulação of the database in the project.

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
## 🛠️ Construído com
* [Docker](https://docs.docker.com/) - Para conteinerização
* [Django](https://docs.djangoproject.com/en/4.1/) - Framework Backend
* [Booststrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Framework Frontend






## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

