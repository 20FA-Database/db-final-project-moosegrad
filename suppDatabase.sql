
create database Supplement_Reviews;

SET GLOBAL validate_password.policy=LOW;

CREATE USER cm_user@localhost IDENTIFIED BY 'pyuser5134';

use mysql;

GRANT SELECT, INSERT, UPDATE, DELETE ON Supplement_Reviews. * TO cm_user@localhost;

use Supplement_Reviews;

CREATE TABLE Reviews( ReviewID INT(200) primary key, SuppID  int(100), BrandID  int(50), ReviewerID  int(30), Stars  int(5) );

Create Table Reviewer( ReviewerID int(30) primary key, NameFirst varchar(30), NameLast varchar(30));

Create table Supplement_Brand( BrandID int(50) Primary key, BrandName varchar(50), Location varchar(150));

Create Table Supplements( SuppID int(100) primary key, BrandID int(50), SuppName varchar(50), SuppType varchar(50));

Insert into Reviewer(ReviewerID, NameFirst, NameLast) values ('1', 'James', 'Smith');

Insert into Reviewer(ReviewerID, NameFirst, NameLast) values ('2', 'Pablo', 'Gonzalez');

Insert into Reviewer(ReviewerID, NameFirst, NameLast) values ('3', 'Katie', 'White');

Insert into Reviewer(ReviewerID, NameFirst, NameLast) values ('4', 'Paige', 'Shaw');

Insert into Reviewer(ReviewerID, NameFirst, NameLast) values ('5', 'Cam', 'Jackson');

insert into Supplement_Brand(BrandID, BrandName, Location) values ('1', 'Nutrex', 'California');

insert into Supplement_Brand(BrandID, BrandName, Location) values ('2', 'First Phorm', 'Ohio');

insert into Supplement_Brand(BrandID, BrandName, Location) values ('3', 'Tim Muller', 'Nevada');

insert into Supplement_Brand(BrandID, BrandName, Location) values ('4','Rule one', 'Indiana');

insert into Supplement_Brand(BrandID, BrandName, Location) values ('5','Dynamic', 'Texas');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('1', '1', 'OutLift', 'Pre Workout');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('2', '1', 'WheyIso', 'Protein');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('3', '2', 'MesoMorph', 'Pre Workout');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('4', '2', 'Iso Whey', 'Protein');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('5', '3', 'Pre Aminos', 'Pre Workout');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('6', '3', 'Natural Whey', 'Protein');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('7', '4', 'Spazmatic', 'Pre Workout');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('8', '4', 'Pump Plus', 'Protein');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('9', '5', 'Savage AF', 'Pre Workout');

insert into Supplements(SuppID, BrandID, SuppName, SuppType) values ('10', '5', 'Natty Whey', 'Protein');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('1', '1', '1', '1', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('2', '2', '1', '1', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('3', '3', '2', '2', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('4', '4', '2', '2', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('5', '4', '2', '1', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('6', '4', '2', '3', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('7', '4', '2', '4', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('8', '4', '2', '5', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('9', '5', '3', '1', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('10', '5', '3', '2', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('11', '5', '3', '3', '1');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('12', '5', '3', '4', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('13', '5', '3', '5', '1');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('14', '6', '3', '1', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('15', '6', '3', '2', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('16', '6', '3', '3', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('17', '7', '4', '4', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('18', '7', '4', '5', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('19', '7', '4', '1', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('20', '8', '4', '1', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('21', '8', '4', '4', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('22', '8', '4', '2', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('23', '9', '5', '1', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('24', '9', '5', '3', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('25', '9', '5', '3', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('26', '10', '5', '2', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('27', '10', '5', '4', '2');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('28', '10', '5', '5', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('29', '1', '1', '5', '4');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('30', '1', '1', '4', '3');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('31', '2', '2', '3', '5');

Insert Into Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) values ('32', '2', '2',' 5', '4');

