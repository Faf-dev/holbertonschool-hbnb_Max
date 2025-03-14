USE hbnb_db;

SHOW DATABASES;

-- Amenity Table
INSERT INTO Amenity (id, name) VALUES (
    '88e44a66-2334-46c2-8e42-172c44cbfabb',
    'Dishwasher'
);
SELECT * FROM Amenity;

-- Update test
UPDATE Amenity SET id='44ba1fb9-5ccc-4785-8cc8-dbe4bf429388' 
WHERE id='88e44a66-2334-46c2-8e42-172c44cbfabb';
SELECT * FROM Amenity;


-- USER Table
INSERT INTO User (id, first_name, last_name, email, password, is_admin) VALUES (
    '8734e5dc-7eb8-44d8-b23c-186665fefd40',
    'John',
    'Doe',
    'john.doe@exemple.com',
    '$2a$12$gBfD1.yGNRwwbvk2ArNvNOdxrFPKP1j8ljferprBZsBscBk8n3pE.',
    FALSE
);
SELECT * FROM User;

-- Update test
UPDATE User SET first_name='Jhon' WHERE first_name='John';
SELECT first_name FROM User;


--
-- PLACE Table
--
INSERT INTO Place (id, title, description, price, latitude, longitude, owner_id) VALUES (
    '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89',
    'Cozy tiny house',
    'A beautifull tiny house made of woods',
    150.5,
    -43.23,
    163.043,
    '8734e5dc-7eb8-44d8-b23c-186665fefd40' -- Owner is Jhon
);
INSERT INTO Place (id, title, description, price, latitude, longitude, owner_id) VALUES (
    '3e45c288-b79d-4be3-8b4d-1896003ecdc5', 
    'CR7 house',
    'The real CR7 house',
    8.03,
    -73.821,
    47.4,
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1' -- Owner is Admin
);
SELECT * FROM Place;

-- Update test
UPDATE Place SET description='A beautifull tiny house made of rocks' 
WHERE id = '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89';
SELECT description FROM Place WHERE id='65cee8dd-df40-4e8b-bacd-e4a28ab6fb89';


--
-- REVIEW Table
--
INSERT INTO Review (id, text, rating, user_id, place_id) VALUES (
    'd3b976b5-8977-4eeb-a6a8-e3bd1082f1fd',
    'A great place to stay in!',
    5,
    '8734e5dc-7eb8-44d8-b23c-186665fefd40',
    '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89' -- Cozy tiny house
);
SELECT * FROM Review;

-- Update test
UPDATE Review SET rating=3 WHERE rating=5;
SELECT rating FROM Review;


--
-- Place_Amenity Table
--
INSERT INTO Place_Amenity (place_id, amenity_id) VALUES (
    '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89', -- 'Cozy tiny house'
    '44ba1fb9-5ccc-4785-8cc8-dbe4bf429388' -- add Dishwasher
);
INSERT INTO Place_Amenity (place_id, amenity_id) VALUES (
    '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89', -- 'Cozy tiny house'
    'ac1bb5af-70dd-41a4-85d5-55df15f28b8b' -- add swimming pool
);
INSERT INTO Place_Amenity (place_id, amenity_id) VALUES (
    '3e45c288-b79d-4be3-8b4d-1896003ecdc5', -- 'CR7 House'
    'ac1bb5af-70dd-41a4-85d5-55df15f28b8b' -- add swimming pool
);
SELECT * FROM Place_Amenity;

-- Update test
UPDATE Place_Amenity SET amenity_id='06383743-20e8-4280-91a5-e29c932a27bc' 
WHERE amenity_id='ac1bb5af-70dd-41a4-85d5-55df15f28b8b'; -- Replace swimming pool by Air conditioning

SELECT Place.id AS place_id, Place.title, Amenity.name AS amenity
FROM Place
JOIN Place_Amenity ON Place.id = Place_Amenity.place_id
JOIN Amenity ON Place_Amenity.amenity_id = Amenity.id; -- List of amenity linked to Places

--
-- Delete test
--
DELETE FROM Review WHERE user_id='8734e5dc-7eb8-44d8-b23c-186665fefd40'; -- Del 'A great place to stay in!
SELECT * FROM Review;

DELETE FROM User WHERE first_name='Jhon'; -- Del user Jhon
SELECT * FROM User;

DELETE FROM Amenity WHERE id='44ba1fb9-5ccc-4785-8cc8-dbe4bf429388'; -- Del Dishwasher
SELECT * FROM Place_Amenity; -- See if the relation's gone
SELECT * FROM Amenity;

DELETE FROM Place WHERE title='Cozy tiny house'; -- Del cozy tiny house
SELECT * FROM Place;

DELETE FROM Place WHERE title='CR7 house'; -- Del CR7 house
SELECT * FROM Place;
SELECT * FROM Place_Amenity; -- See if the ON DELETE CASCADE works
