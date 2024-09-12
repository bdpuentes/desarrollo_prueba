Ejecución:
    Para ejecutar el proyecto se debe iniciar el archivo app.py

Requisitos Previos:

    Python 3.x
    Flask
    SQLite
    Requests (para realizar pruebas)
    
Descripción

    Este proyecto implementa una API RESTful en Python utilizando Flask para la consulta de precios de productos en una tienda electrónica. La API permite consultar los precios de productos específicos en base a una combinación de parámetros como el ID del producto, el ID de la marca y una fecha de aplicación. La base de datos utilizada es SQLite, que contiene una tabla llamada PRICES con los datos de ejemplo sobre los precios.

    El sistema está estructurado siguiendo una arquitectura de capas, donde cada capa cumple una función específica, promoviendo la separación de responsabilidades, modularidad y mantenibilidad.

    Funcionalidad Principal
    Endpoint /price: Permite realizar consultas de precios con base en tres parámetros:
    product_id: El ID del producto.
    brand_id: El ID de la marca.
    application_date: La fecha en la que se desea conocer el precio.
    El API procesa la solicitud y devuelve el precio más relevante en base a la prioridad de los datos en la base de datos.

    Ejemplo de uso:
    Una solicitud al endpoint /price con los siguientes parámetros:

    product_id: 35455
    brand_id: 1
    application_date: '2020-06-14 16:00:00'
    Retorna el precio más relevante disponible en la base de datos para el producto y la marca solicitada dentro del rango de fechas aplicable.

    Arquitectura del Proyecto

El proyecto sigue una arquitectura basada en capas, que incluye:

    Controlador (Controller): Responsable de manejar las solicitudes HTTP entrantes y pasar los parámetros a la capa de servicio.

    Servicio (Service): Contiene la lógica de negocio. Coordina la obtención de datos desde la base de datos a través del repositorio y aplica las reglas necesarias antes de devolver los datos al controlador.

    Repositorio (Repository): Interactúa directamente con la base de datos SQLite, ejecutando las consultas necesarias para recuperar los precios.

    Modelo (Model): Representa los datos de la tabla PRICES como objetos en el código.

Pruebas:
    El proyecto incluye un script de pruebas que automatiza la validación del endpoint /price mediante distintas consultas predefinidas. Las pruebas verifican que el API responda correctamente para diferentes combinaciones de parámetros.

Las pruebas incluidas son:

    Test 1: Consulta a las 10:00 del día 14 de junio de 2020 para el producto 35455 y la marca 1.
    Test 2: Consulta a las 16:00 del día 14 de junio de 2020 para el producto 35455 y la marca 1.
    Test 3: Consulta a las 21:00 del día 14 de junio de 2020 para el producto 35455 y la marca 1.
    Test 4: Consulta a las 10:00 del día 15 de junio de 2020 para el producto 35455 y la marca 1.
    Test 5: Consulta a las 21:00 del día 16 de junio de 2020 para el producto 35455 y la marca 1.

