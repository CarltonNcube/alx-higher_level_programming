-- List all cities of California in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states WHERE states.name
= 'california' AND cities.state_id = states.id ORDER BY cities.id ASC;
