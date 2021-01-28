
/sbin/init

echo "env setting"
export mysql_password=$(cat 
 | grep pass | grep temporary | awk '{print $11}' )
export root_password=$(cat /root/setup/secret.txt |grep root_path| awk '{print $1}')

echo "password change"
mysql --user=root --password=${mysql_password} --connect-expired-password -e "ALTER USER root@localhost IDENTIFIED BY '${root_password}';"

echo "create DB and TABLES"
mysql --user=root --password=$root_password --connect-expired-password -e "CREATE DATABASE rps;"

mysql --user=root --password=$root_password --connect-expired-password -e "create table rps.battle_history(time timestamp,id int,name varchar(10),choice_id int,result varchar(10));"
mysql --user=root --password=$root_password --connect-expired-password -e "alter table rps.battle_history add primary key (time,id);"














