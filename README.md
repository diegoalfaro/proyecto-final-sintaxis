# Proyecto Final Sintaxis

## Integrantes

- Alfaro, Diego
- García, Alejo
- Neuwit, Lucas
- Nuñez, Juan Ignacio
- Otero, Agustín

## Configurar Debugger

Para configurar el Debugger para VS Code se debe agregar este archivo en `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Ejecutar programa",
      "type": "python",
      "request": "launch",
      "program": ".",
      "args": ["ejemplos/test.txt"],
      "console": "integratedTerminal"
    }
  ]
}
```

### Correr intérprete sin Docker

Para correr el intérprete con Docker se puede usar `python3` o `python`:

```sh
# Este ejemplo correría el programa ejemplos/test.txt
python3 . ejemplos/test.txt
```

### Correr intérprete con Docker

Para correr el intérprete con Docker se puede usar `docker-compose`:

```sh
# Este ejemplo correría el programa ejemplos/test.txt
docker-compose run interprete test.txt
```
