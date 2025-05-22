<?php
$host = "localhost";
$usuario = "root";
$contrasena = "1234";
$basedatos = "facturacionpruebas1";

$conn = new mysqli($host, $usuario, $contrasena, $basedatos);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
?>
