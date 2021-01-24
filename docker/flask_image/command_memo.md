

export dfname="python36:flask2"
export conname="flask"
docker build -t ${dfname} -f dockerfile_python.df .
docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro  -p 8081:8080 --net flask --name ${conname} ${dfname} /bin/bash


docker run -d -p 8081:8080 ${dfname}
docker run -itd -p 8081:8080 ${dfname} /bin/bash
docker run -it -p 8081:8080 ${dfname} /bin/bash

docker run -it --net flask --name ${conname} ${dfname} /bin/bash
docker run -itd -p 8081:8080 --net flask --name ${conname} ${dfname} /bin/bash

 --net flask --name ${conname} 

# df for sql
export sql_ver=8
export sql_conname="mysql${sql_ver}"
export sql_dfname="mysql:flask${sql_ver}"
docker build -t ${sql_dfname} -f dockerfile_mysql.df .
docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --privileged --net flask --name ${sql_conname} ${sql_dfname}

docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --privileged --net flask --name ${sql_conname} ${sql_dfname} /sbin/init




mysql --user=root --password=$root_password
SET PASSWORD FOR root = PASSWORD('Root090401');
ALTER USER root@localhost IDENTIFIED BY 'Root-0904';
ALTER USER root@localhost IDENTIFIED BY 'root-0904';

 yum install -y iproute
 ss -anp



docker run -itd --privileged baaff59b44a3 /sbin/init




export mysql_password=$(cat /var/log/mysqld.log | grep pass | awk '{print $11}' )
mysql --user=root --password=$mysql_password

create database mydb; 
mysql --user=root --password=$root_password --connect-expired-password -e "ALTER USER root@localhost IDENTIFIED BY $root_password;" 

mysql --user=root --password=$root_password --connect-expired-password -e "create database mydb;" 



create table rps.battle_history( \
    time timestamp, \
    id int, \
    name varchar(10), \
    choice_id int, \
    result varchar(10)  \
); \
alter table rps.battle_history add primary key (time,id);




RUN scp root@${ip_host}:/root/dockerfiles/001_python_tool/secret.txt /root/

source setup_rps_mysql.sh





