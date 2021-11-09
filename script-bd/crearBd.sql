CREATE TABLE Vehiculos(
    id INT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL,
    fechaEntrada DATE NOT NULL,
    fechaSalida DATE,
    pagado BOOLEAN
);