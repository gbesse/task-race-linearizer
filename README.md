# task-race-linearizer

## Français

Vérifier les courses annulation-fin par recherche de linéarisation.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m task_race_linearizer examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Recherche exhaustive mémoïsée d’un ordre séquentiel compatible avec les intervalles appel/retour et les états observés. Les transitions terminales sont immuables ; le témoin se rejoue étape par étape. Vérifie un contrat abstrait de courses plutôt qu’un simple journal trié par arrivée.

### Limites

18 opérations maximum ; chaque opération renvoie l’état après son effet. Contrat local explicite, pas certification MCP Tasks ni preuve de durabilité réseau.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Check cancellation-completion races through linearization search.

Synthetic data; no network access or secret required.

```sh
python -m task_race_linearizer examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Memoized exhaustive search for a sequential order compatible with call/return intervals and observed states. Terminal states are immutable; the witness replays step by step. Checks an abstract race contract rather than sorting a log by arrival.

### Limits

At most 18 operations; each operation returns post-effect state. Explicit local contract, not MCP Tasks certification or network durability proof.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comprobar carreras cancelación-finalización mediante búsqueda de linealización.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m task_race_linearizer examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Búsqueda exhaustiva memorizada de un orden secuencial compatible con intervalos llamada/respuesta y estados observados. Estados terminales inmutables; el testigo se reproduce paso a paso. Comprueba un contrato abstracto de carreras, no solo ordena registros.

### Límites

Máximo 18 operaciones; cada una devuelve estado posterior a su efecto. Contrato local explícito, no certificación MCP Tasks ni prueba de durabilidad de red.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://modelcontextprotocol.io/extensions/tasks/overview
