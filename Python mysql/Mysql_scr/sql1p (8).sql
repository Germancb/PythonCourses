select payments.customerNumber, customerName, sum(amount) Total, avg(amount) PROM, count(*) from payments, customers where payments.customerNumber=customers.customerNumber group by customerNumber 




