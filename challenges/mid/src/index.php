<?php
session_start();

$db = new SQLite3('/var/www/db/users.db');

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // VULNERABLE QUERY: No prepared statements!
    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

    // Debug info (optional, helps beginners)
    // echo "Debug: " . $query . "<br>";

    $result = $db->query($query);

    if ($result) {
        $row = $result->fetchArray(SQLITE3_ASSOC);
        if ($row) {
            $_SESSION['user'] = $row['username'];
            header("Location: dashboard.php");
            exit;
        } else {
            $error = "Invalid credentials";
        }
    } else {
        $error = "Database Error: " . $db->lastErrorMsg();
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Mid Level Challenge - Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Roboto Mono', monospace; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: rgba(15, 23, 42, 0.6); padding: 2rem; border: 1px solid rgba(0, 224, 255, 0.3); border-radius: 8px; width: 300px; text-align: center; }
        input { width: 100%; padding: 10px; margin: 10px 0; background: #1e293b; border: 1px solid #334155; color: white; }
        button { width: 100%; padding: 10px; background: #00e0ff; border: none; font-weight: bold; cursor: pointer; color: #000; }
        button:hover { background: #00b8d4; }
        .error { color: #ef4444; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>SECURE PORTAL</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">ACCESS</button>
        </form>
        <?php if(isset($error)) echo "<p class='error'>$error</p>"; ?>
        <!-- Hint: Maybe try admin' OR '1'='1 -->
    </div>
</body>
</html>
