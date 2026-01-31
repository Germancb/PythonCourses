select customerNumber, sum(amount) Total, avg(amount) PROM, count(*) from payments group by customerNumber




