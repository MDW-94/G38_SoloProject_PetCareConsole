DROP TABLE pets;
DROP TABLE vets; 
-- DROP TABLE owners;

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    gender VARCHAR(255),
    species VARCHAR(255),
    contact_details VARCHAR(255),
    treatment_notes VARCHAR(255)
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    current_pets INT REFERENCES pets(id) ON DELETE CASCADE
    -- owners INT REFERENCES owners(id) ON DELETE CASCADE
);

-- -- CREATE TABLE owners (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     pets_owned INT REFERENCE pets(id) ON DELETE CASCADE,
--     contact_info VARCHAR(255)
-- );