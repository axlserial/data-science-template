import subprocess


def main():
    # Initialize a git repository
    print("Inicializando un repositorio git...")
    subprocess.run(["git", "init", "--initial-branch", "main"], check=True)

    print("Proyecto inicializado correctamente")
    return


if __name__ == "__main__":
    main()
