
# network
nmcli d
nmtui


# docker install
yum -y update

yum install -y curl
curl -fsSL https://get.docker.com/ | sh
systemctl status docker
systemctl start docker
usermod -aG docker $USER

chkconfig docker on

# docker image
docker pull [image-_name]

# actibate
docker run -i -t centos:centos7 /bin/bash
docker run -p 8080:80 httpd 
docker run -i -t -d -p 8080:80 httpd  /bin/bash
docker run -d -i -t centos:centos7 /bin/bash
docker run  -d centos:centos7 /bin/bash
 --net mybridge --name alpine3 

# background
docker run --detach nginx
docker attach

docker stop eloquent_swan

--name [name]
-e [env]=[val]
-d <---backgroud 

# status check
docker images
docker ps
docker ps -a
docker ps -q


# docker operation 
Ctrl+P Ctrl+Q
docker commit [container_id] [image_name]
docker kill [container_id]
... docker kill $(docker ps -a)
docker rm [container_id]
... docker rm $(docker ps -a -q)
... docker -f rm $(docker ps -a -q) <--- include running container

docker rmi [imageid]

docker exec -i -t [container_id] /bin/bash

# docker inspect
docker inspect --format '{{ .NetworkSettings.IPAddress }}' $(docker ps -q)
docker inspect --format '{{.Config.Hostname}} {{ .NetworkSettings.IPAddress }}  {{ .NetworkSettings.Gateway }}' $(docker ps -q)

# docker network
docker network create --driver=bridge network-name





# os operation
hostname -i
cat /etc/os-release

## Ubuntu系
apt-get update
apt-get install vim

## Centos系
yum install vim

## Alpine
apk update
apk add vim

# docker file
cd <Dockerfileが存在するディレクトリ>
docker build -t [image_name]{:[tag_name]} -f  [dockerfilename] .
docker images

docker build -t python36:flask -f dockerfile_python.df .

