select orderdetails.orderNumber, orderdetails.productCode, products.productName, products.productLine, productlines.image from orderdetails, products, productlines where orderdetails.productCode=products.ProductCode order by orderNumber;


