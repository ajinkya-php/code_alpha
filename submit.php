<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = [
        $_POST['name'],
        $_POST['email'],
        $_POST['title'],
        $_POST['severity'],
        $_POST['description'],
        date("Y-m-d H:i:s")
    ];

    $file = fopen("bugs.csv", "a");
    fputcsv($file, $data);
    fclose($file);

    echo "<h2>Thank you! Your bug has been submitted.</h2>";
} else {
    echo "Invalid access.";
}
?>
