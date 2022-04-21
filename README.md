# Autoprestamo de libros
# Bibliotecas Universidad Nacional de Colombia
Con el objetivo de construir un campus inteligente dentro de la Universidad Nacional de Colombia-Sede Bogotá se busca suplir algunos de los servicios que son ofrecidos a la comunidad universitaria, dentro de los que se encuentra el autoprestamo de libros por parte de la Red de Bibliotecas dentro del campus universitario.

El proceso de autoprestamo de libros en las bibliotecas contempla un antes, durante y despues de la experiencia del usuario, como se muestra a continuación:

![image](https://user-images.githubusercontent.com/70990883/164366780-317ffe7e-db18-4e8a-b064-e36025364265.png)

Antes de realizar el prestamo, el usuario se acerca a la Biblioteca en busca de un libro y el respectivo punto de autoprestamo del piso, pero se encuentra con el problema de que no hay suficientes maquinas de autoprestamo dentro de la biblioteca; después se dispone a realizar el prestamo del libro por medio de las maquinas de autoprestamo existentes, donde se le permite identificarse y al mismo tiempo registrar el libro , encontrando que debe realizar diferentes procesos de autenticación como lo son su documento de identificación, usuario y clave institucional; como ultimo paso se retira el libro de la biblioteca para posteriormente devolverlo a la Biblioteca, donde se puede encontrar con problemas como una mala demagnetización del libro o la no disponibilidad de puntos de devolución.

Partiendo del anterior analisis del viaje que debe hacer el usuario para poder realizar el autoprestamo de un libro, se define la problematica y un primer acercamiento a la solución:

![image](https://user-images.githubusercontent.com/70990883/164368591-d57464b9-8dc5-4ffd-865a-16199c7248fe.png)

Dentro de las problematicas principales destacan los problemas de integración entre los diferentes sistemas que tiene la universidad, no hay suficientes puntos de autoprestamo y la poca robustez del sistema existente. De igual modo, como solución se propone la conexión de nuevos puntos de autoprestamo optimizados y bioseguros, ademas de construir un sistema replicable y escalable más economico.


## Procesamiento de la información
### Miconcontrolador/ Microprocesador

El microcontrolador será el encargado de recibir, procesar y manipular la información del proceso que se realiza con el autopréstamo. Conociendo el proceso descrito en la sección anterior, establecimos una lista de posibles herramientas a utilizar.  

|  | ESP32 | Onion Omega 2 |
| :---:         |     :---:      |          :---: |
| Procesador   |  32-bit Xtensa LX6 de doble núcleo 240 MHz    | CPU MIPS de 580 MHz   |
| Memoria RAM     | 520 KiB SRAM     |64 MB     |
| Almacenamiento    | 	520 KB     | 16 MB      |
| Voltaje de funcionamiento     | 3.3 V      | 3.3 V     |
| WIFI     | 802.11 b/g/n      | 2.4 Ghz  b / g / n     |
| GPIOs     | 13       | 15     |

### Distribución de recursos de la ESP32

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/ESP32.jpg)

![Referencia](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.formacionprofesional.info%2Flos-modulos-esp32-y-lora-mas-vendidos%2F&psig=AOvVaw1jBdXjaZBCsjzVAEg_XZ78&ust=1650600058190000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCJj3u8SipPcCFQAAAAAdAAAAABAJ)

### Distribución de recursos de la ESP32

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/Omega2.png)

### Firmware

Conociendo los recursos de hardware que tenemos, ahora nos disponemos a elegir el firmware que podemos cargar. Para la ESP32 existe más documentación y soporte de la comunidad para Micropython y para C++. Analizaremos las diferencias entre ellos:

| MicroPython | C++ |
| ------------- | ------------- |
| Se instala una sola vez, y para acceder al código de y hacer modificaciones sólo se accesa a un sistema de archivos  | El proceso de compilado y enlace del programa se hace cada que se cambia el código, así como el proceso de flasheado  |
| Se pueden agregar tantas librerías o scripts como uno desee. El número sólo está limitado por la memoria flash del dispositivo | La compilación del programa puede demorar más entre más librerías se incluyan  |
|La ejecución del archivo principal main.py va después del archivo boot.py | El archivo de programa se compila a lenguaje máquina, lo que lo hace más eficiente, pero menos portable|

### Eficiencia y velocidad
- Los programas hechos en MicroPython se ejecutan desde bytecode compilado, que es un código de abstracción intermedia del lenguaje máquina.
- De ser necesario, para mejorar el rendimiento de un programa se puede agregar módulos de código en C o ensamblador.
- Se puede utilizar un Modo de Interprete Interactivo (Interpreter Interactive Mode) para probar el código escrito y verificar que funcione como deseamos; también conocido como REPL (read-eval-print-loop).

Información tomada de : ![image](https://blog.330ohms.com/2020/07/17/comparativa-arduino-v-s-micropython-para-el-esp32/)

## Interfaz Con el usuario - Comunicación con el sistema de información

### Lenguaje Machine to machine: protocolo MQTT

Como regla general la totalidad del sistema inteligente, ha adoptado el protocolo MQTT para la comunicación entre los diferentes dispositivos debido a que "El protocolo MQTT se ha convertido en uno de los principales pilares del IoT por su sencillez y ligereza. Ambos son condicionantes importantes dado que los dispositivos de IoT, a menudo, tienen limitaciones de potencia, consumo, y ancho de banda." [1]

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/MQTT.jpg)

## Protocolos de autentecación de Usuario

Para la autenticación del usuario, se usará como primer elemento el cané que cada estudiante tiene, seguido de un requerimeinto a la base de datos

### Tarjeta MIFARE

La tarjeta MIFARE es una tarjeta con chip de tecnología RFID 13.56Mhz 1K o 4K Entre las tarjetas RFID, la tarjeta MIFARE ® 13,56Mhz muestra el precio más económico. Pionera en la tecnología RFID en tarjetas de plástico, esta tarjeta MIFARE se usa ampliamente en sistemas de control de acceso, sistemas de transporte y fidelización.  La tarjeta MIFARE es la apuesta segura para administrar el acceso a  instalaciones.[2]

### lector de tarjeta 

El módulo RC522 es Lector-Grabador RFID 13.56MHz, posee comunicación SPI lo que permite trabajar fácilmente con la mayoría de microcontroladores. Utiliza un sistema de modulación y demodulación para todo tipo de dispositivos pasivos RFID de 13.56MHz. El dispositivo maneja el ISO14443-A y soporta el algoritmo de encriptación Quick CRYPTO1 y MIFARE. El rango de detección de tags RFID es de aprox. 5-7cm

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/modulo-rfid-c522.jpg)

-	Voltaje de Operación: 3.3V DC
-	Corriente de Operación: 13-26mA/3.3V DC
-	Corriente de Standby: 10-13mA/3.3V DC
-	Corriente de Sleep: <80uA
-	Corriente pico: <30mA
-	Frecuencia de operación: 13.56 MHz
-	Transferencia de datos: Max. 10Mbit/s
-	Tipos de tarjetas compatibles: Mifare1 S50, S70 Mifare1, MIFARE Ultralight, Mifare Pro, Mifare DESFire.
-	Dimensiones RFID-RC522: 40 mm x 60 mm
-	Dimensiones Tarjeta: 85 mm x 54 mm
-	Temperatura de funcionamiento: -20 a 80 grados centígrados
-	Temperatura de almacenamiento: -40 a 85 grados centígrados
-	Humedad relativa: 5% hasta 95 %
-	La tasa de transmisión por defecto: 9600bps, velocidad de transferencia máxima : 1228800bps

## Protocolos de autenticación de Libro 

Actualmente la biblioteca tiene estas etiquetas:

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/libro.jpg)

| Característica | Descripción  |
| ------------- | ------------- |
| Protocolo	|ISO/IEC15693 y 18000-3|
|Frecuencia	|Todo el mundo HF 13,56 Mhz|
|Chip	|ICODE®SLIX ICODE SLI(ICODE 2)|
|Memoria|	UID8ByteUID 64bit|
|Retención de datos|	10 años|
|Los ciclos de programación|	100.000 ciclos|
|Anti-colisión de la	Soporte de múltiples etiquetas de lectura|

Como es un protocolo más costo y el lector supera los costos para realizar un proprtipado con el mismo módulo 522, se usará una etiqueta diferente:

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/slb01_2.jpg)

| Característica | Descripción  |
| ------------- | ------------- |
|Distancia de Lectura| 100mm.|
Frecuencia| 13.56 MHz.|
Protocolo| ISO14443 e ISO15693|
Chipset| Ultralight,  Classic 1K, I.CODE SLI.|
Temperatura| -10ºC ∼ 50ºC.|
Dimensiones| 45mm x 25mm.|

## Pantalla

Este  módulo  consta de una pantalla LCD que nos permitirá desplegar imágenes, programar gráficos, textos, colores.

-	Voltaje de operación: 5 VDC
-	Controlador gráfico (driver): R61505 
-	Controlador de pantalla con buffer de video incluido
-	Interface LCD: Data (8 pines) Control (5 pines)
-	Interface micro SD: SPI (SS,DI,DO,SCK)
-	Nivel lógico de SPI: 3.3 - 5V
-	Tamaño de la pantalla (diagonal): 2.4" (61mm)
-	Resolución: 240x320 píxeles
-	Profundidad de color o bits por pixel: 16/18 bpp
-	Cantidad de colores: 262144 colores (18-bit: R6G6B6)
-	*Puede trabajar opcionalmente a RGB 16-bit: R5G6B5
-	Dimensiones pantalla: 49*38mm (área visible)
-	Dimensiones placa: 72*52mm
-	Socket para memoria externa micro SD
-	Pantalla táctil resistive
-	Fabricante: mcufriend


![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/pantalla.jpg)

### Pruebas Iniciales

![image](https://github.com/dfigueroa11/bibliotecas_autoprestamo_UNAL/blob/main/images/pantalla_2.jpeg)


## Máquina desmagnetizadora

### Referencias 

[1] https://www.luisllamas.es/que-es-mqtt-su-importancia-como-protocolo-iot/
[2] https://a3m.eu/es/tarjeta-mifare

