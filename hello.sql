-- Da linha 5 até a linha 14 é para buscar no banco de dados
-- bebes acima de uma foto ou perfumaria acima de uma foto.
--
-- select product_id,
--       product_category_name,
--       product_photos_qty
--
-- from tb_products
--
-- where (product_category_name = 'bebes'
--    or product_category_name = 'perfumaria')
--
-- and product_photos_qty > 1

-- Da linha 16 em diante é para buscar bebes com foto maior do que 1 e
-- perfumaria com fotos maior do que 5.

select t1.product_id,
       t1.product_category_name,
       t1.product_photos_qty
-- criando um novo apelido para a tabela
from tb_products t1

where (t1.product_category_name = 'bebes'
       and t1.product_photos_qty > 1)
or (t1.product_category_name = 'perfumaria'
       and t1.product_photos_qty > 5)
