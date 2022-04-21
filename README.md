# Autoprestamo de libros
# Bibliotecas Universidad Nacional de Colombia
Con el objetivo de construir un campus inteligente dentro de la Universidad Nacional de Colombia-Sede Bogotá se busca suplir algunos de los servicios que son ofrecidos a la comunidad universitaria, dentro de los que se encuentra el autoprestamo de libros por parte de la Red de Bibliotecas dentro del campus universitario.

El proceso de autoprestamo de libros en las bibliotecas contempla un antes, durante y despues de la experiencia del usuario, como se muestra a continuación:
![image](https://user-images.githubusercontent.com/70990883/164366780-317ffe7e-db18-4e8a-b064-e36025364265.png)
Antes de realizar el prestamo, el usuario se acerca a la Biblioteca en busca de un libro y el respectivo punto de autoprestamo del piso, pero se encuentra con el problema de que no hay suficientes maquinas de autoprestamo dentro de la biblioteca; después se dispone a realizar el prestamo del libro por medio de las maquinas de autoprestamo existentes, donde se le permite identificarse y al mismo tiempo registrar el libro , encontrando que debe realizar diferentes procesos de autenticación como lo son su documento de identificación, usuario y clave institucional; como ultimo paso se retira el libro de la biblioteca para posteriormente devolverlo a la Biblioteca, donde se puede encontrar con problemas como una mala demagnetización del libro o la no disponibilidad de puntos de devolución.


## Procesamiento de la información
### Miconcontrolador/ Microprocesador

El microcontrolador será el encargado de recibir, procesar y manipular la información del proceso que se realiza con el autopréstamo. Conociendo el proceso descrito en la sección anterior, establecimos una lista de posibles herramientas a utilizar.  

|  | ESP32 | Onion Omega 2 |
| :---:         |     :---:      |          :---: |
| Procesador   |  32-bit Xtensa LX6 de doble núcleo 240 MHz    | CPU MIPS de 580 MHz   |
| Memoria RAM     | 520 KiB SRAM     |64 MB     |
| Almacenamiento    | git diff       | 16 MB      |
| Voltaje de funcionamiento     | 3.3 V      | 3.3 V     |
| WIFI     | 802.11 b/g/n      | 2.4 Ghz  b / g / n     |
| GPIOs     | 13       | 15     |

## Conexiones del sistema

## Interfaz Con el usuario - Comunicación con el sistema de información

## Protocolos de autentecación de Usuario.

## Protocolos de autenticación de Libro 

## Máquina desmagnetizadora

### Alimentación del sistema
