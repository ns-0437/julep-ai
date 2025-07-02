# 🍽️ Julep AI - Weather-Based Foodie Tour

## 🧠 Project Overview

This project builds a weather-aware foodie tour experience using [Julep.ai](https://julep.ai) — a no-code AI workflow platform. The system:

1. Accepts a list of cities.
2. Checks each city's current weather to suggest indoor or outdoor dining.
3. Uses AI to identify 3 iconic local dishes per city.
4. Searches for top-rated restaurants that serve those dishes.
5. Crafts a delightful one-day foodie tour (breakfast, lunch, and dinner) as a narrative.

---

## 🛠️ Technologies Used

- **Julep.ai** – Visual AI workflow (weather APIs + LLMs + logic blocks)
- **Python** – For mock logic testing (`test_workflow.py`)
- **JSON** – To manage input data (`cities.json`)

---

## 📁 Folder Structure



julep ai/
├── data/
│ └── cities.json # List of cities
├── outputs/
│ └── paris_tour.txt, etc. # Generated foodie tour texts
├── scripts/
│ └── test_workflow.py # Mock version of the logic
├── README.md
├── .gitignore
└── requirements.txt




---

## 🔄 Julep Workflow (Visual)

The core logic is implemented in a visual workflow on the Julep platform. The steps:

1. **Input**: List of cities  
2. **Weather Check**: Julep weather block  
3. **Indoor/Outdoor Logic**: Decide based on weather  
4. **Dishes Block**: Use LLM to suggest iconic local dishes  
5. **Restaurant Block**: Use LLM to find restaurants per dish  
6. **Tour Generation**: Final LLM block to compose the narrative tour  

📎 **Workflow Link**:  
🔗 [Click here to view the Julep Workflow](https://julep.ai/workflow/share/your-workflow-link-here)  
_(Replace with your actual workflow share link from Julep)_

---

## 🧪 How to Run Locally (Python Mock)

For testing the logic outside of Julep (no API calls):

```bash
cd scripts
python test_workflow.py


__pycache__/
*.pyc
outputs/
.env

