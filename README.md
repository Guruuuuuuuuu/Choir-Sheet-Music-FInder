# Music Finder Bot

A bot that interprets natural language instructions to find sheet music based on specific parameters like voicing (SATB, TB, etc.), themes, techniques, and skill levels.

## Features

- **Natural Language Processing**: Parses instructions to extract key parameters:
  - Voicing (SATB, TB, TTBB, SSA, etc.)
  - Themes (Spring Earth, Earth, etc.)
  - Techniques (overtone singing, etc.)
  - Skill levels (beginning, intermediate, advanced)
  - Ensemble names (Capriccio, Rhapsody, etc.)
  - Additional keywords

- **CPDL API Integration**: Primary integration with Choral Public Domain Library (CPDL) using MediaWiki API
  - Searches the extensive CPDL database of public domain choral music
  - Extracts composer, voicing, and piece information
  - Returns direct links to sheet music pages
  - No API key required!

- **Structured Results**: Returns formatted results with:
  - Title and composer
  - Voicing information
  - Theme and technique
  - Difficulty level
  - Description and source

## Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: The bot uses the CPDL (Choral Public Domain Library) API by default, which requires the `requests` library. No API key is needed for CPDL!

## Usage

### Basic Usage

```python
from music_finder_bot import MusicFinderBot

# Initialize bot with CPDL API (default, no API key needed)
bot = MusicFinderBot(api_type="cpdl")

# Process an instruction
instruction = "Possible pieces for Capriccio: SATB that use overtone singing. And that are on the Spring Earth theme."
result = bot.process_instruction(instruction)

# Display formatted results
print(bot.format_results(result))
```

### Command Line Usage

Run the example script with sample instructions:
```bash
python music_finder_bot.py
```

### Interactive Mode

Run the interactive CLI to enter instructions one at a time:
```bash
python interactive_bot.py
```

You can also provide an API key as an argument:
```bash
python interactive_bot.py YOUR_API_KEY web_search
```

Or set environment variables:
```bash
export MUSIC_FINDER_API_KEY="your_api_key"
export MUSIC_FINDER_API_TYPE="web_search"
python interactive_bot.py
```

### Using with Real APIs

To use with a real API (e.g., Google Custom Search), initialize with an API key:

```python
bot = MusicFinderBot(api_key="YOUR_API_KEY", api_type="web_search")
```

## Example Instructions

1. "Possible pieces for Capriccio: SATB that use overtone singing. And that are on the Spring Earth theme."

2. "Possible TB pieces that are on the Earth theme for Rhapsody. You could add 'beginning Tenor-Bass Choir' to the search."

## Project Structure

- `music_finder_bot.py` - Main bot implementation
- `interactive_bot.py` - Interactive CLI interface
- `requirements.txt` - Python dependencies
- `README.md` - This file

## API Integration

The bot supports multiple API backends:

- **CPDL API** (default): Uses Choral Public Domain Library's MediaWiki API
  - No API key required
  - Searches thousands of public domain choral pieces
  - Returns direct links to sheet music
  - Usage: `bot = MusicFinderBot(api_type="cpdl")`

- **Mock Mode**: Returns sample results for testing
  - Usage: `bot = MusicFinderBot(api_type="mock")`

- **Web Search API**: Ready for Google Custom Search API integration
  - Requires API key
  - Usage: `bot = MusicFinderBot(api_key="YOUR_KEY", api_type="web_search")`

- **OpenAI API**: Ready for OpenAI API integration
  - Requires API key
  - Usage: `bot = MusicFinderBot(api_key="YOUR_KEY", api_type="openai")`

## Extending the Bot

### Adding New Parameter Patterns

Edit the `InstructionParser` class to add new patterns:
- Add to `VOICING_PATTERNS` for new voicing types
- Add to `SKILL_LEVEL_PATTERNS` for new skill levels
- Add to `THEME_PATTERNS` for new themes

### Adding New APIs

1. Add a new method in `SheetMusicAPI` class (e.g., `_custom_api_search`)
2. Update the `search` method to handle the new API type
3. Initialize the bot with `api_type="custom_api"`

## License

This project is open source and available for use.

