# Write your MySQL query statement below
select u.name, sum(amount) as balance
from Transactions t, Users u
where t.account = u.account
group by t.account having sum(amount)>10000
