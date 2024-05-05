import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, max, min, count, desc

spark = SparkSession.builder \
    .appName("MicroDataWarehouseETL") \
    .config("spark.driver.extraClassPath", "sqlite-jdbc-3.45.3.0.jar") \
    .getOrCreate()

# Extract
sales_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "sales") \
    .option("driver", "org.sqlite.JDBC") \
    .load()
customers_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "customers") \
    .option("driver", "org.sqlite.JDBC") \
    .load()
employees_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "employees") \
    .option("driver", "org.sqlite.JDBC") \
    .load()

# Transform
total_revenue_df = sales_df.agg(sum(sales_df.PRICE * sales_df.QUANTITY).alias("TOTAL_REVENUE"))
print("Total Revenue:")
total_revenue_df.show()

top_selling_products_df = sales_df.groupBy("PRODUCT_NAME").agg(sum("QUANTITY").alias("TOTAL_QUANTITY")) \
    .orderBy("TOTAL_QUANTITY", ascending=False).limit(5)
print("Top 5 Selling Products:")
top_selling_products_df.show()

avg_salary_by_dept_df = employees_df.groupBy("DEPARTMENT").agg(avg("SALARY").alias("AVG_SALARY"))
print("Average Salary by Department:")
avg_salary_by_dept_df.show()

high_value_customers_df = customers_df.orderBy(desc("TOTAL_PURCHASES")).limit(3)
print("Top 3 High-Value Customers:")
high_value_customers_df.show()

sales_metrics_by_category_df = sales_df.groupBy("CATEGORY").agg(
    sum("QUANTITY").alias("TOTAL_QUANTITY"),
    avg("PRICE").alias("AVG_PRICE"),
    max("PRICE").alias("MAX_PRICE"),
    min("PRICE").alias("MIN_PRICE"),
    count("*").alias("NUM_PRODUCTS")
)
print("Sales Metrics by Category:")
sales_metrics_by_category_df.show()

# Load
total_revenue_df.write.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "total_revenue") \
    .option("driver", "org.sqlite.JDBC") \
    .mode("overwrite") \
    .save()
top_selling_products_df.write.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "top_selling_products") \
    .option("driver", "org.sqlite.JDBC") \
    .mode("overwrite") \
    .save()
avg_salary_by_dept_df.write.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "avg_salary_by_dept") \
    .option("driver", "org.sqlite.JDBC") \
    .mode("overwrite") \
    .save()
high_value_customers_df.write.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "high_value_customers") \
    .option("driver", "org.sqlite.JDBC") \
    .mode("overwrite") \
    .save()
sales_metrics_by_category_df.write.format("jdbc") \
    .option("url", "jdbc:sqlite:microdatawarehouse.db") \
    .option("dbtable", "sales_metrics_by_category") \
    .option("driver", "org.sqlite.JDBC") \
    .mode("overwrite") \
    .save()

spark.stop()