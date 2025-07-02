# 🍽️ Julep AI - Weather-Based Foodie Tour

## Project Overview
This project creates a weather-aware foodie tour for cities using Julep.ai. It:
1. Checks current weather to decide on indoor/outdoor dining.
2. Suggests 3 iconic dishes per city.
3. Finds top restaurants for each dish.
4. Crafts a full-day breakfast-lunch-dinner plan.

## Technologies
- Julep.ai (Visual AI Workflow)
- Python (for mock testing)
- JSON (city input)

## Folder Structure
julep ai/
├── data/
│ └── cities.json
├── outputs/
│ └── paris_tour.txt, etc.
├── scripts/
│ └── test_workflow.py
├── README.md
├── .gitignore
└── requirements.txt


## Julep Workflow (Visual)
Workflow includes:
- City input
- Weather check
- Dish suggestion (LLM)
- Restaurant search (LLM)
- Final foodie tour (LLM)

### Link to my Julep workflow: *(add your Julep share URL here)*

## How to Run Locally
```bash
cd scripts
python test_workflow.py


---

### ⚙️ Step 6: .gitignore Setup

Open `.gitignore` and paste:

```gitignore
__pycache__/
*.pyc
outputs/
.env
