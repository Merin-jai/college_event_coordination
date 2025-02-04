/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.14-MariaDB : Database - py_college_event_coordination
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`py_college_event_coordination` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `py_college_event_coordination`;

/*Table structure for table `club` */

DROP TABLE IF EXISTS `club`;

CREATE TABLE `club` (
  `club_id` int(11) NOT NULL AUTO_INCREMENT,
  `club` varchar(100) DEFAULT NULL,
  `cstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`club_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `club` */

insert  into `club`(`club_id`,`club`,`cstatus`) values (1,'arts','active'),(2,'sports','active'),(4,'rrrr','inactive');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(100) DEFAULT NULL,
  `dstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `department` */

insert  into `department`(`department_id`,`department`,`dstatus`) values (1,'kjhgbb','active'),(3,'njjkk','active'),(4,'kjjkh','active'),(5,'kkk','inactive');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `event` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `edate` varchar(100) DEFAULT NULL,
  `etime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `event` */

insert  into `event`(`event_id`,`teacher_id`,`event`,`details`,`edate`,`etime`) values (1,1,'jejfjr','jjf','2022-01-27','1:30');

/*Table structure for table `eventchild` */

DROP TABLE IF EXISTS `eventchild`;

CREATE TABLE `eventchild` (
  `echild_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) DEFAULT NULL,
  `file_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `resource_qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`echild_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

/*Data for the table `eventchild` */

insert  into `eventchild`(`echild_id`,`event_id`,`file_id`,`type`,`resource_qty`) values (7,1,1,'resource','4'),(8,1,1,'facility','7');

/*Table structure for table `facilities` */

DROP TABLE IF EXISTS `facilities`;

CREATE TABLE `facilities` (
  `facility_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `fstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`facility_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `facilities` */

insert  into `facilities`(`facility_id`,`fname`,`image`,`fstatus`) values (1,'mmnn','static/images/bff687fc-1639-49cd-9730-7ce3384f6e5edownload (2).png','active'),(3,' cmn','static/images/5fe8d332-892c-42cc-bbff-2aa9bda8f9cebg-2.jpg','inactive');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values ('admin','admin','admin'),('athira12@gmail.com','aa','student'),('ben9@gmail.com','ben','teacher'),('a@gmail.com','nn','teacher'),('agh@gmail.com','kkk','reject'),('vilo@mailinator.com','Cum ad omnis laboris','student'),('lebixiq@mailinator.com','Ut ea molestias ea d','student');

/*Table structure for table `resource` */

DROP TABLE IF EXISTS `resource`;

CREATE TABLE `resource` (
  `resource_id` int(11) NOT NULL AUTO_INCREMENT,
  `rname` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `rstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`resource_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `resource` */

insert  into `resource`(`resource_id`,`rname`,`quantity`,`image`,`rstatus`) values (1,'mgbm','3','static/images/4f16b0d4-0ad0-420a-816e-f15ace8376f7download (1).png','active'),(3,' fdmcx','34','static/images/a75d58d7-afd2-44ac-8ba1-4f26abb45a19bg-3.jpg','inactive');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `sstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `student` */

insert  into `student`(`student_id`,`username`,`firstname`,`lastname`,`place`,`phone`,`email`,`sstatus`) values (1,'athira12@gmail.com','Athira','kumar','kochin','9988776612','athira12@gmail.com','active');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `tstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`username`,`department_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`designation`,`tstatus`) values (1,'ben9@gmail.com',3,'benny','k','kollam','9977664433','ben9@gmail.com','proffessor','active'),(3,'agh@gmail.com',4,'ass','L','kollam','9988776655','agh@gmail.com','lkk','inactive');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
