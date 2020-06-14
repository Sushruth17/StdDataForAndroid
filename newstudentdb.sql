-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2020 at 02:22 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `studentdb`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser` (IN `p_name` VARCHAR(20), IN `p_username` VARCHAR(20), IN `p_password` VARCHAR(20))  BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `branchinfo`
--

CREATE TABLE `branchinfo` (
  `id` int(11) NOT NULL,
  `Name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branchinfo`
--

INSERT INTO `branchinfo` (`id`, `Name`) VALUES
(1, 'CSE'),
(2, 'ECE'),
(3, 'ISE');

-- --------------------------------------------------------

--
-- Table structure for table `marksinfo`
--

CREATE TABLE `marksinfo` (
  `id` int(11) NOT NULL,
  `Marks` int(11) DEFAULT NULL,
  `Sid` int(11) DEFAULT NULL,
  `Subid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `marksinfo`
--

INSERT INTO `marksinfo` (`id`, `Marks`, `Sid`, `Subid`) VALUES
(1, 78, 1, 1),
(2, 89, 1, 2),
(3, 86, 1, 3),
(4, 65, 1, 4),
(5, 67, 2, 1),
(6, 76, 2, 2),
(7, 98, 2, 3),
(8, 46, 2, 4),
(9, 67, 3, 1),
(10, 45, 3, 2),
(11, 98, 3, 3),
(12, 56, 3, 4),
(13, 86, 4, 1),
(14, 57, 4, 2),
(15, 89, 4, 3),
(16, 69, 4, 4),
(17, 95, 5, 1),
(18, 87, 5, 2),
(19, 67, 5, 3),
(20, 97, 5, 4),
(21, 56, 6, 1),
(22, 86, 6, 2),
(23, 89, 6, 3),
(24, 59, 6, 4),
(26, 76, 7, 1),
(27, 46, 7, 2),
(28, 78, 7, 3),
(29, 87, 7, 4),
(30, 75, 8, 1),
(31, 65, 8, 2),
(32, 55, 8, 3),
(33, 95, 8, 4),
(34, 42, 9, 1),
(35, 62, 9, 2),
(36, 57, 9, 3),
(37, 86, 9, 4),
(38, 95, 10, 1),
(39, 94, 10, 2),
(40, 67, 10, 3),
(41, 89, 10, 4),
(42, 45, 11, 1),
(43, 98, 11, 2),
(44, 78, 11, 3),
(45, 56, 11, 4),
(46, 43, 12, 1),
(47, 98, 12, 2),
(48, 45, 12, 3),
(49, 78, 12, 4),
(50, 75, 13, 1),
(51, 85, 13, 2),
(52, 76, 13, 3),
(53, 87, 13, 4),
(54, 67, 14, 1),
(55, 95, 14, 2),
(56, 75, 14, 3),
(57, 65, 14, 4),
(58, 98, 15, 1),
(59, 68, 15, 2),
(60, 78, 15, 3),
(61, 75, 15, 4),
(62, 66, 16, 1),
(63, 98, 16, 2),
(64, 87, 16, 3),
(65, 68, 16, 4),
(66, 56, 17, 1),
(67, 35, 17, 2),
(68, 78, 17, 3),
(69, 85, 17, 4),
(70, 46, 18, 1),
(71, 96, 18, 2),
(72, 58, 18, 3),
(73, 87, 18, 4),
(74, 65, 19, 1),
(75, 56, 19, 2),
(76, 86, 19, 3),
(78, 86, 19, 4),
(79, 92, 20, 1),
(80, 87, 20, 2),
(81, 97, 20, 3),
(82, 68, 20, 4);

-- --------------------------------------------------------

--
-- Table structure for table `seminfo`
--

CREATE TABLE `seminfo` (
  `id` int(11) NOT NULL,
  `Sem` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seminfo`
--

INSERT INTO `seminfo` (`id`, `Sem`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);

-- --------------------------------------------------------

--
-- Table structure for table `studentinfo`
--

CREATE TABLE `studentinfo` (
  `id` int(11) NOT NULL,
  `Name` varchar(40) DEFAULT NULL,
  `Address` varchar(40) DEFAULT NULL,
  `ParentName` varchar(40) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Bid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentinfo`
--

INSERT INTO `studentinfo` (`id`, `Name`, `Address`, `ParentName`, `Age`, `Bid`) VALUES
(1, 'Arun', 'vijaynagar', 'Adams', 20, 1),
(2, 'James', 'malleshwaram', 'Campbell', 21, 1),
(3, 'Joshua', 'hosahalli', 'Phillips', 20, 1),
(4, 'Samuel', 'yelahanka', 'Robert', 21, 1),
(5, 'Joseph', 'rajajinagar', 'Patterson', 20, 1),
(6, 'Thomas', 'bnagar', 'Mcdonald', 21, 1),
(7, 'Matthew', 'majestic', 'Chris', 20, 1),
(8, 'Jack', 'jayanagar', 'Jordan', 21, 3),
(9, 'Daniel', 'chordroad', 'Burns', 20, 3),
(10, 'Butler', 'maagdiroad', 'Harrison', 21, 3),
(11, 'Oliver', 'krpuram', 'Craig', 20, 3),
(12, 'Bell', 'gnagar', 'Robertson', 21, 3),
(13, 'Benjamin', 'mysoreroad', 'Max', 20, 3),
(14, 'Nichols', 'dnagar', 'Christopher', 21, 3),
(15, 'Adam', 'devanahalli', 'Mills', 20, 2),
(16, 'Luke', 'shivajinagar', 'Nathan', 21, 2),
(17, 'Lewis', 'chikjala', 'Jake', 20, 2),
(18, 'Aaron', 'srirampura', 'Patel', 21, 2),
(19, 'Harry', 'ppnagar', 'Edward', 20, 2),
(20, 'Peter', 'kuvempuroad', 'Collins', 21, 2);

-- --------------------------------------------------------

--
-- Table structure for table `subjectinfo`
--

CREATE TABLE `subjectinfo` (
  `id` int(11) NOT NULL,
  `Name` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subjectinfo`
--

INSERT INTO `subjectinfo` (`id`, `Name`) VALUES
(1, 'English'),
(2, 'C'),
(3, 'Kannada'),
(4, 'java');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL,
  `user_name` varchar(45) DEFAULT NULL,
  `user_username` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`user_id`, `user_name`, `user_username`, `user_password`) VALUES
(1, '', '', 'pbkdf2:sha256:150000'),
(2, 'Sushruth S', 'sushruth.sushe@gmail', 'pbkdf2:sha256:150000'),
(3, '123', '123', 'pbkdf2:sha256:150000'),
(4, 'abcd', 'abcd', 'pbkdf2:sha256:150000'),
(5, '3456', '34545', 'pbkdf2:sha256:150000'),
(6, '1234567', '1234567', 'pbkdf2:sha256:150000'),
(7, 'asd', 'asd', 'asd'),
(8, 'ggg', 'ggg', 'ggg'),
(9, 'Prajwal', 'prajwal@gmail.com', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `branchinfo`
--
ALTER TABLE `branchinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `marksinfo`
--
ALTER TABLE `marksinfo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Sid` (`Sid`),
  ADD KEY `Subid` (`Subid`);

--
-- Indexes for table `seminfo`
--
ALTER TABLE `seminfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studentinfo`
--
ALTER TABLE `studentinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subjectinfo`
--
ALTER TABLE `subjectinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `branchinfo`
--
ALTER TABLE `branchinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `marksinfo`
--
ALTER TABLE `marksinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `seminfo`
--
ALTER TABLE `seminfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `studentinfo`
--
ALTER TABLE `studentinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `subjectinfo`
--
ALTER TABLE `subjectinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `user_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `marksinfo`
--
ALTER TABLE `marksinfo`
  ADD CONSTRAINT `marksinfo_ibfk_1` FOREIGN KEY (`Sid`) REFERENCES `studentinfo` (`id`),
  ADD CONSTRAINT `marksinfo_ibfk_2` FOREIGN KEY (`Subid`) REFERENCES `subjectinfo` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
