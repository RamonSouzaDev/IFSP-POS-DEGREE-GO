# EcoCompute API (IFSP Capivari Project) 🌍⚡

> **Sustainable Software Engineering** (Green Computing) API developed for the Pos-Graduação IFSP Capivari context.

[![EcoCompute CI](https://github.com/RamonSouzaDev/IFSP-POS-DEGREE-GO/actions/workflows/ifsp_ci.yml/badge.svg)](https://github.com/RamonSouzaDev/IFSP-POS-DEGREE-GO/actions)
![Python](https://img.shields.io/badge/Python-3.11-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)

## 📌 About the Project

This project demonstrates how **Software Engineering** can contribute to a sustainable future. It implements a **Hexagonal Architecture** microservice that estimates the **Carbon Footprint** of computational tasks using Machine Learning principles.

### Key Concepts
- **Carbon Awareness**: Understanding the environmental impact of code execution.
- **Energy Efficiency**: Calculating potential energy consumption ($kWh$) based on hardware load.
- **Clean Architecture**: Decoupling Domain logic from Frameworks (FastAPI).

## 🏗️ Architecture

The project follows the **Ports and Adapters** (Hexagonal) pattern:

- **`src/domain`**: Core entities (`ComputeTask`, `CarbonFootprint`). Pure Python.
- **`src/application`**: Use Cases (`EstimateEmissionUseCase`). Orchestrates logic.
- **`src/adapters`**: External Interfaces (ML Model, REST API).

## 🚀 How to Run

### Option 1: One-Command (Docker) 🐳
If you have Docker installed, simply run:

```bash
# Windows
./run.bat
```

The API will be available at: **http://localhost:8000/docs**

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn src.main:app --reload
```

## 🧪 Testing

We use `pytest` for quality assurance.

```bash
pytest
```

## 🎓 Education (IFSP)
This project is inspired by the **Pós-Graduação em Desenvolvimento Web e Mobile** at **IFSP Câmpus Capivari**.
- **Free & 100% EAD**.
- **Focus**: Web, Mobile, Systems Modeling, and Innovation.
- **Join us**: [cpv.ifsp.edu.br/pdev](https://cpv.ifsp.edu.br/pdev)

---
*Developed by Ramon Mendes - Software Engineer* 🦅
