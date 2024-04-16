# {{ cookiecutter.project_name }} guía de instalación

## Prerrequisitos

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Crear el entorno conda

```bash
conda env create -f environment.yml
conda activate {{ cookiecutter.conda_env_name }}
```

Los paquetes necesarios para ejecutar el proyecto están ahora instalados dentro del entorno conda `{{ cookiecutter.conda_env_name }}`.