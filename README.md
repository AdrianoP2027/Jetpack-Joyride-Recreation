# Jetpack Joyride Recreation

A 2D endless-runner game recreated in Python using Pygame Zero and event-driven programming.

In *Jetpack Joyride Recreation*, the player controls a character equipped with a jetpack and attempts to survive for as long as possible while avoiding dangerous obstacles. The player can fly through the environment, collect coins, activate power-ups, and unlock different jetpack flame cosmetics. The game becomes increasingly challenging as the player continues to survive.

## Gameplay

The objective is simple:

**Survive as long as possible and achieve the highest score.**

The player must:

* Use the Spacebar or Up Arrow to activate the jetpack
* Control the player's altitude by holding and releasing the jetpack
* Avoid incoming missiles and zappers
* Collect coins throughout the level
* Collect power-ups to gain temporary abilities
* Stay within the boundaries of the game
* Survive as long as possible to increase the score

The game continuously generates obstacles and collectibles, creating an unpredictable gameplay experience.

## Features

* Start screen and loading screen
* Main menu
* Tutorial and instructions screen
* 2D endless-runner gameplay
* Jetpack-based player movement
* Gravity and vertical velocity system
* Animated player movement
* Animated jetpack flames
* Multiple jetpack flame cosmetics
* Randomized obstacle spawning
* Multiple obstacle types
* Collision detection
* Coin collection system
* Power-up system
* Temporary shield power-up
* Cosmetic inventory system
* In-game shop
* Coin-based purchasing system
* Persistent high-score system
* Game-over state
* Player respawning
* Multiple game states
* Scrolling background
* 60 FPS gameplay

## Technologies

**Language**

* Python

**Framework / Library**

* Pygame Zero

**Programming Concepts**

* Event-Driven Programming
* Collision Detection
* Physics-Based Movement
* Gravity and Velocity
* Randomization
* Lists
* File I/O
* Game State Management
* Animation
* Object Management
* Timer-Based Systems

## Project Architecture

The game is organized into multiple systems, each responsible for a specific part of the gameplay.

### Player

Responsible for:

* Player position and movement
* Jetpack thrust
* Gravity and vertical velocity
* Player animation
* Screen boundaries
* Updating the player's state

### Obstacles

Responsible for:

* Creating obstacles
* Randomized obstacle selection
* Randomized vertical positions
* Moving obstacles across the screen
* Collision detection
* Removing obstacles after they leave the screen

### Coins

Responsible for:

* Randomized coin spawning
* Moving coins across the screen
* Detecting player collisions
* Increasing the player's coin total

### Power-Ups

Responsible for:

* Randomized power-up spawning
* Moving power-ups through the environment
* Detecting player collection
* Activating temporary abilities
* Managing the duration of active power-ups

### Cosmetics

Responsible for:

* Managing different jetpack flame designs
* Selecting owned cosmetics
* Displaying available flames
* Managing the player's inventory

### Shop

Responsible for:

* Displaying available cosmetics
* Managing coin costs
* Purchasing new flame designs
* Checking the player's available coins

### Game Menu

Responsible for:

* Displaying the main menu
* Starting the game
* Opening the cosmetics menu
* Opening the shop
* Opening the tutorial
* Exiting the game

### Game State Management

The game uses different states to control which part of the game is currently active:

* Start Screen
* Loading Screen
* Main Menu
* Gameplay
* Cosmetics
* Shop
* Game Over
* Tutorial

This allows individual systems to operate only when they are needed.

## Development Highlights

### Physics-Based Movement

The player movement system combines vertical velocity, gravity, and jetpack thrust.

When the player holds Spacebar or Up Arrow, upward thrust is applied. When the key is released, gravity increases the player's downward velocity.

The player is also restricted from moving beyond the upper and lower boundaries of the game.

### Randomized Obstacles

Obstacles are generated dynamically during gameplay rather than being placed manually.

Different obstacle types are randomly selected and positioned at different heights, requiring the player to continuously react to the changing environment.

### Coin & Inventory System

Coins can be collected during gameplay and are stored as the player's currency.

The currency can then be used in the shop to purchase different jetpack flame cosmetics. Purchased flames are stored in an inventory and can be selected from the cosmetics menu.

### Power-Up System

The game includes a shield power-up that temporarily protects the player from obstacles.

The power-up is activated when the player collides with it and remains active for a limited amount of time before automatically expiring.

### High-Score System

The game tracks the player's highest score and saves it to a text file using file I/O.

When the game starts, the saved high score is loaded so that progress is maintained between sessions.

### Game State Management

The game uses multiple states to control the application's different screens and systems.

This separates menus, gameplay, tutorials, cosmetics, and the shop so that gameplay logic does not continue running while the player is navigating other parts of the game.

## Problem Solving

Throughout development, several systems required debugging and careful coordination.

One challenge was managing the interaction between player movement, gravity, and jetpack thrust. The movement system needed to respond immediately when the player pressed or released the controls while keeping the player within the game boundaries.

Another challenge involved coordinating multiple moving objects at the same time. Obstacles, coins, and power-ups all move across the screen and require collision detection with the player.

The cosmetics and shop systems also required managing multiple states, including whether an item was owned, whether the player had enough coins, and which flame was currently selected.

Debugging these systems helped improve the organization of the game's variables, lists, functions, and game states.

## What I Learned

This project strengthened my understanding of Python programming and game development.

In particular, I developed a better understanding of:

* Designing a larger program using multiple interconnected systems
* Event-driven programming
* Creating physics-based movement
* Managing game states
* Implementing collision detection
* Using lists to manage multiple game objects
* Working with animations
* Using randomization to create dynamic gameplay
* Using file I/O to store persistent data
* Building inventory and purchasing systems
* Debugging interactions between different gameplay systems

The project also helped me understand how individual programming concepts can be combined to create a complete interactive application.

## Future Improvements

Potential future additions include:

* Additional power-ups
* More obstacle types
* Additional jetpack flame designs
* More advanced cosmetic systems
* Additional game environments
* More gameplay mechanics
* Improved difficulty progression
* Additional persistent player data
* Expanded shop functionality

## Project Status

**Completed**

The core gameplay systems, player movement, obstacle generation, collision detection, coin collection, power-ups, cosmetics, inventory, shop, scoring, high-score tracking, menus, tutorial, and game-state systems were implemented during development.
