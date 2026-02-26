FROM php:7.4-apache

# Install dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && docker-php-ext-install pdo pdo_sqlite

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Create directory for DB
RUN mkdir /var/www/db
RUN chown www-data:www-data /var/www/db
RUN chmod 755 /var/www/db

# Copy source code
COPY src/ /var/www/html/

# Make web root writable for SQLi to shell exploit (ATTACH DATABASE)
RUN chown -R www-data:www-data /var/www/html

# Initialize Database
RUN php /var/www/html/init_db.php && \
    rm /var/www/html/init_db.php && \
    chown www-data:www-data /var/www/db/users.db

# SUID Privilege Escalation Setup
# We will make 'base64' SUID root, allowing reading of any file
RUN chmod u+s /usr/bin/base64

# Create Flags
# Flag 1 is in the database (inserted via init_db.php)
# Flag 2 is in /root/root_flag.txt
RUN echo "FLAG{suid_privesc_via_base64}" > /root/root_flag.txt
RUN chmod 600 /root/root_flag.txt

# Create a "backup" file with a hint or creds
RUN echo "admin:supersecretpassword" > /var/www/html/.htpasswd.bak

EXPOSE 80
