-- lists the number of records with the same score in the table second_table

SELECT score FROM second_table COUNT(`score`) AS number
GROUP BY score
ORDER BY score DESC;
