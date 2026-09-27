-- Q214 · Counting with NULLs
SELECT COUNT(*) AS TotalRows,
       COUNT(CustomerID) AS WithCustomer,
       SUM(CASE WHEN CustomerID IS NULL THEN 1 ELSE 0 END) AS WithoutCustomer
FROM orders;
