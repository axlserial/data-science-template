# Cookiecutter - data science :cookie:
By [Axel García](https://github.com/axlserial)

Plantilla de proyecto para ciencia de datos, adaptado a mis necesidades para mi trabajo de tesis.

## Requisitos :pushpin:
- Python 3.12+
- Conda >= 24.1.2
- Cookiecutter >= 2.6.0 - Puedes seguir el siguiente tutorial para crear un entorno conda con cookiecutter: [Creación de entorno conda con Cookiecutter](cookiecutter-installation.md)

## Uso :computer:
Para crear un nuevo proyecto, ejecuta el siguiente comando en el entorno donde hayas instalado cookiecutter:

```bash
cookiecutter https://github.com/axlserial/data-science-template.git
```
o
```bash
cookiecutter gh:axlserial/data-science-template
```

Se te pedirá que ingreses la información necesaria para el proyecto, esta información está definida en `cookiecutter.json`. Después de ingresar la información, el proyecto será creado en el directorio actual.

---
Proyecto basado en [cookiecutter-conda-data-science](https://github.com/jvelezmagic/cookiecutter-conda-data-science).