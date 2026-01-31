select orders.customerNumber, customerName, sum(quantityOrdered*priceEach) $Ordenados, count(*) from orders LEFT JOIN customers on orders.customerNumber=customers.customerNumber, orderdetails where orders.orderNumber=orderdetails.orderNumber group by customerNumber 



