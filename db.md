# table
```
CREATE TABLE article (
 ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 id varchar(20),
 originUrl TEXT,
 originCaption varchar(100),
 imageUrl TEXT,
 title varchar(100),
 iconImageUrl TEXT,
 h1 TEXT,
 h2 TEXT,
 h3 TEXT,
 h4 TEXT,
 h5 TEXT
);
```
