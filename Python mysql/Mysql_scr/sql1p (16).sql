select productCode, RPAD(productName, 50, '.') Nombre_Producto, products.productLine LINEA, SUBSTR(textDescription, 1, 30) Descripcion_producto, length(textDescription) from products, productlines where products.productLine=productlines.productLine


