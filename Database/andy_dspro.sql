-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 15, 2024 at 11:50 AM
-- Server version: 5.7.17-log
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `andy_dspro`
--

-- --------------------------------------------------------

--
-- Table structure for table `andy_menu`
--

CREATE TABLE `andy_menu` (
  `andy_id` varchar(20) COLLATE tis620_bin NOT NULL,
  `andy_name` varchar(50) COLLATE tis620_bin NOT NULL,
  `andy_price` int(20) NOT NULL,
  `andy_type` varchar(50) COLLATE tis620_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=tis620 COLLATE=tis620_bin;

--
-- Dumping data for table `andy_menu`
--

INSERT INTO `andy_menu` (`andy_id`, `andy_name`, `andy_price`, `andy_type`) VALUES
('FR001', 'Frappe  Cocoa', 75, 'ปั่น'),
('FR002', 'Frappe Mint Cocoa', 80, 'ปั่น'),
('FR003', 'Frappe Caramel Cocoa', 80, 'ปั่น'),
('FR004', 'Frappe Fresh milk', 70, 'ปั่น'),
('FR005', 'Frappe Strawberry smoothie', 85, 'ปั่น'),
('FR006', 'Frappe Mango smoothie', 85, 'ปั่น'),
('HCF001', 'Hot Espresso', 50, 'ร้อน'),
('HCF002', 'Hot Americano', 60, 'ร้อน'),
('HCF003', 'Hot Cappuccino', 60, 'ร้อน'),
('HCF004', 'Hot Cafe Latte', 60, 'ร้อน'),
('HCF005', 'Hot Mocha', 60, 'ร้อน'),
('HCF006', 'Hot Caramel Macchiato', 60, 'ร้อน'),
('HNCF001', 'Hot Thai tea', 60, 'ร้อน-ไม่มีกาแฟ'),
('HNCF002', 'Hot Premium Matcha', 75, 'ร้อน-ไม่มีกาแฟ'),
('HNCF003', 'Hot Cocoa', 60, 'ร้อน-ไม่มีกาแฟ'),
('HNCF004', 'Hot Fresh milk', 50, 'ร้อน-ไม่มีกาแฟ'),
('HNCF005', 'Hot Caramel milk', 60, 'ร้อน-ไม่มีกาแฟ'),
('HNCF006', 'Hot Vanilla milk', 60, 'ร้อน-ไม่มีกาแฟ'),
('ICF001', 'Ice Americano', 65, 'เย็น'),
('ICF002', 'Ice Thai Es yen', 70, 'เย็น'),
('ICF003', 'Ice Cappuccino', 70, 'เย็น'),
('ICF004', 'Ice Cafe Latte', 70, 'เย็น'),
('ICF005', 'Ice Mocha', 75, 'เย็น'),
('ICF006', 'Ice Caramel Macchiato', 75, 'เย็น'),
('INCF001', 'Ice Thai tea', 65, 'เย็น-ไม่มีกาแฟ'),
('INCF002', 'Ice Peach tea', 65, 'เย็น-ไม่มีกาแฟ'),
('INCF003', 'Ice Lime tea', 65, 'เย็น-ไม่มีกาแฟ'),
('INCF004', 'Ice Honey Lime Tea', 70, 'เย็น-ไม่มีกาแฟ'),
('INCF005', 'Ice Premium Matcha', 80, 'เย็น-ไม่มีกาแฟ'),
('INCF006', 'Ice Cocoa', 70, 'เย็น-ไม่มีกาแฟ'),
('INCF007', 'Ice Mint Cocoa', 75, 'เย็น-ไม่มีกาแฟ'),
('INCF008', 'Ice Fresh milk', 60, 'เย็น-ไม่มีกาแฟ'),
('INCF009', 'Ice Mint milk', 65, 'เย็น-ไม่มีกาแฟ'),
('INCF010', 'Ice Caramel milk', 65, 'เย็น-ไม่มีกาแฟ'),
('INCF011', 'Ice Vanilla milk', 65, 'เย็น-ไม่มีกาแฟ'),
('SCF001', 'Black orange', 75, 'พิเศษ'),
('SCF002', 'NAM-DOK-MAI', 80, 'พิเศษ-มะม่วง'),
('SCF003', 'Dirty', 85, 'พิเศษ'),
('SCF004', 'Wake it up!', 75, 'พิเศษ'),
('SCF005', 'SUNNY DOY', 85, 'พิเศษ-มะม่วง'),
('SD001', 'Strawberry soda', 60, 'โซดา'),
('SD002', 'Apple soda', 60, 'โซดา'),
('SD003', 'Mint soda', 60, 'โซดา'),
('SD004', 'Red lime soda', 60, 'โซดา'),
('SD005', 'Honey lime soda', 65, 'โซดา');

-- --------------------------------------------------------

--
-- Table structure for table `andy_sale`
--

CREATE TABLE `andy_sale` (
  `sale_id` varchar(50) COLLATE tis620_bin NOT NULL,
  `sale_price` float NOT NULL,
  `sale_count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=tis620 COLLATE=tis620_bin;

--
-- Dumping data for table `andy_sale`
--

INSERT INTO `andy_sale` (`sale_id`, `sale_price`, `sale_count`) VALUES
('FR001', 50, 2),
('FR002', 80, 4),
('FR003', 75, 2),
('FR004', 85, 1),
('FR005', 90, 1),
('FR006', 80, 2),
('HCF001', 50, 3),
('HCF002', 60, 5),
('HCF003', 60, 3),
('HNCF001', 60, 5),
('HNCF003', 60, 3),
('ICF001', 65, 4),
('INCF001', 65, 8);

-- --------------------------------------------------------

--
-- Table structure for table `andy_stock`
--

CREATE TABLE `andy_stock` (
  `stock_id` varchar(50) COLLATE tis620_bin NOT NULL,
  `stock_name` varchar(50) COLLATE tis620_bin NOT NULL,
  `stock_count` int(11) NOT NULL,
  `stock_price` float NOT NULL,
  `stock_buy` date NOT NULL,
  `stock_exp` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=tis620 COLLATE=tis620_bin;

--
-- Dumping data for table `andy_stock`
--

INSERT INTO `andy_stock` (`stock_id`, `stock_name`, `stock_count`, `stock_price`, `stock_buy`, `stock_exp`) VALUES
('COF-250124', 'เมล็ดกาแฟคั่ว (250 กรัม/ถุง)', 1, 595, '2023-10-25', '2023-01-24'),
('COF-71266', 'เมล็ดกาแฟคั่ว (250 กรัม/ถุง)', 1, 600, '2023-12-07', '2025-12-08'),
('MLK-251123', 'นมพาสเจอร์ไรส์ไม่มีแลคโตส (2ลิตร/แกลลอน)\n', 1, 96.75, '2023-11-25', '2023-11-23'),
('PMK-310324', 'นมข้าวโอ๊ต (1ลิตร/กล่อง)', 1, 115, '2023-11-23', '2023-03-24'),
('SCM-010824', 'นมข้นหวาน (388 กรัม/กระป๋อง)', 1, 35, '2023-10-25', '2025-10-25'),
('SCM-271124', 'นมข้นหวาน (388 กรัม/กระป๋อง)', 1, 38, '2023-09-23', '2023-11-24'),
('SYC-250624', 'ไซรัปคาราเมล (375 มิลลิลิตร/ขวด)\n\n', 1, 190, '2023-11-10', '2024-06-25'),
('SYH-250624', 'ไซรัปเฮเซลนัท (375 มิลลิลิตร/ขวด)', 1, 190, '2023-11-10', '2024-06-25'),
('SYV-250624', 'ไซรัปวนิลา (375 มิลลิลิตร/ขวด)\n\n', 1, 190, '2023-11-10', '2024-06-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `andy_menu`
--
ALTER TABLE `andy_menu`
  ADD PRIMARY KEY (`andy_id`);

--
-- Indexes for table `andy_sale`
--
ALTER TABLE `andy_sale`
  ADD PRIMARY KEY (`sale_id`);

--
-- Indexes for table `andy_stock`
--
ALTER TABLE `andy_stock`
  ADD PRIMARY KEY (`stock_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
