#!/usr/bin/env python3
"""
Test script for CPDL API integration
"""

from music_finder_bot import MusicFinderBot

def test_cpdl_search():
    """Test CPDL API search functionality"""
    print("Testing CPDL API Integration...")
    print("=" * 80)
    
    # Initialize bot with CPDL API
    bot = MusicFinderBot(api_type="cpdl")
    
    # Test instruction
    instruction = "Find SATB pieces about nature"
    print(f"\nInstruction: {instruction}\n")
    
    result = bot.process_instruction(instruction)
    print(bot.format_results(result))
    
    # Test another instruction
    print("\n" + "=" * 80)
    instruction2 = "TB pieces for beginning choir"
    print(f"\nInstruction: {instruction2}\n")
    
    result2 = bot.process_instruction(instruction2)
    print(bot.format_results(result2))

if __name__ == "__main__":
    test_cpdl_search()

