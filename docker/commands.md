
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
docker run -d -p 8080:80 httpd 
docker run -d -i -t centos:centos7 /bin/bash
docker run  -d centos:centos7 /bin/bash
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

docker exec -i -t [container_id] /bin/bash

# docker inspect
docker inspect --format '{{ .NetworkSettings.IPAddress }}' $(docker ps -q)
docker inspect --format '{{.Config.Hostname}} {{ .NetworkSettings.IPAddress }}  {{ .NetworkSettings.Gateway }}' $(docker ps -q)

# os operation
hostname -i
cat /etc/os-release

# docker file
cd <Dockerfileが存在するディレクトリ>
docker build -t [Dockerfile_name]{:[tag_name]} .
docker images