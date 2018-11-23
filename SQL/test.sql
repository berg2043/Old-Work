.headers on
.separator ","
.import T-Test.csv raw

-- selecting as ' ID' because csv's error out if the first line is ID lol

SELECT
ID
AS
' ID'
FROM 
raw;