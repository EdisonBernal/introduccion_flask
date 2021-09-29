/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ db-encuesta /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE db-encuesta;

DROP TABLE IF EXISTS encuesta;
CREATE TABLE `encuesta` (
  `idenc` smallint(6) NOT NULL AUTO_INCREMENT,
  `idusu` smallint(6) NOT NULL,
  `titulo` varchar(250) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `imagen` varchar(250) NOT NULL,
  PRIMARY KEY (`idenc`),
  KEY `FK_encuesta_usuario` (`idusu`),
  CONSTRAINT `FK_encuesta_usuario` FOREIGN KEY (`idusu`) REFERENCES `usuario` (`idusu`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS opcion_pregunta;
CREATE TABLE `opcion_pregunta` (
  `idopcpreg` smallint(6) NOT NULL AUTO_INCREMENT,
  `opcpregunta` varchar(100) NOT NULL,
  PRIMARY KEY (`idopcpreg`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS pregunta;
CREATE TABLE `pregunta` (
  `idpreg` smallint(6) NOT NULL AUTO_INCREMENT,
  `idsec` smallint(6) NOT NULL,
  `idtpreg` smallint(6) NOT NULL,
  `idopcpreg` smallint(6) NOT NULL,
  `pregunta` varchar(250) NOT NULL,
  PRIMARY KEY (`idpreg`),
  KEY `FK_pregunta_seccion` (`idsec`),
  KEY `FK_pregunta_tipo_pregunta` (`idtpreg`),
  KEY `FK_pregunta_opcion_pregunta` (`idopcpreg`),
  CONSTRAINT `FK_pregunta_opcion_pregunta` FOREIGN KEY (`idopcpreg`) REFERENCES `opcion_pregunta` (`idopcpreg`),
  CONSTRAINT `FK_pregunta_seccion` FOREIGN KEY (`idsec`) REFERENCES `seccion` (`idsec`),
  CONSTRAINT `FK_pregunta_tipo_pregunta` FOREIGN KEY (`idtpreg`) REFERENCES `tipo_pregunta` (`idtpreg`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS respuesta;
CREATE TABLE `respuesta` (
  `idres` smallint(6) NOT NULL AUTO_INCREMENT,
  `idpreg` smallint(6) NOT NULL,
  `idresopc` smallint(6) NOT NULL,
  `texto` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`idres`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS respuesta_opcion;
CREATE TABLE `respuesta_opcion` (
  `idresopc` smallint(6) NOT NULL AUTO_INCREMENT,
  `idresp` smallint(6) NOT NULL,
  `idopcpreg` smallint(6) NOT NULL,
  PRIMARY KEY (`idresopc`),
  KEY `FK_respuesta_opcion_respuesta` (`idresp`),
  KEY `FK_respuesta_opcion_opcion_pregunta` (`idopcpreg`),
  CONSTRAINT `FK_respuesta_opcion_opcion_pregunta` FOREIGN KEY (`idopcpreg`) REFERENCES `opcion_pregunta` (`idopcpreg`),
  CONSTRAINT `FK_respuesta_opcion_respuesta` FOREIGN KEY (`idresp`) REFERENCES `respuesta` (`idres`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS seccion;
CREATE TABLE `seccion` (
  `idsec` smallint(6) NOT NULL AUTO_INCREMENT,
  `idenc` smallint(6) NOT NULL,
  `seccion` varchar(200) NOT NULL,
  PRIMARY KEY (`idsec`),
  KEY `FK_seccion_encuesta` (`idenc`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS tipo_pregunta;
CREATE TABLE `tipo_pregunta` (
  `idtpreg` smallint(6) NOT NULL AUTO_INCREMENT,
  `tipopregunta` varchar(50) NOT NULL,
  PRIMARY KEY (`idtpreg`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS usuario;
CREATE TABLE `usuario` (
  `idusu` smallint(6) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `contrasena` varchar(250) NOT NULL,
  PRIMARY KEY (`idusu`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;