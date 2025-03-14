USE hbnb_db;

SHOW DATABASES;

-- Amenity Table
INSERT INTO Amenity (id, name) VALUES (
    '88e44a66-2334-46c2-8e42-172c44cbfabb',
    'Dishwasher'
);
SELECT * FROM Amenity;
UPDATE Amenity SET id='44ba1fb9-5ccc-4785-8cc8-dbe4bf429388' WHERE id='88e44a66-2334-46c2-8e42-172c44cbfabb';
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
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1'
);
SELECT * FROM Place;

-- Update test
UPDATE Place SET description='A beautifull tiny house made of rocks' WHERE id = '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89';
SELECT description FROM Place WHERE id='65cee8dd-df40-4e8b-bacd-e4a28ab6fb89';

--
-- REVIEW Table
--

INSERT INTO Review (id, text, rating, user_id, place_id) VALUES (
    'd3b976b5-8977-4eeb-a6a8-e3bd1082f1fd',
    'A great place to stay in!',
    5,
    '8734e5dc-7eb8-44d8-b23c-186665fefd40',
    '65cee8dd-df40-4e8b-bacd-e4a28ab6fb89'
);
SELECT * FROM Review;

-- Update test
UPDATE Review SET rating=3 WHERE rating=5;
SELECT rating FROM Review;

-- Delete test
DELETE FROM Review WHERE user_id='8734e5dc-7eb8-44d8-b23c-186665fefd40';
SELECT * FROM Review;

DELETE FROM Place WHERE title='Cozy tiny house';
SELECT * FROM Place;

DELETE FROM User WHERE first_name='Jhon';
SELECT * FROM User;

DELETE FROM Amenity WHERE id='44ba1fb9-5ccc-4785-8cc8-dbe4bf429388';
SELECT * FROM Amenity;