-- Q216 · Frequent customers
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS Invoices,
       SUM(Revenue) AS Revenue
FROM orders
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
HAVING COUNT(DISTINCT InvoiceNo) >= 5
ORDER BY Revenue DESC;
