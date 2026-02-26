FROM ubuntu:22.04

# Install necessary packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    openssh-server \
    vsftpd \
    sudo \
    net-tools \
    iputils-ping \
    vim \
    nano \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Configure SSH
RUN mkdir /var/run/sshd
RUN useradd -m -s /bin/bash student
RUN echo 'student:password123' | chpasswd

# Configure FTP (Anonymous login)
RUN mkdir -p /var/ftp/pub
RUN echo "Anonymous FTP login allowed" > /var/ftp/pub/welcome.txt
# Create a hidden flag accessible via FTP
RUN echo "FLAG{ftp_anonymous_login_success}" > /var/ftp/.hidden_flag.txt
RUN chown -R ftp:ftp /var/ftp

# Configure VSFTPD
RUN echo "listen=YES" > /etc/vsftpd.conf && \
    echo "anonymous_enable=YES" >> /etc/vsftpd.conf && \
    echo "local_enable=YES" >> /etc/vsftpd.conf && \
    echo "dirmessage_enable=YES" >> /etc/vsftpd.conf && \
    echo "use_localtime=YES" >> /etc/vsftpd.conf && \
    echo "xferlog_enable=YES" >> /etc/vsftpd.conf && \
    echo "connect_from_port_20=YES" >> /etc/vsftpd.conf && \
    echo "anon_root=/var/ftp" >> /etc/vsftpd.conf && \
    echo "no_anon_password=YES" >> /etc/vsftpd.conf && \
    echo "pasv_enable=YES" >> /etc/vsftpd.conf && \
    echo "pasv_min_port=21100" >> /etc/vsftpd.conf && \
    echo "pasv_max_port=21110" >> /etc/vsftpd.conf

# Privilege Escalation Setup (Sudo NOPASSWD)
RUN echo "student ALL=(ALL) NOPASSWD: /usr/bin/cat" >> /etc/sudoers

# Create Root Flag
RUN echo "FLAG{sudo_privilege_escalation_easy}" > /root/root_flag.txt
RUN chmod 600 /root/root_flag.txt

# Expose ports
EXPOSE 22 21

# Startup script
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

CMD ["/startup.sh"]
