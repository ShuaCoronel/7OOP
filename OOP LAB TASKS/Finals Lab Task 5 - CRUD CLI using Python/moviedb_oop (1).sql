-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2025 at 01:29 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moviedb_oop`
--

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `movie_id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `main_actor` varchar(50) NOT NULL,
  `director` varchar(50) NOT NULL,
  `genre` varchar(25) NOT NULL,
  `gross_sales` float NOT NULL,
  `ratings` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`movie_id`, `title`, `main_actor`, `director`, `genre`, `gross_sales`, `ratings`) VALUES
(1, 'Spider-Man: No Money', 'Peter Parker', 'Sam Raimi', 'Sci-Fi', 170000000, 'R16'),
(2, 'Iron Man', 'Robert Downey Jr.', 'Jon Favreau', 'Sci Fi', 585000000, 'PG'),
(4, 'Black Widow', 'Scarlett Johansson', 'Cate Shortland', 'Action/Sci-Fi', 449000000, 'PG13'),
(5, 'Thor: Pointbreak', 'Chris Hemsworth', 'Kennath Branagh', 'Action/Com/Sci-Fi', 459000000, 'PG13'),
(6, 'Star Lord: Quill', 'Chris Pratt', 'James Gunn', 'Action/Com/Sci-fi', 773000000, 'PG13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`movie_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
