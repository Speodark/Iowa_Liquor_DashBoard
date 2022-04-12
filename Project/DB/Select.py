import pandas as pd
from DB.Connection import getCursor

LINESLIMIT = 10000


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
