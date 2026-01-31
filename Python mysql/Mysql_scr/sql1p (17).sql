select orderNumber, orderDate, requiredDate, GREATEST(requiredDate, orderDate), DATEDIFF(requiredDate, orderDate) AS days_between, Sysdate() from orders



