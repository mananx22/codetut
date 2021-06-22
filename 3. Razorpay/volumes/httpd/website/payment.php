<?php 
session_start();
include('db.php');

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully ";

// *************** TEST CODE ***************
//   $payment_id="sdwerr ";
//   $amt=233  ;
//   $name=" sdada ";
//   $payment_status='success ';
//   $added_on=date('Y-m-d h:i:s ');
//   echo  $payment_id;
//   echo  $amt;
//   echo  $name; 
// $sql = "INSERT INTO payment (name, amt, payment_status, payment_id, added_on) VALUES ('$name','$amt','$payment_id','$payment_status','$added_on')";
// if(mysqli_query($conn, $sql)){
//     echo "Records inserted successfully.";
// } else{
//     echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
// }
// *************** END TEST CODE ***************

if(isset($_POST['amt']) && isset($_POST['name']))
    {
        
        $amt=$_POST['amt'];
        $name=$_POST['name'];
        $payment_status="pending";
        $added_on=date('Y-m-d h:i:s'); 

        $sql = "INSERT INTO payment (name, amt, payment_status, added_on) VALUES ('$name', $amt, '$payment_status','$added_on')";
        echo $sql;
        mysqli_query($conn, $sql);

        $_SESSION['OID'] = mysqli_insert_id($conn);
        
    }

if(isset($_POST['payment_id']) && isset($_SESSION['OID']) )
    {
        $payment_id=$_POST['payment_id'];        

        $sql = "UPDATE payment SET payment_status='complete', payment_id='$payment_id' where id='".$_SESSION['OID']. "'";
        echo $sql;
        mysqli_query($conn, $sql);
        
    }


?>