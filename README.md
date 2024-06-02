<div align="center">
<img src="logo.png" height="90px" width="auto" position="center" /> 
<h2>
    <em>Proyecto Django</em>Formulario minimalista maquetado para Web y Movil
</h2>
<p>

</p>

</div>

<div align="center">
    <a href="#🚀-empezar">
        Empezar
    </a>
    <span>&nbsp;✦&nbsp;</span>
    <a href="#🧞-comandos">
        Comandos
    </a>
    <span>&nbsp;✦&nbsp;</span>
    <a href="#🔑-licencia">
        Licencia
    </a>
    <span>&nbsp;✦&nbsp;</span>
    <a href="https://pablotorres.dev">
        Personal
    </a>
   
</div>

<p></p>

<div align="center">

![Astro Badge](https://img.shields.io/badge/Astro-BC52EE?logo=astro&logoColor=fff&style=flat)
![GitHub stars](https://img.shields.io/github/stars/midudev/minimalist-portfolio-json)
![GitHub issues](https://img.shields.io/github/issues/midudev/minimalist-portfolio-json)
![GitHub forks](https://img.shields.io/github/forks/midudev/minimalist-portfolio-json)
![GitHub PRs](https://img.shields.io/github/issues-pr/midudev/minimalist-portfolio-json)

</div>

<img src="portada.png"></img>

## 🛠️ Stack

- [**Django**](https://www.djangoproject.com/) - Django es un Framework web Python de alto nivel que fomenta un desarrollo rápido y un diseño limpio y pragmático.
- [**Typescript**](https://www.typescriptlang.org/) - JavaScript con sintaxis de tipado.



## 🚀 Empezar

### 1. Usa este [repo](https://github.com/pablotpy/formularioLaLinda-django) como _template_ de un proyecto de Sorteos Facil y Practico


- Yo uso [pip](https://pypi.org/project/pip/) como gestor de dependencias y empaquetador.

```bash
python --version
pip --version

#Clona del proyecto LINUX
mkdir formulario
cd formulrio
git clone https://github.com/pablotpy/formularioLaLinda-django.git . 
code .
=======
#Linux + Visual Studio Code - Crear Entorno Virtual:
python3 -m venv venv
source venv/bin/activate
=======
#Linux + Visual Studio Code - Instalar Librerias:
pip install -R  requirements.txt

# Inicializa de Migraciones a base de datos SQLITE3
python manage.py makemigrations
python manage.py migrate


```

### 2. Lanza el servidor de desarrollo:
```bash
#RUN SERVER
http://127.0.0.1:8000/


```

1. Abre [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/) en tu navegador para ver el resultado 🚀


## 🧞 Comandos

|     | Comando          | Acción                                        |
| :-- | :--------------- | :-------------------------------------------- |
| ⚙️  | `http://127.0.0.1:8000/` | Lanza un servidor de desarrollo local en  `http://127.0.0.1:8000/`.  |
| ⚙️  | `python manage.py migrate`| Comprueba posibles errores y hace un empaquetado de producción en.      |
| ⚙️  | `pip list`        | Lista de Librerias Instaladas en el entorno local `pip list` |



## 🔑 Licencia

[MIT](LICENSE.txt) - Creado por [**midudev**](https://midu.dev).
>>>>>>> c9dc726 (Mejora Readme)
