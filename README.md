# proyecto-CGI
Creado para la asignatura DAW, consiste en un script CGI enlazado a un html que nos valide si un formulario está cumplimentado

A la hora de probar el proyecto presenta el siguiente error que no se ha podido corregir:

Internal Server Error

The server encountered an internal error or misconfiguration and was unable to complete your request.

Se intuye que se debe a un fallo de configuración del servidor Apache en la máquina virtual que el alumno posee en casa.

 * No. Porblema en shebang, contenido proveniente de WIN, con lo que la primer línea del script acaba en /usr/bin/perl\r
 * Además hay errores de sintaxis, que no tienen que ver con el problema. Estos errores de sintaxis se pueden comprobar trabajando desde la línea de comando, es decir sin desplegar.    
 * El formulario ¿donde se pone? en carpeta cgi-bin o partir del DocumentRoot
 * Convenientemente deberíamos realizar algún tipo de persistencia. ¿No crees?
