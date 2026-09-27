-- Q209 · Filter rows, then filter groups
SELECT Country, SUM(Revenue) AS BeansRevenue
FROM orders
WHERE Category = 'Beans'
GROUP BY Country
HAVING SUM(Revenue) > 6000
ORDER BY BeansRevenue DESC;
