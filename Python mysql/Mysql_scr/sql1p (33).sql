SELECT productName, quantityInStock,
	CASE
		when quantityInStock <=100 then 'Menos de 100'  
        when quantityInStock <=1000 then 'Menos de 1000'  
        when quantityInStock <=2000 then 'Menos de 2000' 
        else 'Stock mayor a 2000'
	END as Cabtudad_en_Inv
FROM classicalmodels.products;