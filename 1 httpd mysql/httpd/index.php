<?php
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";
echo "<h2>" . $txt1 . "</h2>";
?>

<?php

if (!function_exists('mysqli_init') && !extension_loaded('mysqli')) {
    echo 'We don\'t have mysqli!!!';
} else {
    echo 'we have it!';
}
?>



<?php
$servername = "db";
$username = "admin";
$password = "mananx22";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>