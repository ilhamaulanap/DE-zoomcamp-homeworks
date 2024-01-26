SELECT 
DATE(lpep_pickup_datetime) as date
FROM green_taxi_trips
WHERE trip_distance = (SELECT MAX(trip_distance) FROM green_taxi_trips)

--OR

SELECT 
DATE(lpep_pickup_datetime) as date
FROM green_taxi_trips
ORDER BY trip_distance DESC
LIMIT 1