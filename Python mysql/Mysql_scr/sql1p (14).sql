select productCode, productName from products where products.productCode not in (select productCode from orderdetails group by productCode)

 

