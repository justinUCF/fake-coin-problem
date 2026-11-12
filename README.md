# The Fake Coin Problem
**Authors:** Giorgio Miguel Torregrosa and Justin Gamboa
**Course:** COT5405 - Design and Analysis of Algorithms

## Overview
This project simulates the Fake Coin Problem: Identifying a single fake coin among N identical weighted coins using two approaches: **Brute Force** and **Divide & Conquer**. 

## Requirements
- Python 3.6+

## How to Run
From the project root:

```bash
python src/main.py
```

### Modes
Select a mode using the --mode flag (default: simulation):

```bash
python src/main.py --mode simulation
```

|Mode|Description|
|-|-|
|simulation|Runs a quick smoke test starting at a user-specified coin count, incrementing by 2,048 coins over 10 iterations with 5 runs each|
