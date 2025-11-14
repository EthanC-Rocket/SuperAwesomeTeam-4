# GameHub - Multi-Game Platform

A web application featuring a collection of mini-games with user authentication and score tracking. Built with React.js frontend and Python Flask backend.

## Features

- **User Authentication**: Register and login to track your scores
- **Score Tracking**: Your best scores are saved and displayed in the hub
- **Mini-Games**:
  - 🔢 **Sudoku**: Classic number puzzle game
  - 🚀 **RocketMans**: Navigate your rocket through obstacles
  - ⚔️ **Dungeon Crawler**: Explore dungeons, fight monsters, and level up
  - 🧠 **Personality Quiz**: Discover your personality type
  - 🤔 **Would You Rather**: Make choices and get personality insights
  - 📜 **Zork**: Classic text adventure
  - 👾 **One Night At Rocket**: Arcade-style challenge
  - 🪨 **Rocxs**: Interactive image toggle game

## Project Structure

- `backend/` - Flask API, authentication, score management
- `frontend/` - React app, game components, routing
- `frontend/src/components/games/` - All game components
- `would-you-rather-questions.json` - Data for Would You Rather game

## Setup Instructions

### Unified Setup (Frontend & Backend)

1. From the project root, run:
   ```powershell
   npm install
   npm start
   ```
   This will:
   - Install all frontend requirements
   - Install backend requirements
   - Start the React development server
   - Start the backend Flask APIs automatically
   The frontend runs on `http://localhost:3000` and the backend runs on `http://localhost:5000`.

## How to Use

1. Start the unified setup (see above)
2. Open your browser to `http://localhost:3000`
3. Register an account or continue as a guest
4. Click on any game to start playing
5. Your scores will be saved if you're logged in and displayed in the hub

## Game Controls

- **Sudoku**: Click cells to select, use number pad to fill
- **RocketMans**: Press SPACE or ↑ to fly
- **Dungeon Crawler**: Use arrow keys to move and attack
- **Personality Quiz**: Click your preferred answers
- **Would You Rather**: Choose between two options
- **Zork**: Type commands to play
- **One Night At Rocket**: Arcade controls
- **Rocxs**: Click the image to toggle

## API & Proxy

- React frontend proxies API requests to Flask backend via `frontend/package.json` (`"proxy": "http://localhost:5000"`).
- Would You Rather game may use a separate API endpoint (`http://127.0.0.1:8000`).

## Dependencies

- Backend: See `backend/requirements.txt`
- Frontend: Installed automatically with `npm install` (see `frontend/package.json`)

## Authors
- NextGen Academy Team 4
