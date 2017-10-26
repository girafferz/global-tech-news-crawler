# table
```
CREATE DATABASE news;

use news;

CREATE TABLE article (
 createdAt timestamp not null default current_timestamp,
 updatedAt timestamp not null default current_timestamp on update current_timestamp,
 url TEXT NOT NULL PRIMARY KEY,
 siteLogoUrl TEXT NOT NULL,
 articleImageUrl TEXT NOT NULL,
 siteTitle TEXT NOT NULL,
 bodyTextJa TEXT NOT NULL,
 bodyTextRaw TEXT NOT NULL
);
```
