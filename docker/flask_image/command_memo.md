

export dfname="python36:flask2"
export conname="flask"

docker run -d -p 8081:8080 ${dfname}
docker run -itd -p 8081:8080 ${dfname} /bin/bash
docker run -it -p 8081:8080 ${dfname} /bin/bash

docker run -it --net flask --name ${conname} ${dfname} /bin/bash
docker run -itd -p 8081:8080 --net flask --name ${conname} ${dfname} /bin/bash

 --net flask --name ${conname} 

docker build -t ${dfname} -f dockerfile_python.df .


export sql_conname="mysql"
export sql_dfname="mysql:flask2"
docker build -t ${sql_dfname} -f dockerfile_mysql.df .
docker run -itd --privileged --net flask --name ${sql_conname} ${sql_dfname} /sbin/init





mysql --user=root --password=$(cat root_password.txt)

 yum install -y iproute
 ss -anp



docker run -itd --privileged baaff59b44a3 /sbin/init



cat /var/log/mysqld.log | grep 'temporary password' | awk '{print $11;}' > root_password.txt
mysql --user=root --password=$(cat root_password.txt)

create table rps.battle_history( \
    time timestamp, \
    id int, \
    name varchar(10), \
    choice_id int, \
    result varchar(10)  \
); \
alter table rps.battle_history add primary key (time,id);




RUN scp root@${ip_host}:/root/dockerfiles/001_python_tool/secret.txt /root/
