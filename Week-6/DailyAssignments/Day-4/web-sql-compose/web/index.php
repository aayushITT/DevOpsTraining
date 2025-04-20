<?php
$host = 'db';
$user = 'user';
$pass = 'password';
$db = 'testdb';
$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $conn->query("INSERT INTO users (name) VALUES ('$name')");
}
$result = $conn->query("SELECT * FROM users");
?>
<form method="POST">
    <input type="text" name="name" />
    <input type="submit" />
</form>
<ul>
<?php while ($row = $result->fetch_assoc()) {
    echo "<li>" . $row['name'] . "</li>";
} ?>
</ul>
