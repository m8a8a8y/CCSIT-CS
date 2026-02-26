FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    sudo \
    iputils-ping \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Set up app directory
WORKDIR /app

# Create user
RUN useradd -m -s /bin/bash appuser

# Install Flask
RUN pip install flask

# Copy app files
COPY app/ /app/
RUN chown -R appuser:appuser /app

# Create uploads directory
RUN mkdir /app/uploads
RUN chown appuser:appuser /app/uploads

# Setup Privilege Escalation (Wildcard Injection)
# Create the vulnerable script
RUN mkdir /opt/scripts
COPY scripts/healthcheck.py /opt/scripts/healthcheck.py
RUN chmod 755 /opt/scripts/healthcheck.py

# Allow appuser to run the script as root
RUN echo "appuser ALL=(ALL) NOPASSWD: /usr/bin/python3 /opt/scripts/healthcheck.py" >> /etc/sudoers

# Flags
RUN echo "FLAG{command_injection_rce_success}" > /app/user_flag.txt
RUN echo "FLAG{wildcard_injection_privesc}" > /root/root_flag.txt
RUN chmod 600 /root/root_flag.txt

# Switch to user
USER appuser

EXPOSE 5000

CMD ["python3", "app.py"]
