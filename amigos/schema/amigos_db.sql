-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema amigos_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `amigos_db` ;

-- -----------------------------------------------------
-- Schema amigos_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `amigos_db` DEFAULT CHARACTER SET utf8 ;
USE `amigos_db` ;

-- -----------------------------------------------------
-- Table `amigos_db`.`amigos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amigos_db`.`amigos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `ocupacion` VARCHAR(45) NULL,
  `creador_en` DATETIME NULL DEFAULT NOW(),
  `actualizado_en` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
