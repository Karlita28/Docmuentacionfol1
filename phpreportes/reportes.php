<?php
require('pdf.php');
include 'Conexion.php';

class PDF extends PDF {
    function Header() {
        $this->SetFont('Arial','B',14);
        $this->Cell(0,10,'Reporte de Facturas',0,1,'C');
        $this->Ln(5);
    }

    function TableHeader() {
        $this->SetFont('Arial','B',12);
        $this->SetFillColor(0,102,204);
        $this->SetTextColor(255);
        $this->Cell(10,10,'ID',1,0,'C',true);
        $this->Cell(40,10,'DESCRIPCION',1,0,'C',true);
        $this->Cell(30,10,'CATEGORIA',1,0,'C',true);
        $this->Cell(20,10,'CANT.',1,0,'C',true);
        $this->Cell(25,10,'PRECIO',1,0,'C',true);
        $this->Cell(20,10,'ITBIS',1,0,'C',true);
        $this->Cell(20,10,'DESC.',1,0,'C',true);
        $this->Cell(25,10,'TOTAL',1,1,'C',true);
    }

    function TableBody($conn) {
        $this->SetFont('Arial','',11);
        $this->SetFillColor(230, 240, 255);
        $this->SetTextColor(0);
        $fill = false;

        $consulta = "SELECT * FROM factura";
        $resultado = $conn->query($consulta);

        while($row = $resultado->fetch_assoc()) {
            $this->Cell(10,10,$row['id'],1,0,'C',$fill);
            $this->Cell(40,10,$row['descripcion'],1,0,'L',$fill);
            $this->Cell(30,10,$row['categoria'],1,0,'L',$fill);
            $this->Cell(20,10,$row['cantidad'],1,0,'C',$fill);
            $this->Cell(25,10,number_format($row['precio_unitario'],2),1,0,'C',$fill);
            $this->Cell(20,10,number_format($row['itebis'],2),1,0,'C',$fill);
            $this->Cell(20,10,number_format($row['descuento'],2),1,0,'C',$fill);
            $this->Cell(25,10,number_format($row['total'],2),1,1,'C',$fill);
            $fill = !$fill;
        }
    }
}

$pdf = new PDF();
$pdf->AddPage();
$pdf->TableHeader();
$pdf->TableBody($conn);
$pdf->Output();
?>
