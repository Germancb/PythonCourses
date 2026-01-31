select orders.orderNumber, productCode, orderDate, quantityOrdered, priceEach from orders, orderdetails where orders.orderNumber=orderdetails.orderNumber order by orders.orderNumber 



