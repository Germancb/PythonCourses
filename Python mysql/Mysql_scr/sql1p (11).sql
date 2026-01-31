select productCode, sum(quantityOrdered) Totalq, sum(quantityOrdered * priceEach) TotalO$, count(*)  from orderdetails group by productCode order by productCode



