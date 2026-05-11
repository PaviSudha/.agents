# Mind Palace Wiki Examples

## Scenario: Researching a New Topic
1. Create a workspace:
   `python scripts/wiki_manager.py build-room "QuantumPhysics"`
2. Add a core concept with a template:
   `python scripts/wiki_manager.py add "Entanglement" --room "QuantumPhysics" --template "Science"`
3. Pull external research:
   `python scripts/wiki_manager.py ingest-url "https://en.wikipedia.org/wiki/Quantum_entanglement" --title "WikiData" --room "QuantumPhysics"`
4. Connect to existing knowledge:
   `python scripts/wiki_manager.py link "Entanglement" "Relativity"`
5. Verify the network:
   `python scripts/wiki_manager.py analyze --bridges`

## Scenario: Reorganizing the Palace
1. Rename a vague title:
   `python scripts/wiki_manager.py rename "Stuff" "Thermodynamics"`
2. Let Python find new links:
   `python scripts/wiki_manager.py auto-link`
3. Export the room for a report:
   `python scripts/wiki_manager.py export --room "Physics"`

## Scenario: Quick Search
1. Find every mention of "Entropy":
   `python scripts/wiki_manager.py search "Entropy"`
2. Check recent work:
   `python scripts/wiki_manager.py recent`
