SELECT
    SUM(CASE WHEN CAST(code AS INTEGER) >= 1000 AND CAST(code AS INTEGER) <= 1999 THEN 1 ELSE 0 END) AS code_1000_1999,
    SUM(CASE WHEN CAST(code AS INTEGER) >= 2000 AND CAST(code AS INTEGER) <= 2999 THEN 1 ELSE 0 END) AS code_2000_2999,
    SUM(CASE WHEN CAST(code AS INTEGER) >= 3000 AND CAST(code AS INTEGER) <= 3999 THEN 1 ELSE 0 END) AS code_3000_3999,
	SUM(CASE WHEN CAST(code AS INTEGER) >= 4000 AND CAST(code AS INTEGER) <= 4999 THEN 1 ELSE 0 END) AS code_4000_4999,
	SUM(CASE WHEN CAST(code AS INTEGER) >= 5000 AND CAST(code AS INTEGER) <= 5999 THEN 1 ELSE 0 END) AS code_5000_5999,
	SUM(CASE WHEN CAST(code AS INTEGER) >= 6000 AND CAST(code AS INTEGER) <= 6999 THEN 1 ELSE 0 END) AS code_6000_6999,
    SUM(CASE WHEN CAST(code AS INTEGER) >= 7000 AND CAST(code AS INTEGER) <= 7999 THEN 1 ELSE 0 END) AS code_7000_7999,
	SUM(CASE WHEN CAST(code AS INTEGER) >= 8000 AND CAST(code AS INTEGER) <= 8999 THEN 1 ELSE 0 END) AS code_8000_8999,
	SUM(CASE WHEN CAST(code AS INTEGER) >= 9000 AND CAST(code AS INTEGER) <= 9999 THEN 1 ELSE 0 END) AS code_9000_9999
FROM homegate_urls
;

/* ----------------------------------------- */

SELECT url,code FROM homegate_urls;

/* ----------------------------------------- */

SELECT 
	code,
	COUNT(code)
FROM
	homegate_categories
GROUP BY code
HAVING CAST(code AS INTEGER) >= 9000 AND CAST(code AS INTEGER) <= 9999
ORDER BY code DESC
;

/* ----------------------------------------- */

SELECT
	homegate_urls.url,
	homegate_categories.code
FROM 
	homegate_urls
RIGHT JOIN 
	homegate_categories
ON homegate_urls.code = homegate_categories.code
ORDER BY homegate_categories.code
;





