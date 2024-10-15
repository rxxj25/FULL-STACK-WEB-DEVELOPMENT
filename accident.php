<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate form data
    if (isset($_POST['robbery-location']) && isset($_POST['robbery-description'])) {
        $robbery_location = $_POST['robbery-location'];
        $robbery_description = $_POST['robbery-description'];

        // Process the data (you can save it to a database, send an email, etc.)
        // For now, just display a confirmation message
        echo "<div class='confirmation'>Robbery reported successfully!</div>";
    } else {
        // If required fields are missing, display an error message
        echo "<div class='error'>Please fill in all required fields.</div>";
    }
}
?>