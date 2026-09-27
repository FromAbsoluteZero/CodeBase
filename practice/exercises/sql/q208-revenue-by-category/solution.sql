-- Q208 · Revenue by category
SELECT Category, SUM(Revenue) AS Revenue
FROM orders
GROUP BY Category
ORDER BY Revenue DESC;
