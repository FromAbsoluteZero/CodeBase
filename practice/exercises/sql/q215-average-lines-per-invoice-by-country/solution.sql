-- Q215 · Average lines per invoice by country
WITH per_invoice AS (
    SELECT Country, InvoiceNo, COUNT(*) AS Lines
    FROM orders
    GROUP BY Country, InvoiceNo
)
SELECT Country, COUNT(*) AS Invoices, AVG(Lines) AS AvgLines
FROM per_invoice
GROUP BY Country
ORDER BY AvgLines DESC;
