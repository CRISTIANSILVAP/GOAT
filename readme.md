
# Título del Proyecto

libreria complejos 

## Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto y ejecutarlo en tu máquina local para fines de desarrollo y prueba. Consulta la sección de despliegue para obtener notas sobre cómo desplegar el proyecto en un sistema en producción.

### Requisitos previos
Unicamente se necesita python y git hub

### Instalación
Para acceder a las pruebas se debe tener ambos archivos en una misma carpeta para poder importar
la libreria con las funciones.

## Ejecutando las pruebas

simplemente al tener acceso al archivo se ejecuta en cualquier editor de codigo y ya funciona.

### Desglose en pruebas de extremo a extremo

Estan las 2 pruebas de cada funcion que se implemento y se escogieron;la primera por que la vi en clase, la 
segunda aleatoriamente.

  print("suma #1",suma((-2,1),(1,2)))

### Y pruebas de estilo de código

Las pruebas prueban la veracidad de los valores que nos da la implementacion de cada funcion, esto al hacer
alguna aproximacion o comprobar de que los valores sean cercanos o parecidos 

```
        suma = lc.suma((-2, 1), (1, 2))
        self.assertAlmostEqual(suma[0], -1)
        self.assertAlmostEqual(suma[1], 3)

```

## Despliegue

Agrega notas adicionales sobre cómo desplegar esto en un sistema en producción.

## Construido con
    *visual Studio Code 

## Contribuyendo

Por favor lee [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) para obtener detalles sobre nuestro código de conducta y el proceso para enviarnos pull requests.

## Versionado

Usamos [SemVer](http://semver.org/) para el versionado. Para ver las versiones disponibles, consulta los [tags en este repositorio](https://github.com/your/project/tags).

## Autores
cristian silva 

## Licencia

Este proyecto está bajo la licencia MIT - consulta el archivo [LICENSE.md](LICENSE.md) para más detalles.

## Agradecimientos

* Agradecimiento a cualquiera cuyo código fue utilizado.
* A los autores de cada video del uso de git y a mis compañeros.