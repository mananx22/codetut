<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" 
    integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" 
    crossorigin="anonymous"></script>
<script
  src="https://code.jquery.com/jquery-3.6.0.min.js"
  ></script>
</head>

<body> 
<form >
    <input type = 'textbox' name = 'name' id = 'name' placeholder="Enter your name ..." > <br><br>
    <input type = 'textbox' name = 'amt' id = 'amt' placeholder="Amount ..." > <br><br>
    <input type = 'button' name = 'btn' id = 'btn' value="Pay Now" onclick="pay_now()" > 
</form>
</body>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
    function pay_now(){
        var name = document.getElementById("name").value;

        var amt = document.getElementById("amt").value;

        jQuery.ajax({
                   type:'post',
                   url:'payment.php',
                   data: "amt="+amt +"&name="+name,
                   success:function(result){
                        var options = {
                            "key": "rzp_test_ueU7783QNeCvGc", // Enter the Key ID generated from the Dashboard
                            "amount": amt*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                            "currency": "INR",
                            "name": "IsleArts",
                            "description": "Test Transaction",
                            "image": "https://scontent.fjai1-2.fna.fbcdn.net/v/t1.18169-9/28471564_192198678178631_6771010993698422407_n.jpg?_nc_cat=108&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=0jPvQaLT89sAX9stXUH&_nc_ht=scontent.fjai1-2.fna&oh=ce6f7645596a1a809aecf15e94966ef5&oe=60CFB831",    
                                "handler": function (response){
                                        jQuery.ajax({
                                            type:'post',
                                            url:'payment.php',
                                            data: "payment_id=" + response.razorpay_payment_id,
                                            success:function(result){
                                                alert("Payment successful "+ response.razorpay_payment_id);
                                                // window.location.href="payment.php"
                                            }
                                        });
                                }
                        };

                        var rzp1 = new Razorpay(options);           
                        rzp1.open();
                    }
        });

        
    } 
    
</script>
</html>













<!-- 
<button id="rzp-button1">Pay</button>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
var options = {
    "key": "rzp_test_ueU7783QNeCvGc", // Enter the Key ID generated from the Dashboard
    "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    "currency": "INR",
    "name": "Acme Corp",
    "description": "Test Transaction",
    "image": "https://example.com/your_logo",    
    "handler": function (response){
        alert(response.razorpay_payment_id);
        alert(response.razorpay_order_id);
        alert(response.razorpay_signature)
    }
};
var rzp1 = new Razorpay(options);
document.getElementById('rzp-button1').onclick = function(e){
    rzp1.open();
    e.preventDefault();
}
</script> -->