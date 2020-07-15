
#### CREATE A CONNECTION USING SSH
sudo ssh start
ssh-keygen

# On machine 1
user@ipaddressMachine2
nc localhost <Port>

#On machine 2
nc -l <Port>

# To end connection
sudo service ssh stop


#### CREATE A CONNECTION USING NETCAT
# 9600 is the port we will be using
# Get the IP address for both devices by command
ip address or ip add or ip a

# Replace the ip address by localhost in the syntaxes below

# Open the listener connection (-l: listener)
nc localhost 9600 -l

# Open the sender connection
nc localhost 9600
