cd .\..\SQL
# some asshole said to just pipe the sqlit3 straight to the csv but this
# leaves unecessary junk in the csv file. set-content just loads the output
Get-Content .\test.sql | sqlite3 | set-content .\..\powershell\testing.csv