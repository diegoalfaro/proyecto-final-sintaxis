# Proyecto Final Sintaxis

## Integrantes

- Alfaro, Diego
- García, Alejo
- Neuwit, Lucas
- Nuñez, Juan Ignacio
- Otero, Agustín

## Configurar Debugger

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
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

### Correr intérprete con Docker

Para correr el intérprete con Docker se puede usar `docker-compose`:

```sh
# Este ejemplo correría el programa ejemplos/test.txt
docker-compose run interprete test.txt
```
