-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 06, 2025 at 04:55 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carsdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `id` int(11) NOT NULL,
  `model` varchar(20) NOT NULL,
  `year` year(4) NOT NULL,
  `color` varchar(20) NOT NULL,
  `engineCapacity` int(11) NOT NULL,
  `enginePower` int(11) NOT NULL,
  `engineType` varchar(30) NOT NULL,
  `transmission` varchar(10) NOT NULL,
  `price` decimal(7,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`id`, `model`, `year`, `color`, `engineCapacity`, `enginePower`, `engineType`, `transmission`, `price`) VALUES
(1, 'BMW X5', 2022, 'Black', 3000, 350, 'Petrol', 'A', '50000.00'),
(2, 'BMW 3 Series', 2021, 'White', 2000, 250, 'Diesel', 'M', '40000.00'),
(3, 'BMW M5', 2023, 'Blue', 4000, 600, 'Petrol', 'A', '80000.00'),
(4, 'BMW 5 Series', 2022, 'Silver', 2500, 300, 'Diesel', 'A', '45000.00'),
(5, 'BMW X3', 2023, 'Black', 2000, 240, 'Petrol', 'A', '38000.00'),
(6, 'BMW 7 Series', 2021, 'White', 3500, 400, 'Diesel', 'M', '65000.00'),
(7, 'BMW X1', 2022, 'Blue', 1800, 200, 'Petrol', 'A', '32000.00'),
(8, 'BMW 4 Series', 2023, 'Red', 3000, 350, 'Petrol', 'A', '48000.00'),
(9, 'BMW X6', 2022, 'Black', 4000, 500, 'Diesel', 'M', '75000.00'),
(10, 'BMW i3', 2021, 'Silver', 1500, 170, 'Electric', 'A', '35000.00'),
(11, 'BMW M4', 2023, 'Blue', 3000, 450, 'Petrol', 'M', '62000.00'),
(12, 'BMW X2', 2022, 'White', 2000, 230, 'Diesel', 'A', '36000.00'),
(13, 'BMW 8 Series', 2023, 'Black', 4400, 600, 'Petrol', 'A', '95000.00'),
(14, 'BMW X7', 2022, 'Silver', 4500, 550, 'Diesel', 'A', '85000.00'),
(15, 'BMW 2 Series', 2023, 'Black', 1800, 200, 'Petrol', 'M', '32000.00'),
(16, 'BMW M2', 2021, 'White', 3000, 365, 'Petrol', 'A', '54000.00'),
(17, 'BMW X4', 2022, 'Blue', 2000, 240, 'Diesel', 'A', '41000.00'),
(18, 'BMW 6 Series', 2023, 'Red', 3500, 420, 'Petrol', 'M', '69000.00'),
(19, 'BMW i8', 2022, 'Black', 1500, 170, 'Electric', 'A', '75000.00'),
(21, 'BMW X6', 2022, 'White', 3000, 400, 'Diesel', 'M', '68000.00'),
(22, 'BMW 4 Series', 2023, 'Black', 2500, 320, 'Petrol', 'A', '49000.00'),
(23, 'BMW X3', 2022, 'Blue', 2000, 240, 'Petrol', 'A', '39000.00'),
(24, 'BMW M4', 2021, 'Red', 3000, 450, 'Petrol', 'M', '62000.00'),
(25, 'BMW X2', 2022, 'White', 2000, 230, 'Diesel', 'A', '36000.00'),
(26, 'BMW 7 Series', 2023, 'Black', 4000, 500, 'Diesel', 'M', '77000.00'),
(27, 'BMW i3', 2022, 'Silver', 1500, 170, 'Electric', 'A', '35000.00'),
(28, 'BMW X5', 2021, 'Blue', 3000, 350, 'Petrol', 'A', '52000.00'),
(29, 'BMW 3 Series', 2023, 'Red', 2000, 250, 'Diesel', 'M', '41000.00'),
(30, 'BMW M5', 2022, 'White', 4000, 600, 'Petrol', 'A', '82000.00'),
(31, 'BMW X1', 2023, 'Black', 1800, 200, 'Petrol', 'A', '32000.00'),
(32, 'BMW 5 Series', 2021, 'Silver', 2500, 300, 'Diesel', 'A', '47000.00'),
(33, 'BMW X7', 2022, 'Black', 4500, 550, 'Diesel', 'A', '87000.00'),
(34, 'BMW 2 Series', 2023, 'Blue', 1800, 200, 'Petrol', 'M', '34000.00'),
(35, 'BMW M2', 2022, 'Red', 3000, 365, 'Petrol', 'A', '55000.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
