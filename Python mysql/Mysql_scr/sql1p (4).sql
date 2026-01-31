select customerName, orders.orderNumber, orders.customerNumber, orderdetails.productCode from customers, orders, orderdetails where orders.orderNumber= orderdetails.orderNumber and orders.customerNumber=customers.customerNumber order by customerName;




