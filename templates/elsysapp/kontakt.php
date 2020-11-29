
<?php
// varaible setting
$name = $_REQUEST["Name"];
$email = $_REQUEST["Email"];
$messeage = $_REQUEST["Message"];

//check input fileds
if (empty($name) || empty($email) || empty($messeage))
{
    echo "Vennligst fyll alle arkivene"
}
else
{
    mail("julieqh@stud.ntnu.no", "Svingbrya", $message, "From: $name < $email>");
    echo "<script type =  'text/javascript'>alert('Din meldning er sent') window.history.log(-1); </script>";
    
}
?>

