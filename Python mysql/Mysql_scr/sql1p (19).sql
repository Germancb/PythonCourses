select orderdetails.productCode, sum(quantityOrdered), sum(quantityOrdered*priceEach), count(*) N_Ordenes from orderdetails group by orderdetails.productCode order by productCode



