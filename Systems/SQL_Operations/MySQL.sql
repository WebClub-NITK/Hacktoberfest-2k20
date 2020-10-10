create table smartphones(smartphone_id integer, model_name varchar(50), company varchar(20), price float(10, 2), os varchar(10), release_date date);

insert into smartphones values (1, 'Pixel 3', 'Google', 57000.00, 'Android', '2018-10-09'),
                                (2, 'iPhone XR', 'Apple', 49999.00, 'iOS', '2018-09-12'),
                                (3, 'iPhone 11 Pro', 'Apple', 99900.00, 'iOS', '2019-09-10'),
                                (4, 'Galaxy Note 10 Plus', 'Samsung', 85000.00, 'Android', '2019-08-07'),
                                (5, 'iPhone XS Max', 'Apple', 94999.00, 'iOS', '2018-09-12'),
                                (6, 'Galaxy A50s ', 'Samsung', 19949.00, 'Android', '2019-08-22'),
                                (7, 'Galaxy S9', 'Samsung', 44990.00, 'Android', '2018-03-16'),
                                (8, 'ROG Phone II', 'Asus', 37999.00, 'Android', '2019-09-23'),
                                (9, 'Mi A3', 'Xiaomi', 12999.00, 'Android', '2019-08-21'),
                                (10, 'Galaxy A10', 'Samsung', 7990.00, 'Android', '2019-03-02');

-- Display all smartphones with price less than Rs. 60,000
select * from smartphones where price < 60000;

-- List all smartphones released between 1st March, 2018 to 31st December, 2018
select * from smartphones where release_date BETWEEN '2018-03-01' and '2018-12-31';

-- Find the 2 cheapest smartphones released by Samsung after January 1, 2019 (less expensive one should be displayed first).
select * from smartphones where company='Samsung' and release_date > '2019-01-01' order by price limit 2;