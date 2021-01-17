

export dfname="python36:flask4"
export conname="flask002"

docker run -p 8081:8080 ${dfname}
docker run -d -p 8081:8080 ${dfname}
docker run -itd -p 8081:8080 ${dfname} /bin/bash
docker run -it -p 8081:8080 ${dfname} /bin/bash
docker run -it --net flask --name ${conname} ${dfname} /bin/bash
docker run -itd --net flask --name ${conname} ${dfname} /bin/bash

 --net flask --name ${conname} 

docker build -t ${dfname} -f dockerfile_python.df .


export sql_conname="mysql"
export sql_dfname="mysql:flask-base"
docker build -t ${sql_dfname} -f dockerfile_mysql.df .
docker run -itd --privileged --net flask --name ${sql_conname} ${sql_dfname} /sbin/init





mysql --user=root --password=$(cat root_password.txt)

 yum install -y iproute
 ss -anp

