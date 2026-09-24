-- Q218 · Gross and net by month with CASE
SELECT substr(InvoiceDate, 1, 7) AS Month,
       SUM(CASE WHEN InvoiceNo NOT LIKE 'C%' THEN Revenue ELSE 0 END) AS Gross,
       SUM(Revenue) AS Net
FROM orders
GROUP BY Month
ORDER BY Month;
