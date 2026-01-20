FROM apache/spark:3.5.1

WORKDIR /opt/app

# Copy only application files
COPY app.py .
COPY data1.csv .
COPY data2.csv .

# Run Spark job
CMD ["/opt/spark/bin/spark-submit", "/opt/app/app.py"]
