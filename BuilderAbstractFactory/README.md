<h1>Processing</h1>

<p>Processing es un software especializado en la parte visual de un programa. Este entorno está basado en el lenguaje de programación Java.</p>

<p>Esta herramienta se encuentra en la página oficial de <a href = "https://processing.org/">Processing</a>. Además, se pueden encontrar algunos ejemplos que fueron hechos en esta herramienta, así como sus librerías, herramientas, etc.</p>

<p>La parte visual fue realizada en un sketch de processing, incorporando las demás clases java que se necesitan para la funcionalidad del programa.</p>

<p>Para el uso de este ejemplo en particular, desde la interfaz de processing, se abre el archivo que se encuentra en la carpeta Cliente, llamado <a href="https://github.com/AndresBaquero-00/ModelosI/blob/master/BuilderAbstractFactory/Cliente/Cliente.pde">cliente.pde</a>. Una vez abierto, se ejecuta con el comando <code>ctrl + r</code>, o haciendo click en la parte de ejecutar.</p>

<h3>Ejemplo interfaz del programa</h3>
<img src="/Imagenes/Processing.png">


### Diagrama
![alt text](https://raw.githubusercontent.com/AndresBaquero-00/ModelosI/master/Imagenes/ProgramaSprites.gif)

### Patrón Builder
El patrón lo podemos observar con la clase "Director", la clase "Constructor" y las clases "ConstructorVaquera" y "ConstructorNinja" como constructores concretos que obtienen el nombre, movimiento y los respectivos sprites

### Patrón Abstract Factory
El patrón lo podemos observar gracias a las fabricas abstractas, "FabricaNinja", "FábricaVaquera", "Fábrica" las cuales crean productos nombre, movimiento y sprites
