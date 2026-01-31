select orderNumber, customerNumber from orders where customerNumber in (select customerNumber from customers)





