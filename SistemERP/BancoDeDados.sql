-- Estrutura da tabela cliente
DROP TABLE IF EXISTS `cliente`;

CREATE TABLE `cliente` (
  `idCliente` int NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `Celular` varchar(50) DEFAULT NULL,
  `Cidade` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Inserir dados exemplo
--INSERT INTO `cliente` VALUES (1, 'Nome Exemplo', '(XX)XXXX-XXXX', 'Cidade Exemplo');
