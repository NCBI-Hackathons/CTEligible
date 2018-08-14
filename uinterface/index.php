<?php

//include "include/dbconnect.php";

?>

<HTML>
<HEAD>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>:: CTEligible :: Writing Clinical Trial Protocols</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
 <!-- 
 <link rel="stylesheet" href="/resources/demos/style.css">
 -->
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

<!--  
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script src="https://code.jquery.com/ui/jquery-ui-git.js"></script>
-->
<script>
  $( function() {
//    $( document ).tooltip();
    $( "wordsuggest" ).tooltip();
  } );
  </script>
<style>
.wordsuggest{ color:"red"; }
</style>
</HEAD>
<BODY style="background-color: #FFFFFF">
<!-- <BODY style="background-image: url(background_body.jpg)"> -->
<?php

//include "wordsuggest.php";
$input = "Within";


?>
<P>
<font size=5>
<b>ELIGIBILITY:</b> <br /><br />
<b>
Trial ID: NCT6472<a href="#"></a> </span>
</b>
</font>
<br />
<br />

<table>
<tr>
<td>
<font size=5>
Within <span class="wordsuggest" title="40 days prior. Score = 55%" style="background-color: orange">36 days prior</span> to registration, you must not have treatment.
</font>
</td>
<td>&nbsp;</td>
<td>
<b><font color="purple" size=5>Criteria ID: 40.2, Score: 50%</font></b>
</td>
</tr>
<tr>
<td>
<font size=5>
 Platelet count <span class="wordsuggest" title="greater than or equal to 100000 platelets. Score = 68%" style="background-color: #FFFF00">greater than or equal to 70000 platelets</span> per cubic milimeter.
 </font>
 </td>
 <td width=2%>&nbsp;</td>
<td>
<b><font color="purple" size=5>Criteria ID: 40.6, Score: 42%</font></b>
</td>
</tr>


<tr>
<td>
Browse File: <br />
<input  name="browsefile1" type="file"></input>
</td><td>&nbsp;</td>
<td>
<br />
<br />
<b><font size="6"><u>Consensus Score</u>: 46%</font></b>
</td>
</tr>
</table>

</P>

<!--<span class="wordsuggest" title="Another similar word exists">
-->

<?php 

//echo ("Within 36 days prior to registration you must not have treatment");
//wordFunction("Within 36 days prior to registration you must not have treatment");

?>

<!--
</span>.
-->
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<form action="process.php" method="POST">
Inclusion/Exclusion Criteria: <br />
<select name="Eligibility">
    <option value="">--Please choose eligibility criteria--</option>
    <option value="inclusion">Inclusion</option>
    <option value="exclusion">Exclusion</option>
</select>
<p>
Platelet must be greater than: <br />
    <input type="text" name="platelet">
<br />
And:
<br />
    <input type="text" name="and2">

List of Trials:
<select name="ListOfTrial">
    <option value=""></option>
    <option value="look2a">Inclusion</option>
    <option value="look2b">Exclusion</option>
 </select>

<br /> 
<br /> 
Browse File: <br />
<input name="browsefile2" type="file"></input>
 
<p>

<!--
<p>
Inclusion/Exclusion Criteria: <br />
<select name="Eligibility">
    <option value="">--Please choose eligibility criteria--</option>
    <option value="inclusion">Inclusion</option>
    <option value="exclusion">Exclusion</option>
    <option value="hamster">Hamster</option>
    <option value="parrot">Parrot</option>
    <option value="spider">Spider</option>
    <option value="goldfish">Goldfish</option>
</select>
<p>
-->

</form>

<!--
Wrap

Make a php function that takes a string input, queries a database, and gets the word suggestions and corresponding scores and returns those as output.

<HTML>
<P>
This is a <?php wordfunction("word"); ?>

</P>
</HTML>

- editing and adding the new words, we will take more jquery script, and Ajax does the updating of the database onclick.

Jquery methods: .click methods, .ajax methods are cool to do it.






-->
</font>
</BODY>

</HTML>