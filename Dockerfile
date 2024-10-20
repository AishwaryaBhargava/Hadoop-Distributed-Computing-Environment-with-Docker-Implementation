FROM ubuntu:18.04

# Install SSH server and Java
RUN apt-get update && \
    apt-get install -y ssh rsync vim openjdk-8-jdk && \
    apt-get clean

# Set environment variables
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-arm64
ENV HADOOP_HOME /opt/hadoop
ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin
ENV hadoop_path $HADOOP_HOME
ENV java_path $JAVA_HOME

# Install Hadoop
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz && \
    tar -xzf hadoop-3.2.1.tar.gz -C /opt && \
    mv /opt/hadoop-3.2.1 /opt/hadoop && \
    rm hadoop-3.2.1.tar.gz

# Configure SSH
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \
    cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys && \
    chmod 0600 /root/.ssh/authorized_keys && \
    echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config

# Add Hadoop configuration files
ADD hdfs-site.xml $HADOOP_HOME/etc/hadoop/
ADD core-site.xml $HADOOP_HOME/etc/hadoop/
ADD mapred-site.xml $HADOOP_HOME/etc/hadoop/
ADD yarn-site.xml $HADOOP_HOME/etc/hadoop/

# Add bootstrap script
ADD bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh

# Add JAVA_HOME to hadoop-env.sh
RUN sed -i '/export JAVA_HOME=/c\export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64' $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Expose Hadoop ports
EXPOSE 9870 8088 9000 50070

# Start SSH server and Hadoop services
CMD ["/bootstrap.sh"]
