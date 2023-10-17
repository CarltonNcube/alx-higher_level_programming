-- Print the full description of the first_table table
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'first_table';
