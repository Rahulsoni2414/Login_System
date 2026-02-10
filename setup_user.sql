-- Create user if not exists
CREATE USER IF NOT EXISTS 'college'@'localhost' IDENTIFIED BY 'Soni@1530';

-- Grant privileges
GRANT ALL PRIVILEGES ON COLLEGE.* TO 'college'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
