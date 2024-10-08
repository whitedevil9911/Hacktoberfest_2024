<?php
error_reporting(E_ALL);
ini_set('display_errors',1);

// Database configuration
$servername = "fe80::fa53:70e0:3eb3:f936";
$username = "root"; 
$password = ""; 
$dbname = "flat_sales_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch inquiries from the database
$sql = "SELECT id, name, email, phone, message, submission_date FROM inquiries ORDER BY submission_date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Display the inquiries
    echo "<h2>Submitted Inquiries</h2>";
    echo "<table border='1'><tr><th>ID</th><th>Name</th><th>Email</th><th>Phone</th><th>Message</th><th>Date</th></tr>";

    while ($row = $result->fetch_assoc()) {
        echo "<tr><td>{$row['id']}</td><td>{$row['name']}</td><td>{$row['email']}</td><td>{$row['phone']}</td><td>{$row['message']}</td><td>{$row['submission_date']}</td></tr>";
    }

    echo "</table>";
} else {
    echo "No inquiries found.";
}

// Close connection
$conn->close();
?>
