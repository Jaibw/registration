CREATE DATABASE IF NOT EXISTS demo;

CREATE TABLE IF NOT EXISTS `demo`.`registration`
(
`id` INT(11) NOT NULL AUTO_INCREMENT ,
`name` VARCHAR(500) NOT NULL ,
`email` VARCHAR(500) NOT NULL ,
`create` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ,
PRIMARY KEY (`id`)
) ENGINE = MyISAM;