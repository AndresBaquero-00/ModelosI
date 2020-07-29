<h1>Repositorio para el curso de Modelos I</h1>

<h2>Integrantes</h2>
<ul>
  <li>Andrés Leonardo Baquero Hernandez</li>
  <li>Santiago Andrés Gordillo Piñeros</li>
</ul>

<h1>Patrones Creacionales</h1>

<ul>
  <li>
    Abstract Factory
    <p>Proporciona una interfaz para crear familias de objetos o que dependen entre sí, sin especificar sus clases concretas.</p>
    <img src="/Imagenes/AbstractFactory/abstractfactory.png" alt="Abstract Factory">
    <h4>Implementacion</h4>
    <ul>
      <li>Fabricas</li>
      <img src="/Imagenes/AbstractFactory/FabricaDiscos.png" alt="Fabrica Discos" width="450" height="300">
      <li>Productos</li>
      <img src="/Imagenes/AbstractFactory/Discos.png" alt="Discos" width="450" height="300">
    </ul>
  </li>
  <li>
    Builder
    <p>Separa la construcción de un objeto complejo de su representación, de forma que el mismo proceso de construcción pueda crear       diferentes representaciones.</p>
    <img src="/Imagenes/Builder/builder.png" alt="Builder">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Builder/EjemploBuilder.png" alt="Ejemplo Builder" width="450" height="300">
  </li>
  <li>
    Factory Method
    <p>Define una interfaz para crear un objeto, pero deja que sean las subclases quienes decidan qué clase instanciar. Permite que una clase delegue en sus subclases la creación de objetos.</p>
    <img src="/Imagenes/FactoryMethod/factorymethod.png" alt="Factory Method">
    <h4>Implementacion</h4>
    <img src="/Imagenes/FactoryMethod/EjemploFactoryMethod.jpg" alt="Ejemplo Factory Method" width="750" height="300">
  </li>
  <li>
    Protoype
    <p>Especifica los tipos de objetos a crear por medio de una instancia prototípica, y crear nuevos objetos copiando este prototipo.</p>
    <img src="/Imagenes/Prototype/prototype.png" alt="Prototype">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Prototype/EjemploPrototype.gif" alt="Ejemplo Prototype" width="750" height="300">
  </li>
  <li>
    Singleton
    <p>Garantiza que una clase sólo tenga una instancia, y proporciona un punto de acceso global a ella.</p>
    <img src="/Imagenes/Singleton/singleton.png" alt="Singleton">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Singleton/Ejemplo.jpg" alt="Ejemplo Singleton" width="400" height="450">
  </li>
</ul>



<h1>Patrones Estructurales</h1>
<p>Estudian como se relacionan los objetos en tiempo de ejecución. Sirven para diseñar las interconexiones entre los objetos.</p>

<ul>
  <li>
    Adapter
    <p>Convierte la interfaz de una clase en otra distinta que es la que esperan los clientes. Permiten que cooperen clases que de otra manera no podrían por tener interfaces incompatibles.</p>
    <img src="/Imagenes/Adapter/adapter.png" alt="Adapter">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Adapter/ejemploAdapter.png" alt="Ejemplo Adapter">
  </li>
  <li>
    Bridge
    <p>Desvincula una abstracción de su implementación, de manera que ambas puedan variar de forma independiente.</p>
    <img src="/Imagenes/Bridge/bridge.png" alt="Bridge">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Bridge/ejemploBridge.jpg" alt="Ejemplo Bridge" width="450" height="300">
  </li>
  <li>
    Composite
    <p>Combina objetos en estructuras de árbol para representar jerarquías de parte-todo. Permite que los clientes traten de manera uniforme a los objetos individuales y a los compuestos.</p>
    <img src="/Imagenes/Composite/composite.png" alt="Composite">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Composite/ejemploComposite.gif" alt="Ejemplo Composite" width="750" height="300">
  </li>
  <li>
    Decorator
    <p>Añade dinámicamente nuevas responsabilidades a un objeto, proporcionando una alternativa flexible a la herencia para extender la funcionalidad.</p>
    <img src="/Imagenes/Decorator/decorator.png" alt="Decorator">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Decorator/ejemploDecorator.jpg" alt="Ejemplo Decorator" width="750" height="300">
  </li>
  <li>
    Facade
    <p>Proporciona una interfaz unificada para un conjunto de interfaces de un subsistema. Define una interfaz de alto nivel que hace que el subsistema se más fácil de usar.</p>
    <img src="/Imagenes/Facade/facade.png" alt="Facade">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Facade/ejemploFacade.jpg" alt="Ejemplo Facade" width="400" height="450">
  </li>
  <li>
    Flyweight
    <p>Usa el compartimiento para permitir un gran número de objetos de grano fino de forma eficiente.</p>
    <img src="/Imagenes/Flyweight/flyweight.png" alt="Flyweight">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Flyweight/ejemploFlyweight.gif" alt="Ejemplo Flyweight" width="400" height="450">
  </li>
  <li>
    Proxy
    <p>Proporciona un sustituto o representante de otro objeto para controlar el acceso a éste.</p>
    <img src="/Imagenes/Proxy/proxy.png" alt="Proxy">
    <h4>Implementacion</h4>
    <img src="/Imagenes/Proxy/ejemploProxy.png" alt="Ejemplo Proxy" width="400" height="450">
  </li>
</ul>
