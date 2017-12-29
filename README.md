# owl
Owl is a search engine made purely in python

I created this repository for learning purpose


-----------------------------------------------

Some unformatted info:

create table searchEngine.info (infoId INT NOT NULL AUTO_INCREMENT,main varchar(500), additional varchar(100), url varchar(2048), PRIMARY KEY (infoID));


mysql> describe searchEngine.info; 
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| infoId     | int(11)       | NO   | PRI | NULL    | auto_increment |
| main       | varchar(500)  | YES  |     | NULL    |                |
| additional | varchar(100)  | YES  |     | NULL    |                |
| url        | varchar(2048) | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)



mysql -u search -p
search@123



Owl search engines features:

1. Will see what other search engines can't see: It will visit the links/file path mentioned information column of database.
2. When an owl hears something that gets its attention, it turns its head left and right and up and down until it homes in on the sound. ----> Search engine should continously talk to the user in order to find what he wants, OwlSearch will tell user what it understood from the search query and will ask user if it was correct or not. ( and maybe learn accordingly in future).
3. 
