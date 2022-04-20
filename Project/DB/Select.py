import pandas as pd
from DB.Connection import getCursor

LINESLIMIT = 100000


def getRevenueKPI():
    global LINESLIMIT
    query = f"""
        SELECT 
            SUM(revenue) AS total_revenue
        from 
        (
            SELECT 
            ROUND((sales.bottles_sold*bottles.bottle_retail_price)::NUMERIC,2) AS revenue
            FROM 
                sales
            inner join bottles ON
                sales.bottle_id = bottles.bottle_id
            ORDER BY sales.sale_id
            LIMIT {LINESLIMIT}
        ) AS bottles_revenue
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchone()
    if output:
        return output[0]
    return None


def getCostKPI():
    global LINESLIMIT
    query = f"""
        SELECT 
            SUM(cost) AS total_cost
        from 
        (
            SELECT 
                ROUND((sales.bottles_sold*bottles.bottle_cost)::NUMERIC,2) AS cost
            FROM 
                sales
            inner join bottles ON
                sales.bottle_id = bottles.bottle_id
            ORDER BY sales.sale_id
            LIMIT {LINESLIMIT}
        ) AS bottles_cost
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchone()
    if output:
        return output[0]
    return None


def getBottlesKPI():
    global LINESLIMIT
    query = f"""
        SELECT 
            SUM(bottles_sold) AS bottles_sold
        from 
        (
            SELECT 
                sales.bottles_sold
            FROM 
                sales
            ORDER BY sales.sale_id
            LIMIT {LINESLIMIT}
        ) AS bottles_sold
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchone()
    if output:
        return output[0]
    return None


def getProfitKPI():
    global LINESLIMIT
    query = f"""
        SELECT 
            SUM(revenue - cost) AS total_profit
        from 
        (
            SELECT 
                ROUND((sales.bottles_sold*bottles.bottle_retail_price)::NUMERIC,2) AS revenue,
                ROUND((sales.bottles_sold*bottles.bottle_cost)::NUMERIC,2) AS cost
            FROM 
                sales
            inner join bottles ON
                sales.bottle_id = bottles.bottle_id
            ORDER BY sales.sale_id
            LIMIT {LINESLIMIT}
        ) AS bottles_profit
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchone()
    if output:
        return output[0]
    return None


def getSalesKPI():
    global LINESLIMIT
    return LINESLIMIT


# BarChart Data
def getCategoriesData():
    global LINESLIMIT
    query = f"""
        SELECT
            category_name,
            revenue,
            sales,
            cost,
            bottles,
            (revenue-cost) AS profit
        FROM
            (
                SELECT 
                    categories.category_name, 
                    SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_retail_price)::NUMERIC,2)) AS revenue,
                    count(sales_limited.sale_id) AS sales,
                    SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_cost)::NUMERIC,2)) AS cost,
                    SUM(sales_limited.bottles_sold) AS bottles
                FROM 
                    (
                        SELECT 
                            * 
                        FROM 
                            sales 
                        ORDER BY sales.sale_id 
                        LIMIT {LINESLIMIT}
                    ) AS sales_limited
                LEFT JOIN categories ON
                    sales_limited.category_id = categories.category_id
                INNER JOIN bottles ON
                    sales_limited.bottle_id = bottles.bottle_id
                GROUP BY 
                    categories.category_name
                ORDER BY 
                    revenue
                LIMIT 5
            ) AS categories_data
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchall()

    if output:
        column_names = [desc[0] for desc in cur.description]
        df = pd.DataFrame(output, columns=column_names)
        df = df.melt(['category_name'],
                     var_name='names', value_name='Value')
        return df
    return None


def getVendorsData():
    global LINESLIMIT
    query = f"""
        SELECT
            vendor_name AS category_name,
            revenue,
            sales,
            cost,
            bottles,
            (revenue-cost) AS profit
        FROM
        (
            SELECT 
                vendors.vendor_name, 
                SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_retail_price)::NUMERIC,2)) AS revenue,
                count(sales_limited.sale_id) AS sales,
                SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_cost)::NUMERIC,2)) AS cost,
                SUM(sales_limited.bottles_sold) AS bottles
            FROM 
                (
                    SELECT 
                        * 
                    FROM 
                        sales 
                    ORDER BY sales.sale_id 
                    LIMIT {LINESLIMIT}
                ) AS sales_limited
            LEFT JOIN vendors ON
                sales_limited.vendor_id = vendors.vendor_id
            INNER JOIN bottles ON
                sales_limited.bottle_id = bottles.bottle_id
            GROUP BY 
                vendors.vendor_name
            ORDER BY 
                revenue
            LIMIT 5
        ) AS vendors_data
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchall()

    if output:
        column_names = [desc[0] for desc in cur.description]
        df = pd.DataFrame(output, columns=column_names)
        df = df.melt(['category_name'],
                     var_name='names', value_name='Value')
        return df
    return None


def getStoresData():
    global LINESLIMIT
    query = f"""
        SELECT
            store_name AS category_name,
            revenue,
            sales,
            cost,
            bottles,
            (revenue-cost) AS profit
        FROM
        (
            SELECT 
                stores.store_name, 
                SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_retail_price)::NUMERIC,2)) AS revenue,
                count(sales_limited.sale_id) AS sales,
                SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_cost)::NUMERIC,2)) AS cost,
                SUM(sales_limited.bottles_sold) AS bottles
            FROM 
                (
                    SELECT 
                        * 
                    FROM 
                        sales 
                    ORDER BY sales.sale_id 
                    LIMIT {LINESLIMIT}
                ) AS sales_limited
            LEFT JOIN stores ON
                sales_limited.store_id = stores.store_id
            INNER JOIN bottles ON
                sales_limited.bottle_id = bottles.bottle_id
            GROUP BY 
                stores.store_name
            ORDER BY 
                revenue
            LIMIT 5
        ) AS stores_data
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchall()

    if output:
        column_names = [desc[0] for desc in cur.description]
        df = pd.DataFrame(output, columns=column_names)
        df = df.melt(['category_name'],
                     var_name='names', value_name='Value')
        return df
    return None
# END


# bottles and amount of sales per:
# Returns the average amount of sales and bottles sold per month
def salesAndBottlesPerMonth():
    global LINESLIMIT
    query = f"""
        SELECT
            "month",
            ROUND(avg("bottles_sold"),0) AS "bottles_sold",
            ROUND(avg("sales"),0) AS "sales"
        FROM
        (
            SELECT
                EXTRACT(YEAR FROM sale_date) AS "year",
                TO_CHAR(sale_date,'month') AS "month",
                SUM(bottles_sold) AS "bottles_sold",
                COUNT(sale_id) AS "sales"
            FROM 
            (
                SELECT 
                    * 
                FROM 
                    sales 
                ORDER BY sales.sale_id 
                LIMIT {LINESLIMIT}
            ) AS sales_limited
            GROUP BY "year", "month"
            ORDER BY "year", "month"
        ) AS bottles_sold_by_month
        GROUP BY "month"
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchall()
    if output:
        column_names = [desc[0] for desc in cur.description]
        df = pd.DataFrame(output, columns=column_names)
        return df
    return None


# Returns the revenue and cost per month
def revenueAndCostPerMonth():
    global LINESLIMIT
    query = f"""
        WITH sales_limited(sale_id, sale_date, bottle_id, bottles_sold, store_id, category_id, vendor_id)
        AS
        (
            SELECT  
                * 
            FROM 
                sales 
            ORDER BY sales.sale_id 
            LIMIT {LINESLIMIT}
        )
        SELECT
            "month",
            'revenue' AS "category",
            ROUND(avg(revenue),0) AS value
        FROM
        (
            SELECT
                EXTRACT(YEAR FROM sale_date) AS "year",
                TO_CHAR(sale_date,'month') AS "month",
                SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_retail_price)::NUMERIC,2)) AS revenue
            FROM sales_limited
            inner join bottles ON
                sales_limited.bottle_id = bottles.bottle_id
            GROUP BY "year", "month"
            ORDER BY "year", "month"
        ) AS profit_month
        GROUP BY "month"
        UNION
        SELECT
            "month",
            'cost' AS "category",
            ROUND(avg(cost),0) AS value
        FROM
        (
            SELECT
                EXTRACT(YEAR FROM sale_date) AS "year",
                TO_CHAR(sale_date,'month') AS "month",
                SUM(ROUND((sales_limited.bottles_sold*bottles.bottle_cost)::NUMERIC,2)) AS cost
            FROM sales_limited
            inner join bottles ON
                sales_limited.bottle_id = bottles.bottle_id
            GROUP BY "year", "month"
            ORDER BY "year", "month"
        ) AS profit_month
        GROUP BY "month"
    """
    cur = getCursor()
    cur.execute(query)
    output = cur.fetchall()
    if output:
        column_names = [desc[0] for desc in cur.description]
        df = pd.DataFrame(output, columns=column_names)
        return df
    return None
