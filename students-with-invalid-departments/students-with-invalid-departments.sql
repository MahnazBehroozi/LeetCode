# Write your MySQL query statement below
select s.id, s.name from Students as s 
left join Departments as d on d.id = s.department_id
where d.name is NULL
