# Hadoop-Distributed-Computing-Environment-with-Docker-Implementation

A comprehensive log analysis system built using Hadoop MapReduce, designed to process and analyze web server logs at scale. This implementation provides multiple analysis capabilities through various MapReduce jobs, all containerized using Docker.

## 🚀 Features

### Traffic Analysis
- Most frequently accessed paths tracking
- IP address access patterns
- HTTP method distribution analysis
- URL pattern analysis using n-grams
- Total traffic volume calculation

### Security Monitoring
- Specific IP address monitoring
- POST request tracking
- Error code analysis
- High-volume requestor identification

### Error Tracking
- 404 error monitoring
- Status code distribution
- Response size analysis
- Error pattern detection

### Performance Metrics
- Response size tracking by IP
- Success rate analysis
- Date-specific traffic analysis
- Bandwidth usage monitoring

## 🛠 Prerequisites

- Docker
- Python 3.x
- Hadoop 3.x
- Bash shell

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/AishwaryaBhargava/Hadoop-Distributed-Computing-Environment-with-Docker-Implementation.git
cd Hadoop-Distributed-Computing-Environment-with-Docker-Implementation
```

2. Start the Hadoop environment:
```bash
./bootstrap.sh
```

## 🔍 Available Analysis Jobs

### 1. N-gram Analysis
- **Files**: `mapper.py`, `reducer.py`
- **Purpose**: Analyzes text patterns in URLs
- **Usage**:
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper mapper.py \
    -reducer reducer.py \
    -input /path/to/logs \
    -output /output/ngrams
```

### 2. Image Access Analysis
- **Files**: `mapper1.py`, `reducer1.py`
- **Purpose**: Tracks access to image files
- **Usage**: Similar to above, using mapper1.py and reducer1.py

### 3. IP Address Analysis
- **Files**: `mapper2.py`, `reducer2.py`
- **Purpose**: Monitors specific IP address activity
- **Files**: `mapper5.py`, `reducer5.py`
- **Purpose**: Identifies most active IP addresses

### 4. HTTP Method Analysis
- **Files**: `mapper3.py`, `reducer3.py`
- **Purpose**: Analyzes distribution of HTTP methods
- **Files**: `mapper6.py`, `reducer6.py`
- **Purpose**: Specifically tracks POST requests

### 5. Request Path Analysis
- **Files**: `mapper4.py`, `reducer4.py`
- **Purpose**: Identifies most accessed paths

### 6. Error Analysis
- **Files**: `mapper7.py`, `reducer7.py`
- **Purpose**: Tracks 404 errors and other status codes

### 7. Bandwidth Analysis
- **Files**: `mapper8.py`, `reducer8.py`, `mapper9.py`, `reducer9.py`, `mapper10.py`, `reducer10.py`
- **Purpose**: Analyzes bandwidth usage patterns and response sizes

## 📊 Example Usage

### Basic Log Analysis
```bash
# Run basic log analysis
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper mapper2.py \
    -reducer reducer2.py \
    -input /path/to/logs \
    -output /output/basic_analysis
```

### Finding Most Active IPs
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper mapper5.py \
    -reducer reducer5.py \
    -input /path/to/logs \
    -output /output/ip_analysis
```

### Tracking POST Requests
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -mapper mapper6.py \
    -reducer reducer6.py \
    -input /path/to/logs \
    -output /output/post_analysis
```

## 📌 Notes

- All mapper and reducer scripts are written in Python for maintainability
- Each analysis job is designed to work independently
- Scripts handle common log format errors gracefully
- Date-specific analysis available for historical data

## 🔧 Troubleshooting

1. If jobs fail to start:
   - Check if Hadoop services are running using `jps`
   - Verify input file permissions
   - Check Python script permissions (should be executable)

2. If results are unexpected:
   - Verify log format matches expected format
   - Check for date range restrictions in scripts
   - Verify input path contains valid log files

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔗 Additional Resources

- [Hadoop Streaming Documentation](http://hadoop.apache.org/docs/current/hadoop-streaming/HadoopStreaming.html)
- [Python Documentation](https://docs.python.org/3/)
- [Log Analysis Best Practices](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
