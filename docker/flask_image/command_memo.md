

export dfname="python36:flask4"
export conname="flask002"

docker run -p 8081:8080 ${dfname}
docker run -d -p 8081:8080 ${dfname}
docker run -itd -p 8081:8080 ${dfname} /bin/bash
docker run -it -p 8081:8080 ${dfname} /bin/bash
docker run -it --net flask --name ${conname} ${dfname} /bin/bash
docker run -itd --net flask --name ${conname} ${dfname} /bin/bash

 --net flask --name ${conname} 


export conname="mysql"
export dfname="mysql:flask"
docker run -itd --net flask --name ${conname} ${dfname} /sbin/init



docker build -t ${dfname} -f dockerfile_python.df .
docker build -t ${dfname} -f dockerfile_mysql.df .


 yum install -y iproute
 ss -anp

