# trouble shoot

docker commit { コンテナID } { コンテナ名を適当に付ける }

docker run --rm -it { 適当につけたコンテナ名 } sh


# docker compose
docker-compose up -d

# df for flask app
export flask_ver="1.0"
export dfname="python36:flask${flask_ver}"
export conname="flask"

docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro  -p 8081:8080 --net flask --name ${conname} ${dfname}

docker build -t ${dfname} -f dockerfile_python.df .


## test
docker run -it -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --net flask ${dfname}
http://10.255.255.1:8081/rpsapi?name=kayaru&value=0

docker build -t test:flask -f dockerfile_test_flask.df .


docker run -it -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --net flask test:flask


# df for sql
export sql_ver=
export sql_conname="mysql${sql_ver}"
export sql_dfname="mysql:flask${sql_ver}"
export root_pass=$(cat $PWD/setup/secret.txt | grep root_pass | awk '{print $1}')

docker run -d -v "$PWD/setup/mysql_setup:/docker-entrypoint-initdb.d" -e MYSQL_ROOT_PASSWORD=${root_pass} --net flask --name ${sql_conname} ${sql_dfname}

docker build -t ${sql_dfname} -f dockerfile_mysql.df .

# df for logstash
export logstash_ver=""
export logstash_conname="logstash${logstash_ver}"
export logstash_dfname="logstash:flask${logstash_ver}"

docker build -t ${logstash_dfname} -f dockerfile_logstash.df .

docker run -d -v /root/dockerfiles/001_python_tool/setup:/setup:ro --net flask --name ${logstash_conname} ${logstash_dfname}

## for test
docker run -it -v /root/dockerfiles/001_python_tool/setup:/setup:ro --net flask ${logstash_dfname}

docker run -it -e XPACK_MONITORING_ENABLED=false docker.elastic.co/logstash/logsta
sh:6.8.2



# df for sql Legacy
export sql_ver=8
export sql_conname="mysql${sql_ver}"
export sql_dfname="mysql:flask${sql_ver}"
docker build -t ${sql_dfname} -f dockerfile_mysql.df .
docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --privileged --net flask --name ${sql_conname} ${sql_dfname}

docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --privileged --net flask --name ${sql_conname} ${sql_dfname} /sbin/init

# SQL root
mysql --user=root --password=$root_password
SET PASSWORD FOR root = PASSWORD('******');
ALTER USER root@localhost IDENTIFIED BY '******';

 yum install -y iproute
 ss -anp

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





