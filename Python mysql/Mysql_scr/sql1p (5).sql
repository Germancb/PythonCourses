select productCode, sum(quantityOrdered) total, avg(quantityOrdered) PROM, COUNT(*) from orderdetails group by productCode order by productCode





