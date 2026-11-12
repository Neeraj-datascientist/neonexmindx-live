with open('deployment_NeoNex/blog/distributed-data-pipelines-with-apache-spark-iceberg/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("First 500 chars of iceberg blog:")
print(html[:500])

