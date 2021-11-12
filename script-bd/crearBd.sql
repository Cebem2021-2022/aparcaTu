CREATE TABLE Vehiculos(
    id INT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL,
    fechaEntrada TIMESTAMP NOT NULL,
    fechaSalida TIMESTAMP,
    pagado BOOLEAN
);