select orders.customerNumber, customerName, sum(quantityOrdered), sum(quantityOrdered*priceEach), count(*) from orders, orderdetails, customers where orders.orderNumber=orderdetails.orderNumber and orders.customerNumber=customers.customerNumber group by(customerNumber) order by customerNumber



