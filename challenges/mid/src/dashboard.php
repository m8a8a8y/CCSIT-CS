<?php
session_start();

if (!isset($_SESSION['user'])) {
    header("Location: index.php");
    exit;
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Mid Level Challenge - Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Roboto Mono', monospace; background: #020617; color: #f8fafc; text-align: center; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background: #0f172a; padding: 2rem; border-radius: 8px; border: 1px solid rgba(0, 224, 255, 0.3); }
        h1 { font-family: 'Orbitron', sans-serif; color: #00e0ff; }
        .flag { font-size: 1.5rem; margin: 2rem 0; padding: 1rem; border: 1px solid #22c55e; color: #22c55e; background: rgba(34, 197, 94, 0.1); border-radius: 4px; }
        .hint { color: #94a3b8; font-size: 0.875rem; margin-top: 2rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>ACCESS GRANTED</h1>
        <p>Welcome back, <?= htmlspecialchars($_SESSION['user']) ?>.</p>

        <div class="flag">
            WEB FLAG: FLAG{simple_sql_injection_bypass}
        </div>

        <p>But the real power lies within the system. Can you escalate your privileges?</p>

        <div class="hint">
            HINT: Check for SUID binaries. Maybe decode something interesting?
        </div>

        <a href="logout.php" style="color: #ef4444;">Logout</a>
    </div>
</body>
</html>
