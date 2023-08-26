DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets; 
-- DROP TABLE owners;

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255), -- use datetime? age int alternative? age(timestamp) function?	
    gender VARCHAR(255),
    species VARCHAR(255),
    contact_details VARCHAR(255),
    treatment_notes VARCHAR(255)
    -- in_treatment BOOLEAN NOT NULL DEFAULT FALSE;
    -- admission_date TIMESTAMPTZ;
    -- feeding_times DATETIME
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    current_pets INT NOT NULL REFERENCES pets(id) ON DELETE CASCADE
    -- owners INT REFERENCES owners(id) ON DELETE CASCADE
);

-- -- CREATE TABLE owners (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(255),
--     last_name VARCHAR(255),
--     pets_owned INT REFERENCE pets(id) ON DELETE CASCADE,
--     contact_info VARCHAR(255)
-- );