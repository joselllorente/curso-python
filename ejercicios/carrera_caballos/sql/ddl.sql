CREATE TABLE `curso_python_carrera`.`grandes_premios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(30) NOT NULL,
  `distancia` INT NULL,
  `num_carreras` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `curso_python_carrera`.`apostantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(30) NOT NULL,
  `saldo` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `curso_python_carrera`.`caballos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(30) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `velocidad` INT NOT NULL,
  `experiencia` INT NOT NULL,
  `valor_apuesta` INT NOT NULL,
  `fk_gran_premio` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_idx` (`fk_gran_premio` ASC) VISIBLE,
  CONSTRAINT `gran_premio_fk`
    FOREIGN KEY (`fk_gran_premio`)
    REFERENCES `curso_python_carrera`.`grandes_premios` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);