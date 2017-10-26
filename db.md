# table
```
CREATE DATABASE news;

use news;

CREATE TABLE article (
 urlMD5 VARCHAR(32) NOT NULL PRIMARY KEY, /* md5 of url */
 url TEXT NOT NULL, /* target url */
 siteLogoUrl TEXT NOT NULL, /* site logo */
 articleImageUrl TEXT, /* option */
 siteTitleJa TEXT NOT NULL, /* transleted title */
 siteTitleRaw TEXT NOT NULL, /* news article title raw */
 bodyTextJa TEXT NOT NULL, /* transleted */
 bodyTextRaw TEXT NOT NULL, /* raw article body raw */
 langCode VARCHAR(5) NOT NULL, /* ISO-639-1 https://cloud.google.com/translate/docs/languages */
 createdAt timestamp not null default current_timestamp,
 updatedAt timestamp not null default current_timestamp on update current_timestamp
);
```
