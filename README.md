# Exercicio 2 da Qipu

Objetivo: Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada, assim como a existência de cartas disponíveis e horários de nascer e pôr do sol. No Brasil, estas informações são disponibilizadas pelo site https://www.aisweb.aer.mil.br/. Nesta página é possível encontrar links para cartas, horarios do sol e as informações de TAF e METAR, que são boletins meteorológicos codificados.

Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) e imprima na tela:

- As cartas disponíveis
- Os horários de nascer e pôr do sol de hoje
-A informação de TAF e METAR disponíveis


Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.

## Pré-requisitos

- [Python](https://www.python.org/)

## Como rodar


```bash
# Primeiramente clone o projeto com
$ git clone https://github.com/joaovs2004/Exercicio02-Qipu.git
# Entre na pasta do projeto
$ cd Exercicio02-Qipu/
# Instale as dependencias com
$ pip install -r requirements.txt
# Rode o projeto com
$ python main.py
```