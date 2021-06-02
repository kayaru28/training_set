
alias dpq='docker ps -a -q'
sysctl -w vm.max_map_count=262144

grep -H "" /etc/*version ; grep -H "" /etc/*release
docker stats

fluentd         :alpine
kibana          :centos 8
elasticsearch   :centos 8

# trouble shoot

docker commit { コンテナID } { コンテナ名を適当に付ける }
docker run --rm -it { 適当につけたコンテナ名 } sh


# docker compose
docker-compose up -d
docker-compose down

# df for flask app
export flask_ver="1.0"
export dfname="python36:flask${flask_ver}"
export conname="flask"

docker run -itd -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro  -p 8081:8080 --net flask --name ${conname} ${dfname}

docker build -t ${dfname} -f dockerfile_python.df .
docker build -t python36:flask -f dockerfile_python.df .


## test
docker run -it -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --net flask ${dfname}
http://10.255.255.1:8081/rpsapi?name=kayaru&value=0

docker build -t test:flask -f dockerfile_test_flask.df .


docker run -it -v /root/dockerfiles/001_python_tool/setup:/root/setup:ro --net test_backend test:flask


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

# df for fluentd
docker build -t fluentd:flask -f dockerfile_fluentd.df .

docker  exec -it fluentd sh
curl -X POST -d 'json={"json":"message"}' http://fluentd:24280/debug.test
curl -X POST -F upfile=@/test_cron.log http://fluentd:24280/debug_test
apk add openssh

# df for haproxy
docker build -t haproxy:flask -f dockerfile_haproxy.df .



# elasticsearch
docker build -t elasticsearch:flask -f dockerfile_elasticsearch.df .

docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.0
sysctl -w vm.max_map_count=262144
## commands
### cluster health check
curl -X GET "localhost:9200/_cat/health?v&pretty"
curl localhost:9200/_cluster/health?pretty=true
curl localhost:9200/_cat/nodes
curl http://localhost:9200/_cat/nodes?v #cluster check

### index check
curl localhost:9200/_aliases?pretty
curl localhost:9200/_cat/count/{index}

### cluster health check

curl -X POST "localhost:9200/my_index/my_doctype/" -H "Content-Type:application/json" -d '{"name":"taro","state":"test"}'
curl -X POST "localhost:9200/my_index/my_doctype/" -H "Content-Type:application/json" -d '{"name":"jiro","state":"test","crea":"test2"}'
curl -X GET "localhost:9200/my_index/my_doctype/qqmMongBOsh592scjhGS/_source?pretty"

## reference
https://qiita.com/ryurock/items/b9c51435bcc617d7c6be

# kibana
docker build -t kibana:flask -f dockerfile_kibana.df .



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





