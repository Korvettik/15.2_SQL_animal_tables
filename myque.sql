CREATE TABLE IF NOT EXISTS types
    (
    ID_type INTEGER PRIMARY KEY AUTOINCREMENT, 
    animal_type TEXT 
    );

CREATE TABLE IF NOT EXISTS breeds 
    (
    ID_breed INTEGER PRIMARY KEY AUTOINCREMENT, 
    breed TEXT
    );

CREATE TABLE IF NOT EXISTS outcome_types 
    (
    ID_outcome_types INTEGER PRIMARY KEY AUTOINCREMENT, 
    outcome_types TEXT
    );

CREATE TABLE IF NOT EXISTS colors 
    (
    ID_color INTEGER PRIMARY KEY AUTOINCREMENT, 
    color1 TEXT
    );

CREATE TABLE IF NOT EXISTS outcome_subtype 
    (
    ID_outcome_subtype INTEGER PRIMARY KEY AUTOINCREMENT, 
    outcome_subtype TEXT
    );

CREATE TABLE IF NOT EXISTS animals_new
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age_upon_outcome TEXT,
    animal_id TEXT,
    name TEXT,
    date_of_birth TEXT,
    outcome_month INTEGER,
    outcome_year INTEGER,
    
    
    type_id INTEGER,
    breed_id INTEGER,
    color_id INTEGER,
    outcome_subtype_id INTEGER,
    outcome_type_id INTEGER,
    
    FOREIGN KEY (type_id) REFERENCES types(ID_type) ON DELETE CASCADE,
    FOREIGN KEY (breed_id) REFERENCES breeds(ID_breed) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(ID_color) ON DELETE CASCADE,
    FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtype(ID_outcome_subtype) ON DELETE CASCADE,
    FOREIGN KEY (outcome_type_id) REFERENCES outcome_types(ID_outcome_types) ON DELETE CASCADE
    );

INSERT INTO types (animal_type)
SELECT DISTINCT animal_type
FROM animals;

INSERT INTO types (animal_type)
SELECT DISTINCT animal_type
FROM animals;

INSERT INTO breeds (breed)
SELECT DISTINCT breed
FROM animals;

INSERT INTO colors (color1) 
SELECT DISTINCT color1
FROM animals;

INSERT INTO outcome_subtype (outcome_subtype)
SELECT DISTINCT outcome_subtype
FROM animals;

INSERT INTO outcome_types(outcome_types)
SELECT DISTINCT outcome_type
FROM animals;

INSERT INTO animals_new
(
age_upon_outcome,
animal_id,
name,
date_of_birth,
outcome_month,
outcome_year,
type_id,
breed_id,
color_id,
outcome_subtype_id,
outcome_type_id
)
SELECT
age_upon_outcome,
animal_id,
name,
date_of_birth,
outcome_month,
outcome_year,
ID_type,
ID_breed,
ID_color,
ID_outcome_subtype,
ID_outcome_types
FROM animals
LEFT JOIN types
ON animals.animal_type = types.animal_type
LEFT JOIN breeds
ON animals.breed = breeds.breed
LEFT JOIN colors
ON animals.color1 = colors.color1
LEFT JOIN outcome_subtype
ON animals.outcome_subtype = outcome_subtype.outcome_subtype
LEFT JOIN outcome_types
ON animals.outcome_type = outcome_types.outcome_types;
