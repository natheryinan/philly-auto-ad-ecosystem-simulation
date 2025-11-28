
# Philadelphia Auto Ad Ecosystem Simulation

This repository contains simulation models for understanding how online advertising
budget strategies affect exposure, click-throughs, and conversions in the Greater
Philadelphia automotive market (new car dealers, used car dealers, and private sellers).

The project includes:

### **1. Demand & Traffic Modeling**
- Simple probabilistic demand model for daily ad impressions.
- Region-level controls (e.g., reach in different Philadelphia neighborhoods).
- Scenario generation for 30–90 day forecast windows.

### **2. Auction & Bidding Simulation**
- Basic ad auction logic similar to Google Ads:
  - Query value  
  - Bid amount  
  - Quality score  
  - AdRank  
- Simulation of winning probability and cost per click (CPC).

### **3. Budget Allocation**
- Daily $100 budget example.
- Models budget burn rate, impression wins, and expected offline conversions.
- Tracks ROI contribution over 30–60 days.

### **4. Scenario Tree Planner**
- Generates multiple possible futures of daily demand.
- Allows “look-ahead” style decisions:
  - Pick the ad action that performs best across scenarios.
- Useful for budget pacing and multi-day planning.

### **5. Code & Outputs**
- `deepseek_python_*.py` — simulation code
- `deepseek_markdown_*.md` — design notes and model description
- `RESULTS.ini` — output logs from example runs
- `online_budget_scenario_tree.png` — look-ahead planning diagram

---

## **How to Run**
From the project folder:

```bash
python philadelphia_auto_ad_ecosystem.py
