select productCode, RPAD(productName, 35, '.'), LPAD(productName, 30, '.'), products.productLine, SUBSTR(textDescription, 1, 20) Linea from products, productlines where products.productLine=productlines.productLine


