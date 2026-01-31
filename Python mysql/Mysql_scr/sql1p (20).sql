select orderdetails.productCode, productName, productScale, sum(quantityOrdered), sum(quantityOrdered*priceEach), count(*) from orderdetails, products where orderdetails.productCode=products.productCode group by(productCode) order by productCode



