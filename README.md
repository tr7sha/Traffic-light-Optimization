# Markov Decision Process (MDP) - AI Final Project

## Overview
This project models a Markov Decision Process (MDP) for optimizing traffic light controls. Developed for the Artificial Intelligence course at SRM University.

## Features
- **Bellman Equations**: Implementation of Bellman's equations to find the optimal policy for traffic light control.
- **State Evaluation**: Calculates costs and defines value iteration to evaluate states.
- **Transition Probabilities**: Employs a probability counter for transition states based on real-world data.
- **Optimal Policy Calculation**: Determines the best action for each state to minimize costs and improve traffic flow.

## Technical Stack
- Python
- CSV for data handling
- Itertools for state combinations

## Usage
Run `main.py` to execute the MDP model. The program calculates the optimal traffic light control policy by analyzing state values and transition probabilities derived from traffic data.

## Repository Structure
- `main.py`: Contains the MDP model and the main algorithm for the project.
- `Data.csv`: Stores the traffic data used for calculating transition probabilities.
