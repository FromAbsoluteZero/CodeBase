-- Q212 · Deduplicate with ROW_NUMBER
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY InvoiceNo, StockCode, Description, Category, Quantity,
                            InvoiceDate, UnitPrice, CustomerID, Country
           ) AS rn
    FROM orders
)
SELECT COUNT(*) AS RowsAfter
FROM ranked
WHERE rn = 1;
