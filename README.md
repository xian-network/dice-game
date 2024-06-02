# Dice Game

Example Smart Contract based Dice game with random functions and house edge. Range based dice with multiplier winnings based on range.

## Installation for Tests

### Ubuntu 22.04

Follow these steps to set up the environment on Ubuntu 22.04:

1. **Update and prepare the system:**

   ```bash
   sudo apt-get update
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt-get update
   ```

2. **Install necessary packages:**

   ```bash
   sudo apt-get install pkg-config python3.11 python3.11-dev python3.11-venv libhdf5-dev build-essential
   ```

3. **Clone Contracting:**

   ```bash
   git clone https://github.com/xian-network/xian-contracting
   git clone https://github.com/xian-network/dice-game.git
   ```

4. **Set up Python virtual environment and dependencies:**

   ```bash
   python3.11 -m venv xian_venv
   source xian_venv/bin/activate
   pip install -e xian-contracting/
   ```

5. **Run the tests**

   ```bash
   cd dice-game/tests
   python3.11 test_dice.py
   ```

## Deploy

Use the wallet to submit the con_uberdice.py contract contents.
