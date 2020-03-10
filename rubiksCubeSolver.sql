-- phpMyAdmin SQL Dump
-- version 4.7.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 10, 2020 at 03:30 PM
-- Server version: 5.7.20
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rubiksCubeSolver`
--

-- --------------------------------------------------------

--
-- Table structure for table `whiteCross`
--

CREATE TABLE `whiteCross` (
  `id` tinyint(2) NOT NULL,
  `position` varchar(12) NOT NULL,
  `blue` varchar(100) NOT NULL,
  `red` varchar(100) NOT NULL,
  `green` varchar(100) NOT NULL,
  `orange` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `whiteCross`
--

INSERT INTO `whiteCross` (`id`, `position`, `blue`, `red`, `green`, `orange`) VALUES
(23, '000000000001', '', 'F2 U\' R2', 'M2 U2 M2', 'F2 U L2'),
(24, '000000000002', 'F2 U\' R\' F R', 'F\' B\'', 'F2 U L\' B L', 'F L'),
(21, '000000000010', 'R2 U F2', '', 'R2 U\' B2', 'S2 U2 S2'),
(22, '000000000020', 'R F', 'R2 U\' B\' R B', 'R\' B\'', 'R2 U F\' L F'),
(19, '000000000100', 'L2 U\' F2', 'S2 U2 S2', 'L2 U B2', ''),
(20, '000000000200', 'L\' F\'', 'L2 U B\' R B', 'L B', 'L2 U\' F\' L F'),
(17, '000000001000', 'M2 U2 M2', 'B2 U R2', '', 'B2 U\' L2'),
(18, '000000002000', 'B2 U R\' F R', 'B R', 'B2 U\' L\' B L', 'B\' L\''),
(15, '000000010000', 'F', 'R U\' B\' R B', 'R2 B\' R2', 'D F D\''),
(16, '000000020000', 'F\' U\' R\' F R', 'R\'', 'D\' R\' D', 'F2 L F2'),
(13, '000000100000', 'F\'', 'D\' F\' D', 'L2 B L2', 'L\' U\' F\' L F'),
(14, '000000200000', 'F U\' R\' F R', 'F2 R\' F2', 'D L D\'', 'L'),
(11, '000001000000', 'R2 F R2', 'R\' U\' B\' R B', 'B\'', 'D\' B\' D'),
(12, '000002000000', 'D R D\'', 'R', 'B U\' L\' B L', 'B2 L\' B2'),
(9, '000010000000', 'L2 F\' L2', 'D B D\'', 'B', 'L U\' F\' L F'),
(10, '000020000000', 'D\' L\' D', 'B2 R B2', 'B\' U\' L\' B L', 'L\''),
(7, '000100000000', 'F2', 'U\' R2', 'U2 B2', 'U L2'),
(8, '000200000000', 'U\' R\' F R', 'U2 B\' R B', 'U L\' B L', 'F\' L F'),
(5, '001000000000', 'U F2', 'R2', 'U\' B2', 'U2 L2'),
(6, '002000000000', 'R\' F R', 'U\' B\' R B', 'U2 L\' B L', 'U F\' L F'),
(3, '010000000000', 'U\' F2', 'U2 R2', 'U B2', 'L2'),
(4, '020000000000', 'U2 R\' F R', 'U B\' R B', 'L\' B L', 'U\' F\' L F'),
(1, '100000000000', 'U2 F2', 'U R2', 'B2', 'U\' L2'),
(2, '200000000000', 'U R\' F R', 'B\' R B', 'U\' L\' B L', 'U2 F\' L F');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `whiteCross`
--
ALTER TABLE `whiteCross`
  ADD PRIMARY KEY (`position`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
