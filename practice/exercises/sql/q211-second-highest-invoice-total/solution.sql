-- Q211 · Second-highest invoice total
WITH totals AS (
    SELECT InvoiceNo, SUM(Revenue) AS InvoiceTotal
    FROM orders
    GROUP BY InvoiceNo
),
ranked AS (
    SELECT *, DENSE_RANK() OVER (ORDER BY InvoiceTotal DESC) AS rnk
    FROM totals
)
SELECT InvoiceNo, InvoiceTotal
FROM ranked
WHERE rnk = 2;
