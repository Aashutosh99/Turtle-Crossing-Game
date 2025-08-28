# 🐢 Turtle Crossing Game  

A fun Python game built using the `turtle` graphics module where you guide a turtle across the road while avoiding cars. Each successful crossing increases your score and the difficulty level. 🚦  

---

## 🎮 Game Overview  
- You control a **turtle** trying to cross from the bottom to the top of the screen.  
- **Cars** spawn randomly and move across the road.  
- Each successful crossing:  
  - Resets the turtle to the start position.  
  - Increases your score.  
  - Increases car speed (higher difficulty).  
- Collision with a car ends the game.  

---

## 📂 Project Structure  

```
turtle-crossing-game/
│── main.py          # Main game loop
│── player.py        # Player class (the turtle)
│── car_manager.py   # Manages car creation & movement
│── scoreboard.py    # Handles score display & game over screen
│── README.md        # Project documentation
```

---

## ⚙️ Setup Instructions  

### 🔹 Uploading this project to GitHub  
Run these commands in your project folder:  
```bash
git init
git add .
git commit -m "Initial commit - Turtle Crossing Game"
git branch -M main
git remote add origin https://github.com/Aashutosh99/my_python_projects.git
git push -u origin main
```



### 🔹 Cloning the project  
Once uploaded, anyone can clone it by running:  
```bash
git clone https://github.com/Aashutosh99/my_python_projects.git
cd turtle-crossing-game
```

### 🔹 Running the game  
Make sure you have **Python 3.x** installed, then run:  
```bash
python main.py
```

---

## ⌨️ Controls  
- **↑ Arrow Key** → Move the turtle upward.  


## 🚀 Features  
- Smooth turtle movement.  
- Random car generation.  
- Increasing difficulty with each level.  
- Score tracking.  
- Collision effects (color changes & background change).  

---

## 🛠️ Future Improvements  
- Add lives system instead of instant game over.  
- Introduce different car types & speeds.  

---

## 🧑‍💻 Author  
Developed by Aashutosh
