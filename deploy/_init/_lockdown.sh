#!/bin/bash

echo "Pre-system Update"
unset UCF_FORCE_CONFFOLD
export UCF_FORCE_CONFFNEW=YES
ucf --purge /boot/grub/menu.lst


echo "System Update"
# https://devops.stackexchange.com/a/1143
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -yq


echo "System Install"
sudo apt-get install fail2ban mosh ufw vim tree htop -y


echo "Create User"
AUTH_KEYS_DIR="/root"

USER="deploy"

# Create new user.
useradd $USER
mkdir /home/$USER
mkdir /home/$USER/.ssh
chmod 700 /home/$USER/.ssh
chsh -s /bin/bash $USER

# Copy Authorized keys.
cp $AUTH_KEYS_DIR/.ssh/authorized_keys /home/$USER/.ssh/authorized_keys
chmod 400 /home/$USER/.ssh/authorized_keys
chown $USER:$USER /home/$USER -R

# Add User to the 'sudo' group.
usermod -a -G sudo $USER

echo "Set password for user"
passwd $USER

apt-get update
apt-get upgrade -y
apt-get install fail2ban mosh ufw vim unattended-upgrades -y

# Add User to the sudoers file.
echo "$USER    ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


# Configure SSH.
cat << EOF > /etc/ssh/sshd_config
Port 22
Protocol 2
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
HostKey /etc/ssh/ssh_host_ed25519_key
UsePrivilegeSeparation yes
KeyRegenerationInterval 3600
ServerKeyBits 1024
SyslogFacility AUTH
LogLevel INFO
LoginGraceTime 120
PermitRootLogin no
StrictModes yes
RSAAuthentication yes
PubkeyAuthentication yes
IgnoreRhosts yes
RhostsRSAAuthentication no
HostbasedAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
PasswordAuthentication no
X11Forwarding yes
X11DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
UsePAM yes
EOF

service ssh restart

# Configure Firewall.
ufw allow 22
ufw allow 80
ufw allow 443
ufw allow 60000:61000/udp
ufw --force enable
