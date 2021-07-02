-- SET PERSIST disabled_storage_engines="MyISAM,BLACKHOLE,FEDERATED,ARCHIVE,MEMORY";

SET PERSIST server_id = 1;
SET PERSIST enforce_gtid_consistency = 'ON'; -- up
SET PERSIST gtid_mode = 'OFF_PERMISSIVE'; -- add
SET PERSIST gtid_mode = 'ON_PERMISSIVE'; -- add
SET PERSIST gtid_mode = 'ON';

INSTALL PLUGIN group_replication SONAME 'group_replication.so'; -- up

-- SET PERSIST plugin_load_add='group_replication.so';
SET PERSIST group_replication_group_name="5af90778-dae0-11eb-a627-0242c0a81003"; -- uuid
SET PERSIST group_replication_start_on_boot=off;
SET PERSIST group_replication_local_address= "mysql:33061";
SET PERSIST group_replication_group_seeds= "mysql:33061,mysql002:33061,mysql003:33061";
SET PERSIST group_replication_bootstrap_group=off;

SET SQL_LOG_BIN=0;
CREATE USER replication_user@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO replication_user@'%';
GRANT BACKUP_ADMIN ON *.* TO replication_user@'%';
FLUSH PRIVILEGES;
SET SQL_LOG_BIN=1;

CHANGE REPLICATION SOURCE TO SOURCE_USER='replication_user', SOURCE_PASSWORD='password' FOR CHANNEL 'group_replication_recovery';

