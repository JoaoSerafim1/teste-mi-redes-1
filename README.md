Comandos a serem rodados (sempre como sudo)

#Cria rede de nome "netid" em modo "bridge"
docker network create netid

#Compila a imagem com base na imagem padrao do python 3.9-slim
docker build -t python-socket-image .

#Instancia os containers em modo background e interativo
docker run -d -it --network=netid --name sid1 python-socket-image
docker run -d -it --network=netid --name sid2 python-socket-image

#"Invade" o terminal do "servidor" (primeira parte que abre para comunicacao e espera) e executa a aplicacao correspondente, ja dentro do terminal
docker exec -it sid1 bash
python test-peer-1.py

A seguir, abra um terminal separado para fazer o controle do outro container

#"Invade" o terminal do "cliente" (parte que inicialmente manda informacao) e executa a aplicacao correspondente, ja dentro do terminal
docker exec -it sid2 bash
python test-peer-2.py