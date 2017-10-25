# table
```
CREATE DATABASE news;

CREATE TABLE article (
 created_at timestamp not null default current_timestamp,
 updated_at timestamp not null default current_timestamp on update current_timestamp,
 id varchar(20),
 originUrl TEXT,
 originCaption varchar(100),
 imageUrl TEXT,
 title TEXT,
 iconImageUrl TEXT,
 h1en TEXT,
 h1ja TEXT,
 h2en TEXT,
 h2ja TEXT,
 h3ja TEXT,
 h3en TEXT,
 h4ja TEXT,
 h4en TEXT,
 h5ja TEXT,
 h5en TEXT
);
```
