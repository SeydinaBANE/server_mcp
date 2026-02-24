# 🤖 Server MCP-Agent LangGraph avec outils Math & Météo

Un projet d'agent IA basé sur **LangChain**, **LangGraph** et le protocole **MCP (Model Context Protocol)**, connectant un modèle LLM Groq à des outils externes via des serveurs MCP.

---

## 📁 Structure du projet

```
Server_mcp/
├── src/
│   ├── client.py          # Agent principal (LangGraph + Groq)
│   ├── mathserver.py      # Serveur MCP — outils mathématiques (stdio)
│   └── weather.py         # Serveur MCP — outil météo (streamable_http)
├── .env                   # Clés API (non versionné)
├── .gitignore
├── .python-version        # Version Python du projet
├── .venv/                 # Environnement virtuel Python
├── pyproject.toml         # Configuration du projet
├── requitements.txt       # Dépendances Python
├── uv.lock                # Lockfile uv
└── README.md
```

---

## ⚙️ Prérequis

- Python 3.11+ (voir `.python-version`)
- [uv](https://docs.astral.sh/uv/) - gestionnaire de paquets (recommandé)
- Un compte [Groq](https://console.groq.com) pour obtenir une clé API

---

## 🚀 Installation

### Avec `uv` (recommandé)

```bash
cd Server_mcp
uv sync
```

### Avec `pip` classique

```bash
cd Server_mcp
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
pip install -r requitements.txt
```

### Configurer les variables d'environnement

Créer (ou compléter) le fichier `.env` à la racine :

```env
GROQ_API_KEY=votre_clé_api_groq_ici
```

---

## 🧩 Architecture

Ce projet utilise deux types de transport MCP :

| Fichier | Transport | Lancement |
|---|---|---|
| `src/mathserver.py` | `stdio` | Automatique via le client |
| `src/weather.py` | `streamable_http` | Manuel sur le port 8000 |

```
src/client.py
    ├── MultiServerMCPClient
    │       ├── math (stdio)    → src/mathserver.py
    │       └── weather (http)  → src/weather.py :8000
    ├── ChatGroq (openai/gpt-oss-120)
    └── create_agent (LangGraph)
```

---

## 🛠️ Les outils disponibles

### Serveur Math (`src/mathserver.py`)
| Outil | Description | Paramètres |
|---|---|---|
| `add` | Additionne deux nombres | `a: float, b: float` |
| `subtract` | Soustrait deux nombres | `a: float, b: float` |

### Serveur Météo (`src/weather.py`)
| Outil | Description | Paramètres |
|---|---|---|
| `get_weather` | Retourne la météo d'une ville | `location: str` |

---

## ▶️ Lancer le projet

### Étape 1 - Démarrer le serveur météo (Terminal 1)

```bash
source .venv/bin/activate
python src/weather.py
```

Le serveur démarre sur `http://127.0.0.1:8000/mcp`

### Étape 2 -Lancer le client agent (Terminal 2)

```bash
source .venv/bin/activate
python src/client.py
```

### Résultat attendu

```
Les outils disponibles: ['add', 'subtract', 'get_weather']
La réponse à votre question: (4+5) = 9 et (54-50) = 4
```

-

## 🐛 Erreurs fréquentes

| Erreur | Cause | Solution |
|---|---|---|
| `Missing 'transport' key` | Clé `transport` absente dans la config | Ajouter `"transport": "stdio"` ou `"streamable_http"` |
| `SyntaxError: forgot a comma` | `print("texte" variable)` | Ajouter une virgule : `print("texte", variable)` |
| `object dict can't be used in await` | Utilisation de `.invoke()` au lieu de `.ainvoke()` | Remplacer par `await agent.ainvoke(...)` |
| `streamable-http` non reconnu | Tiret au lieu d'underscore | Utiliser `streamable_http` |

---

## 📚 Technologies utilisées

- [LangChain](https://python.langchain.com/) — Framework LLM
- [LangGraph](https://langchain-ai.github.io/langchain/) — Agent ReAct
- [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) — Intégration MCP
- [FastMCP](https://github.com/jlowin/fastmcp) — Création de serveurs MCP
- [Groq](https://groq.com/) — Inférence LLM ultra-rapide
- [uv](https://docs.astral.sh/uv/) — Gestionnaire de paquets moderne
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Gestion des variables d'environnement

---

## 👤 Auteur

**Bane Seydina Mouhamet** 