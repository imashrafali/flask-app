-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 31, 2018 at 08:44 AM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `averageprogrammer`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `Name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `Name`, `email`, `phone`, `msg`, `date`) VALUES
(1, 'myfirstpost', 'myfirstpost@gmail.com', '1234567789', 'my first post', '2018-08-19 21:29:33'),
(2, 'Ashraf ali', 'ashrafali1995ali@gmail.com', '8892163967', 'my first test ', NULL),
(3, 'Ashraf ali', 'ashrafali1995ali@gmail.com', '8892163967', 'my first test ', '2018-08-19 22:05:18'),
(4, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'adklashfasldfalsdj', '2018-08-20 12:34:35'),
(5, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'adklashfasldfalsdj', '2018-08-20 12:38:24'),
(6, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'adklashfasldfalsdj', '2018-08-20 12:40:08'),
(7, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'adklashfasldfalsdj', '2018-08-20 12:44:14'),
(8, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'adklashfasldfalsdj', '2018-08-20 12:46:06'),
(9, 'Ashraf ali', 'ashrafali1995ali@gmail.com', '8892163967', 'hi this is test mail', '2018-08-20 12:53:31'),
(10, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'ashrafaliaf', '2018-08-20 13:01:24'),
(11, 'Ashraf ali', 'ashrafali1995ali@gmail.com', '8892163967', 'adhfdhodfhsd', '2018-08-20 13:04:41'),
(12, 'Ashraf ali', 'mashrafa581@gmail.com', '8892163967', 'ashrafaliaf', '2018-08-20 13:06:02'),
(13, 'mujeer', 'marela@gmail.com', '7204221447', 'hi bro nice website', '2018-08-23 14:31:05'),
(14, 'Ashraf ali', 'ashrafali1995ali@gmail.com', '8892163967', '', '2018-08-25 11:25:35');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `sub` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `sub`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'Python wiki', 'Beautiful is better than ugly', 'first-post', 'Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.', 'contact-bg.j', '2018-08-31 12:12:34'),
(2, 'The Python Tutorial', 'Python is an easy to learn, powerful programming language', 'second-post', ' Numbers\r\nThe interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses (()) can be used for grouping. For example:\r\n\r\n>>>\r\n>>> 2 + 2\r\n4\r\n>>> 50 - 5*6\r\n20\r\n>>> (50 - 5*6) / 4\r\n5.0\r\n>>> 8 / 5  # division always returns a floating point number\r\n1.6\r\nThe integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.\r\n\r\nDivision (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %:', '', '2018-08-22 13:29:20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
