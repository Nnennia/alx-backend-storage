# MySQL Advanced
## Using MySQL DELIMITER for stored procedures
    Typically, a stored procedure contains multiple statements separated by semicolons (;). To compile the whole stored procedure as a single compound statement, you need to temporarily change the delimiter from the semicolon (;) to another delimiter such as $$ or //: