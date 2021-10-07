# Geralda Bot
Geralda é um bot para o aplicativo discord, a qual foi feita para disponibilizar as métricas de uma aplicação no 
discord, sendo que essas métricas estão salvas em um DB Postgresql.

Caso trabalhe com Postgresql e o discord, sinta-se a vontade em clonar o projeto e utiliza-lo para sua aplicação, assim
como fazer as modificações que julgar pertinente. A seguir esta descrito alguns exemplos e como instalar/subir a Geralda.

## Build
A Geralda segue o básico da estrutura de um bot do discord, então inicialmente eu recomendo que você leia esse 
[tutorial](https://realpython.com/how-to-make-a-discord-bot-python/).

Com o conhecimento do tutorial em mente e considerando que vc já tenha um DB Postgresql em funcionamento. 
Geralda irá precisar definir algumas variáveis de ambiente, as quais estão descritas
no arquivo [system_variables](https://github.com/pedrohrf/geralda-bot/blob/main/src/enums/system_variables.py).

Após a definição das variáveis de ambiente será necessário [instalar o Python 3](https://www.python.org/downloads/).
Feito a instalação, podemos utilizar o pip para instalar as dependências do projeto:
```
pip install -r requirements.txt
```

Ps: Pode ser que algumas dependências necessitem da instalação de alguns pacotes dependendo do seu SO.

Por fim basta executar:
```
python geralda.py
```

## Utilização com o docker

O projeto possui um Dockerfile, que é usado para criar imagens docker e utilizar em diversos ambientes. Por padrão, a versão do Python utilizado no build é o Python3:latest, no entanto é possível passar um parâmetro (*PYTHON_IMAGE_VERSION*) ao iniciar o processo de build dessa imagem, através do comando:

```sh
docker build -t container-name . --build-arg PYTHON_IMAGE_VERSION=python:3.8
```

> Ps: Ao omitir o parametro PYTHON_IMAGE_VERSION na linha de comando, a versão 3 (latest) será utilizada, pegando a versão mais recente.
