#!/usr/bin/perl

#habilitamos el script a cgi
use CGI;

my $cgi = new CGI;

#obtenemos todos los valores del formulario
my $nombre = $cgi->param('nombre');
my $apellido = $cgi->param('apellido');
my $email = $cgi->param('email');
my $edad = $cgi->param('edad');
my $ciclo = $cgi->param('ciclo');
my $otros = $cgi->param('otros')

#revisamos que los campos no esten vacíos; si uno o varios lo están, devolvemos un aviso diciendo que el formulario no es correcto
if ($nombre eq "" | $apellido eq "" |$email eq "" |$otros eq "" ){
  print $cgi->header("text/html");
  print 'No has cumplimentado adecuadamente el formulario.'
  return;
}
#si el formulario es correcto, devolvemos todos los valores introducidos en el formulario
else {
  print $cgi->header("text/html");
  print 'Los datos introducidos son los siguientes: <br>';
  print 'Nombre: ' . $nombre ' <br>';
  print 'Apellidos: ' . $apellido ' <br>';
  print 'Email: ' . $email ' <br>';
  print 'Edad: ' . $email ' <br>';
  print 'Ciclo: ' . $edad ' <br>';
  print 'Estudios anteriores: ' . $ciclo ' <br>';
}
