-- Q217 · Running total with a frame
WITH monthly AS (
    SELECT substr(InvoiceDate, 1, 7) AS Month, SUM(Revenue) AS Revenue
    FROM orders
    GROUP BY Month
)
SELECT Month,
       Revenue,
       SUM(Revenue) OVER (
           ORDER BY Month
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS RunningTotal
FROM monthly
ORDER BY Month;
