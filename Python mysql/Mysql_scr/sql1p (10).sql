select orderNumber, sum(quantityOrdered), sum(quantityOrdered * priceEach) TotalO$, count(*) from orderdetails group by orderNumber order by orderNumber 



