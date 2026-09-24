-- Q213 · Month-over-month growth with LAG
WITH monthly AS (
    SELECT substr(InvoiceDate, 1, 7) AS Month, SUM(Revenue) AS Revenue
    FROM orders
    GROUP BY Month
)
SELECT Month,
       Revenue,
       LAG(Revenue) OVER (ORDER BY Month) AS PrevRevenue,
       (Revenue - LAG(Revenue) OVER (ORDER BY Month))
           / LAG(Revenue) OVER (ORDER BY Month) * 100 AS GrowthPct
FROM monthly
ORDER BY Month;
