"""
Music Finder Bot
A bot that interprets instructions to find sheet music based on specific parameters.
"""

import re
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


@dataclass
class SearchParameters:
    """Structured parameters extracted from instructions"""
    voicing: Optional[str] = None  # SATB, TB, TTBB, etc.
    theme: Optional[str] = None  # Spring Earth, Earth, etc.
    technique: Optional[str] = None  # overtone singing, etc.
    skill_level: Optional[str] = None  # beginning, intermediate, advanced
    ensemble_name: Optional[str] = None  # Capriccio, Rhapsody, etc.
    additional_keywords: List[str] = None  # Any other relevant search terms
    
    def __post_init__(self):
        if self.additional_keywords is None:
            self.additional_keywords = []


class InstructionParser:
    """Parses natural language instructions to extract search parameters"""
    
    # Common voicing patterns
    VOICING_PATTERNS = {
        r'\bSATB\b': 'SATB',
        r'\bTB\b': 'TB',
        r'\bTTBB\b': 'TTBB',
        r'\bSSA\b': 'SSA',
        r'\bSSAA\b': 'SSAA',
        r'\bSAB\b': 'SAB',
        r'\btenor-bass\b': 'TB',
        r'\btenor bass\b': 'TB',
        r'\bTenor-Bass\b': 'TB',
        r'\bTenor Bass\b': 'TB',
    }
    
    # Skill level patterns
    SKILL_LEVEL_PATTERNS = {
        r'\bbeginning\b': 'beginning',
        r'\bbeginner\b': 'beginning',
        r'\bintermediate\b': 'intermediate',
        r'\badvanced\b': 'advanced',
        r'\bemerging\b': 'beginning',
    }
    
    # Common themes
    THEME_PATTERNS = {
        r'Spring Earth': 'Spring Earth',
        r'Earth theme': 'Earth',
        r'Earth': 'Earth',
        r'Spring': 'Spring',
    }
    
    def parse(self, instruction: str) -> SearchParameters:
        """Parse instruction and extract parameters"""
        instruction_lower = instruction.lower()
        params = SearchParameters()
        
        # Extract voicing
        for pattern, voicing in self.VOICING_PATTERNS.items():
            if re.search(pattern, instruction, re.IGNORECASE):
                params.voicing = voicing
                break
        
        # Extract skill level
        for pattern, level in self.SKILL_LEVEL_PATTERNS.items():
            if re.search(pattern, instruction_lower):
                params.skill_level = level
                break
        
        # Extract theme
        for pattern, theme in self.THEME_PATTERNS.items():
            if re.search(pattern, instruction, re.IGNORECASE):
                params.theme = theme
                break
        
        # Extract techniques (overtone singing, etc.)
        if re.search(r'overtone singing', instruction_lower):
            params.technique = 'overtone singing'
        
        # Extract ensemble name (Capriccio, Rhapsody, etc.)
        # Pattern 1: "for Capriccio:" or "for Rhapsody."
        ensemble_match = re.search(r'for\s+(\w+)[:.]', instruction, re.IGNORECASE)
        if ensemble_match:
            params.ensemble_name = ensemble_match.group(1)
        # Pattern 2: "for Rhapsody" at the end
        if not params.ensemble_name:
            ensemble_match = re.search(r'for\s+(\w+)\s*\.', instruction, re.IGNORECASE)
            if ensemble_match:
                params.ensemble_name = ensemble_match.group(1)
        
        # Extract additional keywords from quoted text
        quoted_text = re.findall(r'"([^"]+)"', instruction)
        params.additional_keywords.extend(quoted_text)
        
        # Extract any other important keywords
        important_keywords = ['choir', 'choral', 'piece', 'pieces']
        for keyword in important_keywords:
            if keyword in instruction_lower and keyword not in params.additional_keywords:
                params.additional_keywords.append(keyword)
        
        return params


class SheetMusicAPI:
    """Interface for sheet music search APIs"""
    
    def __init__(self, api_key: Optional[str] = None, api_type: str = "web_search"):
        """
        Initialize API client
        
        Args:
            api_key: API key for the service (if required)
            api_type: Type of API to use ("web_search", "openai", etc.)
        """
        self.api_key = api_key
        self.api_type = api_type
    
    def build_search_query(self, params: SearchParameters) -> str:
        """Build a search query from parameters"""
        query_parts = []
        
        if params.voicing:
            query_parts.append(params.voicing)
        
        if params.theme:
            query_parts.append(params.theme)
        
        if params.technique:
            query_parts.append(params.technique)
        
        if params.skill_level:
            query_parts.append(f"{params.skill_level} choir")
        
        if params.ensemble_name:
            query_parts.append(params.ensemble_name)
        
        query_parts.extend(params.additional_keywords)
        
        # Add sheet music specific terms
        query_parts.extend(["sheet music", "choral piece", "choral music"])
        
        return " ".join(query_parts)
    
    def search(self, params: SearchParameters) -> List[Dict[str, Any]]:
        """
        Search for sheet music based on parameters
        
        Returns:
            List of dictionaries containing sheet music information
        """
        query = self.build_search_query(params)
        
        if self.api_type == "web_search":
            return self._web_search(query, params)
        elif self.api_type == "openai":
            return self._openai_search(query, params)
        else:
            # Fallback: return mock data for demonstration
            return self._mock_search(params)
    
    def _web_search(self, query: str, params: SearchParameters) -> List[Dict[str, Any]]:
        """Perform web search (requires API key for Google Custom Search or similar)"""
        # This is a placeholder - you would integrate with Google Custom Search API
        # or another search API here
        if not self.api_key:
            print("Warning: No API key provided. Using mock results.")
            return self._mock_search(params)
        
        # Example integration (uncomment and configure when you have an API key):
        # url = f"https://www.googleapis.com/customsearch/v1"
        # params_dict = {
        #     "key": self.api_key,
        #     "cx": "YOUR_SEARCH_ENGINE_ID",
        #     "q": query
        # }
        # response = requests.get(url, params=params_dict)
        # return self._parse_search_results(response.json())
        
        return self._mock_search(params)
    
    def _openai_search(self, query: str, params: SearchParameters) -> List[Dict[str, Any]]:
        """Use OpenAI API to search for sheet music"""
        if not self.api_key:
            print("Warning: No OpenAI API key provided. Using mock results.")
            return self._mock_search(params)
        
        # This would use OpenAI's API to generate search results
        # Implementation would go here
        
        return self._mock_search(params)
    
    def _mock_search(self, params: SearchParameters) -> List[Dict[str, Any]]:
        """Return mock search results for demonstration"""
        results = []
        
        # Generate results based on parameters
        if params.voicing == "SATB" and params.theme and "overtone" in str(params.technique).lower():
            results.append({
                "title": "Singing in Tune with Nature",
                "composer": "Amanda Cole",
                "voicing": "SATB",
                "technique": "Overtone singing / Microtonal just intonation",
                "theme": "Nature/Earth",
                "description": "SATB choral work utilizing microtonal just intonation tuning, creating shimmering clouds of lush overtones",
                "source": "N.E.O. Voice Festival 2020",
                "difficulty": "Advanced"
            })
        
        if params.voicing == "TB" and params.theme and "Earth" in params.theme:
            results.append({
                "title": "For the Beauty of the Earth",
                "composer": "John Rutter",
                "voicing": "TTBB",
                "theme": "Earth",
                "description": "Celebrates the beauty of the natural world, available in TTBB arrangement",
                "source": "Various publishers",
                "difficulty": params.skill_level or "Intermediate"
            })
            
            if params.skill_level == "beginning":
                results.append({
                    "title": "First Songs for Emerging Tenor-Bass Choir",
                    "composer": "Mark Patterson (arr.)",
                    "voicing": "TB",
                    "theme": "Nature/Earth",
                    "description": "Collection for emerging tenor-bass choirs including 'Come Sail Away with Me,' 'A Future Shared,' and 'Gloucester Moors'",
                    "source": "Carl Fischer",
                    "difficulty": "Beginning"
                })
        
        # If no specific matches, return generic results
        if not results:
            results.append({
                "title": f"Choral Piece - {params.voicing or 'Mixed'}",
                "composer": "Various",
                "voicing": params.voicing or "Mixed",
                "theme": params.theme or "General",
                "description": f"Sheet music matching: {params.voicing or ''} {params.theme or ''} {params.technique or ''}",
                "source": "Music database",
                "difficulty": params.skill_level or "Various"
            })
        
        return results


class MusicFinderBot:
    """Main bot class that orchestrates instruction parsing and sheet music search"""
    
    def __init__(self, api_key: Optional[str] = None, api_type: str = "web_search"):
        self.parser = InstructionParser()
        self.api = SheetMusicAPI(api_key=api_key, api_type=api_type)
    
    def process_instruction(self, instruction: str) -> Dict[str, Any]:
        """
        Process an instruction and return sheet music results
        
        Args:
            instruction: Natural language instruction for finding sheet music
            
        Returns:
            Dictionary containing parsed parameters and search results
        """
        # Parse instruction
        params = self.parser.parse(instruction)
        
        # Search for sheet music
        results = self.api.search(params)
        
        return {
            "instruction": instruction,
            "parsed_parameters": asdict(params),
            "search_results": results,
            "result_count": len(results)
        }
    
    def format_results(self, result_dict: Dict[str, Any]) -> str:
        """Format results as a readable string"""
        output = []
        output.append("=" * 80)
        output.append("MUSIC FINDER BOT RESULTS")
        output.append("=" * 80)
        output.append(f"\nInstruction: {result_dict['instruction']}")
        output.append("\nParsed Parameters:")
        params = result_dict['parsed_parameters']
        for key, value in params.items():
            if value:
                output.append(f"  - {key.replace('_', ' ').title()}: {value}")
        
        output.append(f"\n\nFound {result_dict['result_count']} result(s):\n")
        
        for i, result in enumerate(result_dict['search_results'], 1):
            output.append(f"\n{i}. {result.get('title', 'Unknown Title')}")
            output.append(f"   Composer: {result.get('composer', 'Unknown')}")
            output.append(f"   Voicing: {result.get('voicing', 'N/A')}")
            if result.get('technique'):
                output.append(f"   Technique: {result['technique']}")
            output.append(f"   Theme: {result.get('theme', 'N/A')}")
            output.append(f"   Difficulty: {result.get('difficulty', 'N/A')}")
            output.append(f"   Description: {result.get('description', 'N/A')}")
            output.append(f"   Source: {result.get('source', 'N/A')}")
        
        output.append("\n" + "=" * 80)
        return "\n".join(output)


def main():
    """Example usage of the Music Finder Bot"""
    # Initialize bot (no API key needed for mock mode)
    bot = MusicFinderBot()
    
    # Sample instructions
    instructions = [
        "Possible pieces for Capriccio: SATB that use overtone singing. And that are on the Spring Earth theme.",
        "Possible TB pieces that are on the Earth theme for Rhapsody. You could add \"beginning Tenor-Bass Choir\" to the search."
    ]
    
    # Process each instruction
    for instruction in instructions:
        result = bot.process_instruction(instruction)
        print(bot.format_results(result))
        print("\n")


if __name__ == "__main__":
    main()

