-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 10, 2023 at 11:38 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop_product`
--

-- --------------------------------------------------------

--
-- Table structure for table `group_product`
--

CREATE TABLE `group_product` (
  `id` int(11) NOT NULL,
  `name_group` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `image_product`
--

CREATE TABLE `image_product` (
  `id` int(11) NOT NULL,
  `path_product_image` varchar(255) DEFAULT NULL COMMENT 'flag = 1',
  `url_product_image` varchar(255) DEFAULT NULL COMMENT 'flag = 2',
  `flag` int(3) DEFAULT NULL,
  `product_id` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `image_product`
--

INSERT INTO `image_product` (`id`, `path_product_image`, `url_product_image`, `flag`, `product_id`) VALUES
(91, 'images_230210_173614_1_1duIKx65-jXBB-505u-AfmY-ZdTiPayiaXIk.png', NULL, 1, 332),
(92, 'http://192.168.64.97:5000/ViewImage/images_230210_173614_2_CHcTrAHK-HhmP-y14o-aize-zx9pI49bweYp.png', NULL, 1, 332),
(93, 'images_230210_173617_1_ThLogY7B-gLO7-5kHv-fj5e-wMTAoE3rMkxk.png', NULL, 1, 333),
(94, 'http://192.168.64.97:5000/ViewImage/images_230210_173617_2_21LUMKNL-iovZ-No5z-4Dbv-QTlrEbnf1kjP.png', NULL, 1, 333),
(95, 'images_230210_173620_1_5XUvvth9-CtTa-IhiD-XbaF-4QlAjqRf07Mg.png', NULL, 1, 334),
(96, 'http://192.168.64.97:5000/ViewImage/images_230210_173620_2_2IVSuld7-aBD0-vM4G-qH9n-y89U3nv4JCCM.png', NULL, 1, 334),
(97, 'images_230210_173656_1_q5P9DMrP-3DJj-bJzd-8cfl-DhwkjVSSFIG3.png', NULL, 1, 335),
(98, 'http://192.168.64.97:5000/ViewImage/images_230210_173656_2_ukdE2k36-c05i-Sy8D-Wemf-tfD06aVMRimS.png', NULL, 1, 335),
(99, 'images_230210_173657_1_Um37aOK0-OnXm-UCQK-rgjE-kMZYQ74iwhuM.png', NULL, 1, 336),
(100, 'http://192.168.64.97:5000/ViewImage/images_230210_173658_2_3VecLQ4I-v5wR-wC7M-BxtA-IZKYEUUlWwjO.png', NULL, 1, 336),
(101, 'images_230210_173658_1_Oin0MePW-wkKZ-TQi3-eI0C-P55CKsiSsiGU.png', NULL, 1, 337),
(102, 'http://192.168.64.97:5000/ViewImage/images_230210_173658_2_uxR7keT8-kSHA-Hfgr-ff8s-1qWGJXD9igB2.png', NULL, 1, 337),
(103, 'images_230210_173659_1_5cUXP1fr-KoAR-Wd3g-OhqM-rOEixSfnglZK.png', NULL, 1, 338),
(104, 'http://192.168.64.97:5000/ViewImage/images_230210_173659_2_Lo5wdzTm-TLmZ-mO1x-UAJL-sgpuq3KtAKiW.png', NULL, 1, 338),
(105, 'images_230210_173659_1_kFXuoAua-T0BV-2AUF-8LOf-Bd1tbHl1rKCS.png', NULL, 1, 339),
(106, 'http://192.168.64.97:5000/ViewImage/images_230210_173659_2_XE7VV2oD-dO8S-U3JJ-BjqJ-WNtFw0ClFQSp.png', NULL, 1, 339),
(107, 'images_230210_173659_1_MNHNrZRk-fsrW-Iy0k-K02C-KXeaEvBtOQjx.png', NULL, 1, 340),
(108, 'http://192.168.64.97:5000/ViewImage/images_230210_173659_2_mWDetdqD-xSw2-k1ko-H956-EheEnRiEmYG6.png', NULL, 1, 340),
(109, 'images_230210_173700_1_oeznvwM2-7V7s-6HJh-1JPE-x7Z8ntCNxaxl.png', NULL, 1, 341),
(110, 'http://192.168.64.97:5000/ViewImage/images_230210_173700_2_a9MRV9Vb-afT7-t1Xd-Dm6a-7qtDfaCEJtEj.png', NULL, 1, 341);

-- --------------------------------------------------------

--
-- Table structure for table `image_user`
--

CREATE TABLE `image_user` (
  `id` int(11) NOT NULL,
  `url_product_image` varchar(255) DEFAULT NULL,
  `user_id` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name_product` varchar(255) DEFAULT NULL,
  `detail_product` varchar(255) DEFAULT NULL,
  `group_product` varchar(3) DEFAULT NULL,
  `price_product` decimal(10,0) DEFAULT NULL,
  `star_product` int(3) DEFAULT NULL,
  `discount_product` decimal(10,0) DEFAULT NULL,
  `qty_product` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name_product`, `detail_product`, `group_product`, `price_product`, `star_product`, `discount_product`, `qty_product`) VALUES
(269, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(270, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(271, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(272, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(273, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(274, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(275, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(276, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(277, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(278, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(279, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(280, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(281, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(282, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(283, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(284, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(285, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(286, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(287, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(288, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(289, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(290, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(291, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(292, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(293, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(294, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(295, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(296, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(297, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(298, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(299, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(300, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(301, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(302, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(303, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(304, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(305, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(306, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(307, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(308, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(309, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(310, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(311, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(312, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(313, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(314, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(315, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(316, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(317, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(318, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(319, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(320, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(321, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(322, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(323, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(324, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(325, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(326, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(327, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(328, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(329, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(330, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(331, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(332, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(333, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(334, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(335, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(336, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(337, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(338, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(339, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(340, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5'),
(341, 'หกฟหกฟหกฟ', 'หกฟหกฟหกฟ', '1', '254', 5, '0', '5');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name_user` varchar(255) DEFAULT NULL,
  `lname_user` varchar(255) DEFAULT NULL,
  `password_user` varchar(255) DEFAULT NULL,
  `email_user` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name_user`, `lname_user`, `password_user`, `email_user`) VALUES
(1, 'rang', 'ok', 'rang7754', 'rang7754@gmail.com'),
(5, 'yoyo', 'yoyo', 'yoyo', 'yoyo@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `group_product`
--
ALTER TABLE `group_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `image_product`
--
ALTER TABLE `image_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `image_user`
--
ALTER TABLE `image_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `group_product`
--
ALTER TABLE `group_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `image_product`
--
ALTER TABLE `image_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT for table `image_user`
--
ALTER TABLE `image_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=342;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
