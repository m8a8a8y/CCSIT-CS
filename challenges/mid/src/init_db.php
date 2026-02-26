<?php
$db = new SQLite3('/var/www/db/users.db');

$db->exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)");

// Insert admin user
$db->exec("INSERT INTO users (username, password, role) VALUES ('admin', 'supersecretpassword123', 'admin')");

// Insert a fake user with a flag as password
$db->exec("INSERT INTO users (username, password, role) VALUES ('flag_keeper', 'FLAG{database_dump_master}', 'user')");

echo "Database initialized.";
?>
