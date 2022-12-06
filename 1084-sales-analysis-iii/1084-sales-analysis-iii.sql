select distinct sales.product_id, product_name
from product, sales
where product.product_id = sales.product_id and
    sales.product_id not in (
        select sales.product_id
        from product, sales
        where product.product_id = sales.product_id and
            not(
                year(sale_date) = 2019 and
                month(sale_date) >= 1 and
                month(sale_date) <= 3
            )
    )