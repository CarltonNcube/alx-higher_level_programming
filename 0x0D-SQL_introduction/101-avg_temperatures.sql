-- Calculate the average temperature in Fahrenheit by city
SELECT city,
       AVG((temperature - 32) * 5/9) AS avg_temperature_fahrenheit
FROM `temperatures`
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;

