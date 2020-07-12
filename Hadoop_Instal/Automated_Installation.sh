#!/usr/bin/env bash

echo "UPDATING SYSTEM"
sudo apt-get update << EOF
Password
EOF

## Creating a directoy called "opt"
mkdir opt
cd opt

## Java
echo
echo "INSTALLING JAVA"

 wget -O jdk-8u221-linux-x64.tar.gz \
 -c --content-disposition \
 "https://javadl.oracle.com/webapps/download/AutoDL BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"
 tar -zxvf jdk-8u221-linux-x64.tar.gz
 rm jdk-8u221-linux-x64.tar.gz

# Create a bash profile
cd
sudo gedit .bash_profile
echo "## JAVA HOME" >> .bash_profile.sh
echo "export JAVA_HOME=/home/fieldemploye/opt/jdk1.8.0_221" >> .bash_profile.sh
echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile.sh

## HADOOP
echo
echo "INSTALLING HADOOP"
echo >> .bash_profile.sh
echo "## HADOOP HOME" >> .bash_profile.sh
echo "export HADOOP_HOME=/home/fieldemploye/opt/hadoop-3.1.3" >> .bash_profile.sh
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export YARN_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> .bash_profile.sh

# Edit hadoop-env.sh
cd opt/hadoop-3.1.3/etc/hadoop
sudo gedit hadoop-env.sh << EOF
Password
EOF

echo "export JAVA_HOME=/home/fieldemploye/opt/jdk1.8.0_221" >> hadoop-env.sh

# Edit core-site.xml
sudo gedit core-site.xml << EOF
Password
EOF

echo "<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
<property>
<configuration>" >> core-site.xml

# Edit hdfs-site.xml
sudo gedit hdfs-site.xml

echo "<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>
<property>
  <name>dfs.name.dir</name>
    <value>file:///home/fieldemploye/opt/hadoop-3.1.3/namenode</value>
</property>
<property>
  <name>dfs.data.dir</name>
    <value>file:///home/fieldemploye/opt/hadoop-3.1.3/datanode</value>
</property>
</configuration>" >> hdfs-site.xml

## Edit mapred-site.xml
sudo gedit mapred-site.xml

echo "<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>" >> mapred-site.xml

## Edit yarn-site.xml
sudo gedit yarn-site.xml

echo "<configuration>
<property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>" >> yarn-site.xml


## Python
echo
echo "INSTALLING Python"

# Another alternative to install Python
#sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev #libreadline-dev libffi-dev << EOF
#Y
#EOF

cd opt
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar -zxvf Python-3.7.5.tgz
rm Python-3.7.5.tgz

echo "export PHYTON_HOME=/home/fieldemploye/opt/Python-3.7.5" >> .bash_profile.sh
echo "export PATH=$PATH:$PHYTON_HOME/bin" >> .bash_profile.sh

## Scala
echo
echo "INSTALLING Scala"

sudo wget http://scala-lang.org/files/archive/scala-2.12.11.deb
sudo dpkg -i scala-2.12.11.deb

echo "## SCALA HOME"
echo "export SCALA_HOME=/home/fieldemploye/opt/scala-2.11.8" >> .bash_profile.sh
echo "export PATH=$PATH:$SCALA_HOME/bin" >> .bash_profile.sh


## SQOOP 
echo 
echo "INSTALLING SQOOP"

echo "## SQOOP HOME" >> .bash_profile.sh
echo "export SQOOP_HOME=/home/fieldemploye/opt/sqoop-1.4.7" >> .bash_profile.sh
echo "export PATH=$PATH:$SQOOP_HOME/bin" >> .bash_profile.sh

## MYSQL
echo "INSTALLING MYSQL"
echo

cd
sudo apt-get install mysql-server
sudo mysql_secure_installation utility
# Allow remote access
sudo ufw enable
sudo ufw allow mysql
# Start the MySQL service
sudo systemctl start mysql 
sudo systemctl status mysql.service
# launch at reboot
sudo systemctl enable mysql
sudo systemctl restart mysql
# Set the root password
UPDATE mysql.user SET authentication_string = PASSWORD('Password') WHERE User = 'root';
FLUSH PRIVILEGES;


## SBT Home
#export SBT_HOME=/home/fieldemploye/opt/sbt
#export PATH=$PATH:$SBT_HOME/bin

source .bash_profile

## Format hdfs namenode
hdfs namenode -format

## Start all sh
start-all.sh

## Check running status
jps
