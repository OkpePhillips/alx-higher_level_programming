-- Script that lists all records of the table second_table of the database hbtn_0c_0
-- display the score and the name (in this order).Does not list rows without a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
