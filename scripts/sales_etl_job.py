import sys
from pyspark.sql import SparkSession, functions as F

def main(run_date):
    spark = (SparkSession.builder.appName("SalesETLJob").master("spark://spark-master:7077").getOrCreate())

    # --- Read ---
    df_sales = (spark.read.option("header", True).csv("hdfs://hdfs-namenode:9000/sales_etl/input/sales.csv"))

    df_products = (spark.read.json("hdfs://hdfs-namenode:9000/sales_etl/input/products.json"))


    df_sales.createOrReplaceTempView("sales_raw")
    df_products.createOrReplaceTempView("products_raw")


    # --- Enrich / classify ---
    spark.sql("""
        CREATE OR REPLACE TEMP VIEW sales_enriched AS
        SELECT
            s.sale_id,
            s.product_id,
            s.quantity,
            p.product_name,
            p.unit_price,
            (s.quantity * p.unit_price) AS total_price,
            CASE
                WHEN (s.quantity * p.unit_price) >= 1000 THEN 'High'
                WHEN (s.quantity * p.unit_price) >= 500  THEN 'Medium'
                ELSE 'Low'
            END AS sale_value_category
        FROM sales_raw s
        INNER JOIN products_raw p
            ON s.product_id = p.product_id
    """)

    df_output = spark.sql("SELECT * FROM sales_enriched")

    df_output.write.mode("overwrite").option("header", True).csv("hdfs://hdfs-namenode:9000/sales_etl/output/final_csv/{run_date}")
    df_output.write.mode("overwrite").parquet("hdfs://hdfs-namenode:9000/sales_etl/output/final_parquet/{run_date}")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide run_date argument in format YYYY-MM-DD")
        sys.exit(1)
    
    run_date = sys.argv[1]
    main(run_date)

