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
-- Estrutura para tabela `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$XSrnzdlZhwKY78yiUiJx4C$wRMY1Fo8V5F5365mHCh53vfXfeKw7PfL1jxi5cM7y/8=', '2024-07-14 23:59:48.515855', 0, 'claudio', '', '', 'cl4ud1or31s@gmail.com', 0, 1, '2024-07-14 22:14:24.686969'),
(5, 'pbkdf2_sha256$720000$PHQWCpFZ6tgcJD7crjbVxx$+oGx5xoK797gEiGl/TtjOC2yKR/POIHMkaleTP4km1U=', '2024-07-15 00:01:06.898843', 0, 'admin', '', '', 'admin@admin.com', 0, 1, '2024-07-14 23:38:45.223047'),
(6, 'pbkdf2_sha256$720000$PgBFZgmF44zvlC5jvt6dLT$fdOcvQ1xALVmJH7hxUVK+Z5DuNcveFa8LfH4NgZJcF4=', '2024-07-15 00:00:35.921195', 0, 'elias', '', '', 'elias@gmail.com', 0, 1, '2024-07-15 00:00:27.108590');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
