# Write your MySQL query statement below
select w.name as warehouse_name, sum((p.Width*p.Length*p.Height)*w.Units) as volume
from Warehouse w
join Products p
where p.product_id = w.product_id
group by w.name
​
