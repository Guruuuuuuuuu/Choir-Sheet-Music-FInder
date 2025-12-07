#!/usr/bin/env python3
"""
Interactive CLI for Music Finder Bot
Allows users to input instructions and get sheet music results
"""

from music_finder_bot import MusicFinderBot
import sys


def main():
    """Interactive CLI interface"""
    print("=" * 80)
    print("MUSIC FINDER BOT - Interactive Mode")
    print("=" * 80)
    print("\nEnter instructions to find sheet music.")
    print("Type 'quit' or 'exit' to stop.\n")
    
    # Initialize bot
    api_key = None
    api_type = "web_search"
    
    # Check for API key in environment or command line args
    import os
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
        if len(sys.argv) > 2:
            api_type = sys.argv[2]
    elif os.getenv("MUSIC_FINDER_API_KEY"):
        api_key = os.getenv("MUSIC_FINDER_API_KEY")
        api_type = os.getenv("MUSIC_FINDER_API_TYPE", "web_search")
    
    bot = MusicFinderBot(api_key=api_key, api_type=api_type)
    
    while True:
        try:
            # Get user input
            instruction = input("\nEnter instruction: ").strip()
            
            if not instruction:
                continue
            
            if instruction.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break
            
            # Process instruction
            print("\nProcessing...")
            result = bot.process_instruction(instruction)
            
            # Display results
            print(bot.format_results(result))
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()

