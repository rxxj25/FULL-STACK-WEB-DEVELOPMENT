<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $electricityUsage = $_POST["electricityUsage"];
    $waterUsage = $_POST["waterUsage"];
    $maintenanceFee = $_POST["maintenanceFee"];

    // Calculate utility bills
    $electricityBill = $electricityUsage * ELECTRICITY_RATE; // Define ELECTRICITY_RATE as per your tariff
    $waterBill = $waterUsage * WATER_RATE; // Define WATER_RATE as per your tariff

    // Calculate total bill
    $totalBill = $electricityBill + $waterBill + $maintenanceFee;

    // Store data in the database
    $servername = "localhost";
    $username = "your_username";
    $password = "your_password";
    $dbname = "your_database";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare SQL statement
    $sql = "INSERT INTO utility_bills (electricity_usage, water_usage, maintenance_fee, electricity_bill, water_bill, total_bill)
            VALUES ('$electricityUsage', '$waterUsage', '$maintenanceFee', '$electricityBill', '$waterBill', '$totalBill')";

    if ($conn->query($sql) === TRUE) {
        echo "Bills calculated and stored successfully.";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Close connection
    $conn->close();
}
?>
