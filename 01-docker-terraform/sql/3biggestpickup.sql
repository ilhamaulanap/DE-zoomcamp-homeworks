WITH pickup_amount as
(SELECT b."Borough", SUM (a.total_amount) as total_amount 
FROM green_taxi_trips a
INNER JOIN taxi_Zone b
ON a."PULocationID" = b."LocationID"
WHERE DATE(a.lpep_pickup_datetime) = '2019-09-18' 
GROUP BY b."Borough"
ORDER BY total_amount
)

SELECT "Borough" FROM pickup_amount WHERE total_amount > 50000
ORDER BY total_amount DESC