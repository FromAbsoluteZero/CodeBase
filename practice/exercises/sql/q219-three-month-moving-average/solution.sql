-- Q219 · Three-month moving average
WITH monthly AS (
    SELECT substr(InvoiceDate, 1, 7) AS Month, SUM(Revenue) AS Revenue
    FROM orders
    GROUP BY Month
)
SELECT Month,
       Revenue,
       AVG(Revenue) OVER (
           ORDER BY Month
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS MovingAvg3
FROM monthly
ORDER BY Month;
