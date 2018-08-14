<?php

function conn() {
    $mysqli = new mysqli('localhost', 'user', 'pass', 'cteligible');
    $mysqli->set_charset('utf8');
	
    return $mysqli;
}

?>
<!--

<p>This is a <?php // wordFunction("word"); ?>.</p>

-->


<!--

MySQL commands for setting up CTEligible Database
mysql>
CREATE DATABASE cteligible;
GRANT ALL ON cteligible.* to user@cteligible IDENTIFIED BY 'pass';
CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);

DROP TABLE wordsuggest_tbl;
CREATE TABLE IF NOT EXISTS wordsuggest_tbl (sn INT(255) NOT NULL AUTO_INCREMENT, cid VARCHAR(255) NOT NULL, words VARCHAR(255) NOT NULL, cscore VARCHAR(20) NOT NULL, PRIMARY KEY (sn)
)ENGINE=INNODB;

INSERT INTO wordsuggest_tbl VALUES ('','40.2',"Platelet count greater than or equal to 100000 platelets per cubic milimeter",'58');
INSERT INTO wordsuggest_tbl VALUES ('','23',"Within 36 days prior to registration you must not have treatment",'31');

DESCRIBE wordsuggest_tbl;

SELECT * FROM wordsuggest_tbl;
-->