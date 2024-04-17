# {{ cookiecutter.project_name }} / guía de instalación

## Prerrequisitos

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Crear el entorno conda

```bash
conda env create -f environment.yml
conda activate {{ cookiecutter.conda_env_name }}
```

Los paquetes necesarios para ejecutar el proyecto están ahora instalados dentro del entorno conda `{{ cookiecutter.conda_env_name }}`.

## Instalación del proyecto como paquete de Python

Para poder acceder a módulos desde cualquier parte del proyecto (como las `notebooks`), es necesario instalarlo como un paquete de Python. Para ello, ejecuta el siguiente comando en el entorno anteriormente creado sobre la raíz del proyecto (donde se encuentra el archivo `setup.py`):

```bash
pip install --no-build-isolation --no-deps -e .
```

De esta forma, puedes acceder a los módulos definidos en `{{ cookiecutter.project_module_name }}` desde cualquier parte del proyecto.