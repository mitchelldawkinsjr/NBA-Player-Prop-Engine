# NBA Player Stats Probability Analyzer

## Overview
This tool analyzes NBA player statistics and calculates the probability of players achieving specific statistical thresholds in games. Using the Sportradar API, it retrieves player data across all NBA teams and applies Poisson probability distribution to predict the likelihood of players reaching certain benchmarks for points, rebounds, assists, three-pointers, blocks, and steals.

## Features
- Retrieves player statistics by team and season from the Sportradar API
- Calculates probability for players to reach specified thresholds in:
  - Points
  - Rebounds
  - Assists
  - Three-pointers made
  - Blocks
  - Steals
- Filters players based on minimum playing time (22+ minutes)
- Outputs probabilities as percentages, only displaying players who exceed a specified probability threshold

## Requirements
- Python 3.6+
- Required Python packages:
  - requests
  - pandas
  - json
  - math
  - argparse
  - time

## Installation
```bash
# Clone the repository
git clone [repository-url]
cd [repository-name]

# Install required packages
pip install requests pandas
```

## Configuration
Before using this tool, you need to set up your API credentials:

1. Sign up for a Sportradar API key at https://developer.sportradar.com/
2. Replace the `API_KEY` variable in the script with your actual API key:
   ```python
   API_KEY = "your_api_key_here"
   ```

## Usage
Run the script with the following parameters:

```bash
python nba_stats.py
```

To modify the statistical thresholds, edit the main function call at the bottom of the script:

```python
# Parameters: season_year, points, rebounds, assists, probability_threshold
main(2024, 15, 14, 14, 96)
```

- `season_year`: The NBA season to analyze (e.g., 2024)
- `points`: Minimum points threshold to calculate probability for
- `rebounds`: Minimum rebounds threshold to calculate probability for
- `assists`: Minimum assists threshold to calculate probability for
- `percent`: Minimum probability threshold (%) to display results

## Output
The script outputs player names and their probabilities of achieving the specified statistical thresholds. Only players with probabilities higher than the specified threshold (default: 96%) will be displayed.

Example output:
```
Season: 2024

Nikola Jokić | nuggets
Probability of 14 Rebounds is: 97.32%
Probability of 15 Points is: 99.87%
Probability of 14 Assists is: 96.51%

Luka Dončić | mavs
Probability of 15 Points is: 99.95%
```

## How It Works
1. The script iterates through all NBA teams
2. For each team, it retrieves player statistics for the specified season
3. For each player averaging 22+ minutes per game, it calculates the probability of achieving specified thresholds
4. Using the Poisson distribution, it determines the probability of a player achieving at least k occurrences of a statistic
5. It displays results only for players exceeding the probability threshold

## Note on API Rate Limiting
The script includes time delays between API calls to respect Sportradar's rate limiting:
```python
# Sleep for 1/2 second after each team stats have been pulled
time.sleep(.500)
```

## License
MIT License

## Acknowledgments
- [Sportradar API](https://developer.sportradar.com/) for providing NBA statistics data
