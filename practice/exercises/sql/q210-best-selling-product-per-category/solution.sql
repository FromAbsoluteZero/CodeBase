-- Q210 · Best-selling product per category
WITH product AS (
    SELECT Category, Description, SUM(Revenue) AS Revenue
    FROM orders
    GROUP BY Category, Description
),
ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Revenue DESC, Description) AS rn
    FROM product
)
SELECT Category, Description, Revenue
FROM ranked
WHERE rn = 1
ORDER BY Category;
