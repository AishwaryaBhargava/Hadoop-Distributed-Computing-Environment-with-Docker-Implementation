#!/bin/bash

# Start SSH server
/etc/init.d/ssh start

# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Set HADOOP_HOME
export HADOOP_HOME=/opt/hadoop

# Check if Hadoop commands exist
if ! command -v $HADOOP_HOME/bin/hdfs &> /dev/null; then
    echo "Hadoop commands not found. Exiting."
    exit 1
fi

# Format namenode
$HADOOP_HOME/bin/hdfs namenode -format

# Start Hadoop services
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh
$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver

# Keep the container running
tail -f /dev/null