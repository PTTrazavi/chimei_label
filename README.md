# chimei label website
## How to use Docker on 201
1. in the directory of Dockerfile
```bash
docker build . -t chimei_label
docker run -itd --rm --name chimei_label_web -v /home/jeremylai/docker_projects/chimei_label:/app/ -p 15009:15009 chimei_label

```
2. go into the running container bash  
```bash
docker exec -it [container ID] bash
```
3. start the django runserver
```bash
python3 manage.py runserver 0.0.0.0:15009
```
4. execute ngrok so user can connect this website outside VPN
```bash
ngrok http 15009
```
## the web will work on this URL
https://192.168.200.201:15009/  
https://xxxxxx.ngrok.io/  
