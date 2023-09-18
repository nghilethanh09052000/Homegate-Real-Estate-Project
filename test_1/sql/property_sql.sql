--DROP TABLE homegate_properties;
CREATE TABLE IF NOT EXISTS homegate_properties (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL UNIQUE,
    seller_name VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(255),
    property_type VARCHAR(255),
    rooms VARCHAR(255),
    built_year VARCHAR(255),
    property_address VARCHAR(255),
    listing_status VARCHAR(255),
    price VARCHAR(255),
    property_features TEXT,
    property_description TEXT,
    local_amenties TEXT,
    website VARCHAR(255),
    available_from VARCHAR(255),
    floors VARCHAR(255),
    number_of_floors VARCHAR(255),
    number_of_apartments VARCHAR(255),
    surface_living_m2 VARCHAR(255),
    floor_space_m2 VARCHAR(255),
    land_area_m2 VARCHAR(255),
    volume_m3 VARCHAR(255),
    room_height_m VARCHAR(255),
    last_refurbishment VARCHAR(255)
);

-- COPY public.homegate_properties (url, seller_name, phone_number, email, property_type, rooms, built_year, property_address, listing_status, price, property_features, property_description, local_amenties, website, available_from, floors, number_of_floors, number_of_apartments, surface_living_m2, floor_space_m2, land_area_m2, volume_m3, room_height_m, last_refurbishment)
-- FROM 'D:/Work/TestUpwork/test_1/2_properties/project/data/data_version_1.csv' DELIMITER ',' CSV HEADER QUOTE '"' ESCAPE E'\\';


/* -------- Update command to null value instead of 'null' string ---------- */
UPDATE homegate_properties
SET
    url = NULLIF(url, 'null'),
    seller_name = NULLIF(seller_name, 'null'),
    phone_number = NULLIF(phone_number, 'null'),
    email = NULLIF(email, 'null'),
    property_type = NULLIF(property_type, 'null'),
    rooms = NULLIF(rooms, 'null'),
    built_year = NULLIF(built_year, 'null'),
    property_address = NULLIF(property_address, 'null'),
    listing_status = NULLIF(listing_status, 'null'),
    price = NULLIF(price, 'null'),
    property_features = NULLIF(property_features, 'null'),
    property_description = NULLIF(property_description, 'null'),
    local_amenties = NULLIF(local_amenties, 'null'),
    website = NULLIF(website, 'null'),
    available_from = NULLIF(available_from, 'null'),
    floors = NULLIF(floors, 'null'),
    number_of_floors = NULLIF(number_of_floors, 'null'),
    number_of_apartments = NULLIF(number_of_apartments, 'null'),
    surface_living_m2 = NULLIF(surface_living_m2, 'null'),
    floor_space_m2 = NULLIF(floor_space_m2, 'null'),
    land_area_m2 = NULLIF(land_area_m2, 'null'),
    volume_m3 = NULLIF(volume_m3, 'null'),
    room_height_m = NULLIF(room_height_m, 'null'),
    last_refurbishment = NULLIF(last_refurbishment, 'null')
;

/* -------- Change Data Type of last_refurebishment and year_built to INTEGER ---------- */

SELECT LENGTH(built_year) FROM homegate_properties WHERE LENGTH(built_year) > 4;
SELECT LENGTH(last_refurbishment) FROM homegate_properties WHERE LENGTH(built_year) > 4;

ALTER TABLE homegate_properties
	ALTER COLUMN built_year TYPE INT
	USING built_year::integer;
	
ALTER TABLE homegate_properties
	ALTER COLUMN last_refurbishment TYPE INT
	USING last_refurbishment::integer;

/* -------- Change Data Type of Columns below to NUMERIC ---------- */
SELECT 
    rooms,
    floors,
    number_of_floors,
    number_of_apartments,
    surface_living_m2,
    floor_space_m2,
    land_area_m2,
    volume_m3,
    room_height_m
FROM 
    homegate_properties
WHERE
    rooms !~ '^[0-9.]+$'
    OR floors !~ '^[0-9.]+$'
    OR number_of_floors !~ '^[0-9.]+$'
    OR number_of_apartments !~ '^[0-9.]+$'
    OR surface_living_m2 !~ '^[0-9.]+$'
    OR floor_space_m2 !~ '^[0-9.]+$'
    OR land_area_m2 !~ '^[0-9.]+$'
    OR volume_m3 !~ '^[0-9.]+$'
    OR room_height_m !~ '^[0-9.]+$'
;

UPDATE homegate_properties
SET
    floors = NULLIF(floors, 'GF')
;

ALTER TABLE homegate_properties;
    ALTER COLUMN rooms TYPE NUMERIC USING rooms::NUMERIC,
    ALTER COLUMN floors TYPE NUMERIC USING floors::NUMERIC,
    ALTER COLUMN number_of_floors TYPE NUMERIC USING number_of_floors::NUMERIC,
    ALTER COLUMN number_of_apartments TYPE NUMERIC USING number_of_apartments::NUMERIC,
    ALTER COLUMN surface_living_m2 TYPE NUMERIC USING surface_living_m2::NUMERIC,
    ALTER COLUMN floor_space_m2 TYPE NUMERIC USING floor_space_m2::NUMERIC,
    ALTER COLUMN land_area_m2 TYPE NUMERIC USING land_area_m2::NUMERIC,
    ALTER COLUMN volume_m3 TYPE NUMERIC USING volume_m3::NUMERIC,
    ALTER COLUMN room_height_m TYPE NUMERIC USING room_height_m::NUMERIC
;

/* -------- Update On Request Price to Null ---------- */

SELECT 
 	price,
	COUNT(price)
FROM 
	homegate_properties
GROUP BY
	price
HAVING price !~ '^[0-9,]+$'
;

UPDATE homegate_properties
SET
    price = NULLIF(price, 'On request')
;

SELECT 
	COUNT(CASE WHEN phone_number LIKE '%+%' THEN phone_number ELSE NULL END) AS phone_number_with_plus,
	COUNT(CASE WHEN phone_number NOT LIKE '%+%' THEN phone_number ELSE NULL END) AS phone_number,
	COUNT(CASE WHEN phone_number IS NULL THEN phone_number ELSE NULL END) AS not_phone
FROM 
	homegate_properties
;



SELECT phone_number, COUNT(phone_number) FROM homegate_properties GROUP BY phone_number;


