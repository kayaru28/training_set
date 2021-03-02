DROP SCHEMA IF EXISTS rps;
CREATE DATABASE rps CHARACTER SET utf8mb4;

CREATE TABLE rps.battle_history(
        time timestamp,
        id int,
        name varchar(10),
        choice_id int,
        result varchar(10) 
) DEFAULT CHARACTER SET= utf8mb4;

ALTER TABLE rps.battle_history ADD PRIMARY KEY (time,id);


CREATE TABLE rps.battle_count(
        name varchar(10),
        count int
) DEFAULT CHARACTER SET= utf8mb4;

ALTER TABLE rps.battle_count ADD PRIMARY KEY (name);


