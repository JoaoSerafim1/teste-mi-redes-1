## 🐧 🐢 Comandos a serem executados em terminal do Linux-Ubuntu (sempre como "root", ou seja, modo "sudo")

```console
docker network create netid
```
###### (Cria rede de nome "netid" em modo "bridge")

```console
docker build -t python-socket-image .
```
###### (Compila a imagem com base na imagem padrao do python 3.9-slim)

```console
docker run -d -it --network=netid --name sid1 python-socket-image
```
```console
docker run -d -it --network=netid --name sid2 python-socket-image
```
###### (Instancia os containers em modo background e interativo)

```console
docker exec -it sid1 bash
```
###### ("Invade" o terminal do "servidor", a primeira parte que abre para comunicacao e espera informacao)
```console
python test-peer-1.py
```
###### (Executa a aplicacao correspondente, ja dentro do terminal)

### A seguir, abra um terminal separado para fazer o controle do outro container.

```console
docker exec -it sid2 bash
```
###### ("Invade" o terminal do "cliente", a parte que inicialmente manda informacao)
```console
python test-peer-2.py
```
###### (Executa a aplicacao correspondente, ja dentro do terminal)

## 🔧 📚 Paginas web consultadas para instalacao, solucao de problemas e aprendizado:
- **Instalacao:**
  - [_Install Docker Engine on Ubuntu_](https://docs.docker.com/engine/install/ubuntu)
- **Como resolver problemas ao executar o Docker**:
  - [_Cannot connect to the Docker daemon at unix:/var/run/docker.sock. Is the docker daemon running?_](https://stackoverflow.com/questions/44678725/cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker)
  - [_Is it possible to use docker without sudo?_](https://askubuntu.com/questions/1165877/is-it-possible-to-use-docker-without-sudo)
- **Tutoriais**:
  - [_Docker Containers: IPC using Sockets — Part 2_](https://medium.com/techanic/docker-containers-ipc-using-sockets-part-2-834e8ea00768)
  - [_How to get bash or ssh into a running container in background mode?_](https://askubuntu.com/questions/505506/how-to-get-bash-or-ssh-into-a-running-container-in-background-mode/543057#543057)
