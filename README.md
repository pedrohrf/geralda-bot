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

## Exemplos de Uso

