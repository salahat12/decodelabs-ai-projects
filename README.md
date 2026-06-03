# 🤖 DecoBot — Rule-Based AI Chatbot
 
> **Project 1** of the DecodeLabs Industrial Training Program | Batch 2026  
> *Building the logic skeleton before the intelligence.*
 
---
 
## 📌 Overview
 
DecoBot is a rule-based AI chatbot built entirely with **Python** using control flow and dictionary-based intent matching. This project demonstrates the foundational architecture of intelligent systems — the deterministic logic layer that sits beneath modern AI models.
 
No machine learning. No external libraries. Pure programmatic decision-making.
 
---
 
## 🧠 The Concept: Why Rule-Based First?
 
Before building systems that *learn*, an AI engineer must master systems that *reason*.
 
| System | Type | Characteristic |
|--------|------|----------------|
| Rule-Based (this project) | Deterministic | Traceable, Safe, Zero hallucination risk |
| LLM / Neural Network | Probabilistic | Flexible, but unpredictable |
 
Rule-based systems act as **guardrails** for probabilistic AI — used in production by frameworks like NVIDIA NeMo and Llama Guard.
 
---
 
## ⚙️ Architecture: The IPO Model
 
```
INPUT (Raw Feed)  →  PROCESS (Logic Skeleton)  →  OUTPUT (Feedback Loop)
Sanitization &       Intent Matching &              Response
Normalization        Dictionary Lookup              Generation
```
 
---
 
## ✅ Features
 
- 🔁 **Infinite Loop** — Continuous `while True` conversation cycle
- 🧹 **Input Sanitization** — Handles case variations and whitespace (`.lower().strip()`)
- 📚 **Knowledge Base** — Dictionary with 12+ predefined intents
- ❓ **Fallback Response** — Graceful handling of unknown inputs
- 🚪 **Exit Strategy** — Clean `break` command on `exit` / `quit`
- ⚡ **O(1) Lookup** — Dictionary-based matching vs O(n) if-elif ladder
---
 
## 🚀 Getting Started
 
### Prerequisites
- Python 3.x
### Run the chatbot
 
```bash
python3 chatbot.py
```
 
### Example Session
 
```
==================================================
  DecoBot – Rule-Based AI Chatbot
  Type 'exit' or 'quit' to stop.
==================================================
 
You: hello
DecoBot: Hello! How can I assist you today?
 
You: what is ai
DecoBot: AI (Artificial Intelligence) is the simulation of human intelligence in machines.
 
You: tell me a joke
DecoBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛
 
You: exit
DecoBot: Goodbye! Keep building, keep learning. 🚀
```
 
---
 
## 📁 Project Structure
 
```
decodelabs-ai-projects/
│
├── chatbot.py      # Main chatbot — all logic lives here
└── README.md       # You are here
```
 
---
 
## 🔑 Key Concepts Demonstrated
 
- **Control Flow** — Loops, conditionals, break statements
- **Data Structures** — Dictionary as a knowledge base (Hash Map)
- **String Methods** — Normalization via `.lower()` and `.strip()`
- **Algorithmic Efficiency** — O(1) dictionary lookup vs O(n) if-elif chain
- **Software Design** — IPO model, separation of concerns, modular functions
---
 
## 🛣️ What's Next (Project 2 Preview)
 
This project uses **discrete mapping** (exact keyword match).  
Project 2 moves to **continuous mapping** — semantic/vector-based matching where the bot understands *meaning*, not just keywords.
 
```
Project 1:  "hello"  ──────────►  "Hello!"        (Exact Match)
Project 2:  "hey man" ─[vector]─►  "Hello!"        (Semantic Match)
```
 
---
 
## 🏷️ Built With
 
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![DecodeLabs](https://img.shields.io/badge/DecodeLabs-Batch_2026-green?style=flat-square)
![AI](https://img.shields.io/badge/AI-Rule--Based-orange?style=flat-square)
 
---
 
## 📄 License
 
This project is part of the **DecodeLabs Industrial Training Kit**.  
Built for educational and portfolio purposes.
 
---
 
*"An LLM without rules is a hallucination engine. Today, we build the skeleton that holds the intelligence."*  
**— DecodeLabs, Module 01**
 
