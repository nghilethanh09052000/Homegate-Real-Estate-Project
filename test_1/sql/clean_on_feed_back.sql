SELECT *
FROM homegate_properties
WHERE
    seller_name IS NULL AND
    phone_number IS NULL AND
    email IS NULL AND
    property_type IS NULL AND
    rooms IS NULL AND
    built_year IS NULL AND
    property_address IS NULL AND
    listing_status IS NULL AND
    price IS NULL AND
    property_features IS NULL AND
    property_description IS NULL AND
    local_amenties IS NULL AND
    website IS NULL
;

DELETE FROM homegate_properties
WHERE
    seller_name IS NULL AND
    phone_number IS NULL AND
    email IS NULL AND
    property_type IS NULL AND
    rooms IS NULL AND
    built_year IS NULL AND
    property_address IS NULL AND
    listing_status IS NULL AND
    price IS NULL AND
    property_features IS NULL AND
    property_description IS NULL AND
    local_amenties IS NULL AND
    website IS NULL
;



UPDATE homegate_properties
SET listing_status = "Buy";



SELECT 
	phone_number 
FROM 
	homegate_properties
;


SELECT
	seller_name AS "Name Seller",
	phone_number AS "Phone number",
	email AS "Email",
	property_type AS "Property Type",
	rooms AS "Rooms",
	built_year AS "Built Year",
	property_address AS "Property Address",
	listing_status AS "Listing Status",
	price AS "Price",
	property_features AS "Property Features",
	property_description AS "Property Description",
	local_amenties AS "Local amenities",
	website AS "Website/property URL"
FROM
 	homegate_properties
;
