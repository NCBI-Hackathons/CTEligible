<?php
/*function conn() {
    $mysqli = new mysqli('localhost', 'user', 'pass', 'cteligible');
    $mysqli->set_charset('utf8');
    return $mysqli;
}
*/

function conn() {
    $mysqli = new mysqli('localhost', 'user', 'pass', 'cteligible');
    $mysqli->set_charset('utf8');
	
    return $mysqli;
}

function wordFunction($input) {
		//lookup $input in database
		$mysqli = new mysqli('localhost', 'user', 'pass', 'cteligible');
		$mysqli->set_charset('utf8');
		
		$query= $mysqli->prepare("SELECT cscore FROM wordsuggest_tbl WHERE words=?");
		$query->bind_param('s',$input);
		
		$query->execute();
		$result = $query->get_result();
		$return = $result->fetch_all();
		
		var_dump($return);
		
		//		$query= "SELECT words, cscore FROM wordsuggest_tbl WHERE ";
//		$results = get query results, hopefully with mysqli;
//		$otherWordsFromDatabase = ?
//		$returnedHTML = "<span class='wordsuggest' title='";
//		$returnedHTML .= $results["words"];
//		$returnedHTML .= ">" . $input . "</span>";
//		echo $returnedHTML;
echo "Test CSCORE";
		}

// python3 parseInputSentence.py "Within 36 days prior to registration you must not have treatment";
// Score: 31

?>
<!--
<p>This is a <?php // wordFunction("word"); ?>.</p>
-->

<!--
mysql>
CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);

It's better to use the Platelet and the Haemoglobin Trial Data. Concentrate on the Numbers for Now.
Return the Scores for each criteria and also the weighted score for all the criteria on the page.

DROP TABLE wordsuggest_tbl;

CREATE TABLE IF NOT EXISTS wordsuggest_tbl (sn INT(255) NOT NULL AUTO_INCREMENT, cid VARCHAR(255) NOT NULL,words VARCHAR(255) NOT NULL, cscore VARCHAR(20) NOT NULL, PRIMARY KEY (sn))ENGINE=INNODB;

INSERT INTO wordsuggest_tbl VALUES ('',"Within 36 days prior to registration you must not have treatment",'31');

INSERT INTO wordsuggest_tbl VALUES ('','40.2',"Platelet count greater than or equal to 100000 platelets per cubic milimeter",'58');

DESCRIBE wordsuggest_tbl;

SELECT * FROM wordsuggest_tbl;

CREATE TABLE parent (
    id INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE=INNODB;

Severe, active co-morbidity, defined as follows:

HIV_CTEPTrials_072018

Exclusion

* Acquired immune deficiency syndrome (AIDS) based upon current Centers for Disease Control and Prevention (CDC) definition; note: human immunodeficiency virus (HIV) testing is not required for entry into this protocol; protocol-specific requirements may also exclude immuno-compromised patients

AIDS excluded; immunocompromised excluded



-->