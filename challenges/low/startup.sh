#!/bin/bash

# Start SSH
service ssh start

# Start VSFTPD
service vsftpd start

# Keep container running
tail -f /dev/null
