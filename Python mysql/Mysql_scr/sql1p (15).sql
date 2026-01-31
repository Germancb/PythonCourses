create view TotVenxP as select orderdetails.productCode, productName, sum(quantityOrdered), sum(quantityOrdered * priceEach) TotalO$, avg(priceEach), count(*) from orderdetails, products where orderdetails.productCode=products.productCode group by orderdetails.productCode order by productCode


 
