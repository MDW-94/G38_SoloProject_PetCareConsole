DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets; 
-- DROP TABLE owners;

CREATE TABLE vets (
    vet_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
    -- owners INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE
    -- registered_owners 
);

CREATE TABLE pets (
    pet_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255), -- use datetime? age int alternative? age(timestamp) function?	
    gender VARCHAR(255),
    species VARCHAR(255),
    contact_details VARCHAR(255),
    treatment_notes VARCHAR(255),
    admission_date VARCHAR(255),
    vet_id INT REFERENCES vets(vet_id) ON DELETE CASCADE

    -- in_treatment BOOLEAN NOT NULL DEFAULT FALSE;
    -- feeding_times DATETIME
    -- discharge_date TIMESTAMP
);


-- -- CREATE TABLE owners (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(255),
--     last_name VARCHAR(255),
--     FOREIGN KEY (pets_owned) INT NOT NULL REFERENCE pets(id) ON DELETE CASCADE,
--     contact_info VARCHAR(255),
--     registered BOOLEAN DEFAULT FALSE,
--     FOREIGN KEY(registered_vet) INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
-- -- );

-- pet_registration table?
-- owner_registration table?