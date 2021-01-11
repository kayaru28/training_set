
docker run -i -t -d -p 8081:8080 ${dfname} /bin/bash
docker run -i -t -p 8081:8080 ${dfname} /bin/bash

export dfname="python36:flask2"
docker run -p 8081:8080 ${dfname}
docker run -d -p 8081:8080 ${dfname}

docker build -t ${dfname} -f dockerfile_python.df .


 yum install -y iproute
 ss -anp

