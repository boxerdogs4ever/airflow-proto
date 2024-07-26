CREATE TABLE IF NOT EXISTS patient
(
    ID SERIAL PRIMARY KEY,
    name VARCHAR(255),
    disease VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS patient_variant
(
    ID SERIAL PRIMARY KEY,
    patient_ID INTEGER,
    ncbi_id VARCHAR(255),
    depth_of_coverage INTEGER
);
CREATE TABLE IF NOT EXISTS ncbi_variant
(
    ID SERIAL PRIMARY KEY,
    ncbi_id VARCHAR(255),
    gene VARCHAR(255),
    locus VARCHAR(255)
);


-- insert into patient (name, disease) values ('John Ton', 'colorectal cancer');
-- insert into patient (name, disease) values ('Mary Contrary', 'crohn disease');
