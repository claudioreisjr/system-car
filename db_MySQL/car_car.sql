-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 15/07/2024 às 02:10
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `veiculos`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `car_car`
--

CREATE TABLE `car_car` (
  `id` bigint(20) NOT NULL,
  `owner_name` varchar(255) NOT NULL,
  `whatsapp` varchar(20) NOT NULL,
  `car_name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `km` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `license_plate` varchar(7) NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` varchar(7) NOT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `car_car`
--

INSERT INTO `car_car` (`id`, `owner_name`, `whatsapp`, `car_name`, `brand`, `km`, `price`, `license_plate`, `location`, `status`, `image`) VALUES
(9, 'Jorge', '351231231212', 'CRF', 'HONDA', 5000, 9920.00, 'HKS12', 'Baependi, MG', 'ativo', 'cars/moto2.jpg'),
(12, 'Elias', '3512312312', 'Caminhão', 'Mercedes', 120000, 120000.00, 'KSL1212', 'Nepomuceno, MG', 'ativo', 'cars/caminhao1.jpg'),
(14, 'José do Egito', '35997650818', 'Ferrari Vermelha', 'Ferrari', 1000, 1000000.00, 'BAW1212', 'Lavras_MG', 'ativo', 'cars/ferrari.jpg'),
(18, 'João Silva', '35931414343', 'Mustang GT', 'Mustang', 4, 1000000.00, '123KJS', 'Lavras, MG', 'ativo', 'cars/mustang_amarelo_JBLM9ht.jpg'),
(21, 'Pedro', '351332131', 'Argo', 'Fiat', 33, 55000.00, 'JKS123', 'São Paulo, SP', 'ativo', 'cars/fiatargo.jpg'),
(22, 'Hugo', '3212312312', 'Pulse', 'Fiat', 22000, 72000.00, 'KJS123', 'Perdões, MG', 'vendido', 'cars/fiatpulse.jpg'),
(23, 'Aldo', '3512312312', 'Toro Ranch', 'Fiat', 22000, 110000.00, 'JSK123', 'Lavras, MG', 'vendido', 'cars/fiattoro.JPG'),
(24, 'Gabriela', '0211231231', 'Uno', 'Fiat', 45000, 55000.00, 'KJS213', 'Lavras, MG', 'ativo', 'cars/fiatuno.jpg'),
(25, 'Janaina', '3512312312', 'Gol', 'Volkswagen', 33000, 62000.00, 'JSK123', 'Lavras, MG', 'ativo', 'cars/gol.JPG'),
(26, 'Roberto', '359812882', 'Jetta', 'Volksvagem', 45000, 109000.00, 'JSK1234', 'Betim, MG', 'ativo', 'cars/jettatsi.jpg'),
(27, 'Bernardo', '3512312312', 'Onix', 'Chevrolet', 19000, 67000.00, 'HGH1223', 'Lavras, MG', 'vendido', 'cars/onixbost.jpg');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `car_car`
--
ALTER TABLE `car_car`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `car_car`
--
ALTER TABLE `car_car`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
