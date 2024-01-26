WITH pu_astoria as (
SELECT 
	a.lpep_pickup_datetime,
	a."DOLocationID",
	b."Zone" as pickup_zone,
	a.tip_amount
FROM green_taxi_trips a
INNER JOIN taxi_zone b
ON a."PULocationID" = b."LocationID"
WHERE b."Zone" = 'Astoria' and 
	DATE(a.lpep_pickup_datetime) between '2019-09-01' and '2019-09-30'
)

SELECT d."Zone" 
FROM pu_astoria c
INNER JOIN taxi_zone d
ON c."DOLocationID" = d."LocationID"
ORDER BY tip_amount DESC
LIMIT 1