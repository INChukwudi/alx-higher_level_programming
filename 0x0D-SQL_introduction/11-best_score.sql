-- Script that lists all records of the table `second_table` and orders them in MySQL
-- Records listed hvae score >= 10
SELECT `score`, `name` FROM `second_table` 
WHERE `score` >= 10 ORDER BY `score` DESC;
