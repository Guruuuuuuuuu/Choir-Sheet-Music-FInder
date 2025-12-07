#!/usr/bin/env python3
"""
Example usage of the Music Finder Bot
Demonstrates how to use the bot programmatically
"""

from music_finder_bot import MusicFinderBot


def example_basic_usage():
    """Basic usage example"""
    print("=" * 80)
    print("EXAMPLE 1: Basic Usage")
    print("=" * 80)
    
    # Initialize bot
    bot = MusicFinderBot()
    
    # Process a single instruction
    instruction = "Possible pieces for Capriccio: SATB that use overtone singing. And that are on the Spring Earth theme."
    result = bot.process_instruction(instruction)
    
    # Display results
    print(bot.format_results(result))


def example_multiple_instructions():
    """Example with multiple instructions"""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Multiple Instructions")
    print("=" * 80)
    
    bot = MusicFinderBot()
    
    instructions = [
        "Possible pieces for Capriccio: SATB that use overtone singing. And that are on the Spring Earth theme.",
        "Possible TB pieces that are on the Earth theme for Rhapsody. You could add \"beginning Tenor-Bass Choir\" to the search.",
        "Find SSA pieces about nature for intermediate choir."
    ]
    
    for i, instruction in enumerate(instructions, 1):
        print(f"\n--- Instruction {i} ---")
        result = bot.process_instruction(instruction)
        print(bot.format_results(result))


def example_accessing_parsed_data():
    """Example showing how to access parsed data programmatically"""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Accessing Parsed Data")
    print("=" * 80)
    
    bot = MusicFinderBot()
    
    instruction = "Possible TB pieces that are on the Earth theme for Rhapsody. You could add \"beginning Tenor-Bass Choir\" to the search."
    result = bot.process_instruction(instruction)
    
    # Access parsed parameters
    params = result['parsed_parameters']
    print(f"\nInstruction: {result['instruction']}")
    print(f"\nExtracted Parameters:")
    print(f"  Voicing: {params.get('voicing', 'Not specified')}")
    print(f"  Theme: {params.get('theme', 'Not specified')}")
    print(f"  Skill Level: {params.get('skill_level', 'Not specified')}")
    print(f"  Technique: {params.get('technique', 'Not specified')}")
    print(f"  Ensemble: {params.get('ensemble_name', 'Not specified')}")
    
    # Access search results
    print(f"\nFound {result['result_count']} result(s):")
    for i, piece in enumerate(result['search_results'], 1):
        print(f"\n  {i}. {piece.get('title')} by {piece.get('composer')}")


if __name__ == "__main__":
    example_basic_usage()
    example_multiple_instructions()
    example_accessing_parsed_data()

