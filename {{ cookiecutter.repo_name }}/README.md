# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Guía de instalación :rocket:

Para instalar las dependencias necesarias para ejecutar el proyecto, consulta la guía de instalación en [install.md](install.md).

## Organización del proyecto :file_folder:

    ├── LICENSE
    ├── README.md          <- El README para desarrolladores usando este proyecto.
    ├── install.md         <- Instrucciones detalladas para configurar este proyecto.
    ├── data
    │   ├── processed      <- Los conjuntos de datos procesados para los modelos.
    │   └── raw            <- Los archivos originales que no se deben modificar.
    │
    ├── models             <- Modelos entrenados y serializados.
    │
    ├── notebooks          <- Jupyter notebooks. La convención de nombres es un número (para ordenar),
	│                         las iniciales del creador y una descripción corta separada por `-`, por ejemplo
	│                         `1.0-aigg-exploracion-inicial-datos`.
    │
    ├── references         <- Diccionarios de datos, manuales y otros materiales explicativos.
    │
    ├── reports            <- Análisis generados como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos y figuras generadas para informes.
    │
    ├── environment.yml    <- El archivo de requerimientos para reproducir el entorno.
    │
	├── .here              <- El archivo .here se usa para detener la búsqueda si ninguno 
	│                         de los otros criterios se aplica al buscar la raíz del proyecto.
	│
	├── setup.py           <- Configuración de empaquetado para poder acceder a los módulos del proyecto.
	│
    └── {{ cookiecutter.project_module_name }}               <- Código fuente usado en este proyecto.
        ├── __init__.py    <- Hace a '{{ cookiecutter.project_module_name }}' un paquete de Python.
        │
        ├── data           <- Scripts para descargar o generar datos.
        │   └── make_dataset.py
        │
		├── datatypes      <- Definiciones de tipos de datos personalizados.
        │
        ├── features       <- Scripts para convertir los datos originales en características para los modelos.
        │   └── build_features.py
        │
        ├── models         <- Scripts para entrenar modelos para hacer predicciones.
        │   │
		│   │   Ejemplos de scripts de entrenamiento y predicción:
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts para tareas comunes.
        │   └── paths.py   <- Funciones auxiliares para referenciar archivos relativos en todo el proyecto.
        │
        └── visualization  <- Scripts para crear visualizaciones exploratorias y orientadas a resultados.
            └── visualize.py

## Notas adicionales :memo:
Este proyecto fue creado para utilizarse con Conda + VSCode, por lo que se recomienda encarecidamente seguir la guía de instalación para configurar el entorno de trabajo del proyecto y utilizar VSCode como el editor principal.