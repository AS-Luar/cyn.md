#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Speech Understanding Module for Voice Assistant

This is a complete solution for the speech understanding exercise.
It implements intent recognition, entity extraction, context management,
and dialog generation for a voice assistant.
"""

import re
import json
import time
import os
import random

class IntentRecognizer:
    """A class for recognizing user intents from speech text using regex patterns."""
    
    def __init__(self):
        """Initialize the intent recognizer with predefined patterns."""
        # Initialize intent patterns
        self.intent_patterns = {
            "greeting": [
                r"(hello|hi|hey|greetings)( there| assistant| voice assistant)?",
                r"good (morning|afternoon|evening)"
            ],
            "farewell": [
                r"(goodbye|bye|see you( later)?)",
                r"(exit|quit|stop)( assistant| program)?"
            ],
            "weather_inquiry": [
                r"(what|how)('s| is) (the )?weather( like)?( in (?P<location>\w+))?",
                r"(weather|forecast)( in| for) (?P<location>[\w\s]+)",
                r"is it (going to|gonna) (rain|snow|be sunny)( in (?P<location>\w+))?"
            ],
            "time_inquiry": [
                r"what('s| is) (the )?time( now)?",
                r"(tell|give) me the (current |)time",
                r"what time is it"
            ],
            "date_inquiry": [
                r"what('s| is) (the )?date( today)?",
                r"what day is (it|today)",
                r"(tell|give) me the (current |)date"
            ],
            "device_control": [
                r"(turn|switch) (?P<action>on|off) (the )?(?P<device>[\w\s]+)( please)?",
                r"(dim|brighten) (the )?(?P<device>[\w\s]+)( please)?"
            ],
            "timer_set": [
                r"(set|start) a timer for (?P<duration>[\w\s]+)( please)?",
                r"timer for (?P<duration>[\w\s]+)( please)?"
            ],
            "general_question": [
                r"(who|what|where|when|why|how) (is|are|was|were|do|does) [\w\s]+",
                r"(can|could) you (tell|explain) [\w\s]+"
            ]
        }
    
    def detect_intent(self, text):
        """
        Detect the intent from the given text.
        
        Args:
            text: The text to analyze
            
        Returns:
            A tuple of (intent, entities) where entities is a dictionary
        """
        # Convert text to lowercase for case-insensitive matching
        text = text.lower()
        
        # Check each intent and its patterns
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    # Extract entities from the match
                    entities = self._extract_entities(intent, match, text)
                    return intent, entities
        
        # No match found, return unknown intent
        return "unknown_intent", {}
    
    def _extract_entities(self, intent, match, original_text):
        """
        Extract entities based on the matched pattern and intent.
        
        Args:
            intent: The detected intent
            match: The regex match object
            original_text: The original text input
            
        Returns:
            A dictionary of extracted entities
        """
        entities = {}
        
        # Extract named groups from the regex match
        for group_name in match.groupdict():
            entities[group_name] = match.group(group_name)
        
        # Additional processing for specific intents
        if intent == "weather_inquiry" and "location" not in entities:
            # Try to find location after "in" or "for"
            location_match = re.search(r"(in|for) (?P<location>[\w\s]+)$", original_text.lower())
            if location_match:
                entities["location"] = location_match.group("location").strip()
        
        elif intent == "timer_set" and "duration" in entities:
            # Convert duration text to seconds
            duration_text = entities["duration"]
            entities["seconds"] = self._parse_duration(duration_text)
            
        return entities
    
    def _parse_duration(self, duration_text):
        """
        Parse a duration string into seconds.
        
        Args:
            duration_text: Text like "5 minutes", "1 hour and 30 seconds", etc.
            
        Returns:
            Duration in seconds or None if parsing fails
        """
        total_seconds = 0
        
        # Try to extract hours
        hour_match = re.search(r"(\d+)(\s+)?(hour|hr)", duration_text)
        if hour_match:
            hours = int(hour_match.group(1))
            total_seconds += hours * 3600
        
        # Try to extract minutes
        minute_match = re.search(r"(\d+)(\s+)?(minute|min)", duration_text)
        if minute_match:
            minutes = int(minute_match.group(1))
            total_seconds += minutes * 60
        
        # Try to extract seconds
        second_match = re.search(r"(\d+)(\s+)?(second|sec)", duration_text)
        if second_match:
            seconds = int(second_match.group(1))
            total_seconds += seconds
        
        # If nothing was matched but there's a number, assume it's seconds
        if total_seconds == 0:
            number_match = re.search(r"(\d+)", duration_text)
            if number_match:
                total_seconds = int(number_match.group(1))
        
        return total_seconds if total_seconds > 0 else None


class KeywordIntentRecognizer:
    """A class for recognizing intents based on keywords and phrases."""
    
    def __init__(self):
        """Initialize with intent keywords."""
        self.intent_keywords = {
            "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
            "farewell": ["goodbye", "bye", "see you", "exit", "quit", "stop"],
            "weather_inquiry": ["weather", "forecast", "temperature", "sunny", "rainy", "cloudy"],
            "time_inquiry": ["time", "clock", "hour"],
            "date_inquiry": ["date", "day", "today", "calendar"],
            "device_control": ["turn on", "turn off", "switch on", "switch off", "dim", "brighten"],
            "timer_set": ["timer", "set timer", "alarm", "reminder"],
            "general_question": ["who", "what", "where", "when", "why", "how"]
        }
    
    def detect_intent(self, text):
        """
        Detect intent based on keyword matching.
        
        Args:
            text: The text to analyze
            
        Returns:
            The most likely intent
        """
        text = text.lower()
        
        # Count keyword matches for each intent
        matches = {intent: 0 for intent in self.intent_keywords}
        
        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    matches[intent] += 1
        
        # Find intent with most matches
        max_matches = 0
        best_intent = "unknown_intent"
        
        for intent, count in matches.items():
            if count > max_matches:
                max_matches = count
                best_intent = intent
        
        # Return unknown if no keywords matched
        if max_matches == 0:
            return "unknown_intent", {}
            
        # Simple entity extraction based on intent
        entities = self._extract_basic_entities(best_intent, text)
        return best_intent, entities
    
    def _extract_basic_entities(self, intent, text):
        """
        Extract basic entities based on the intent.
        
        Args:
            intent: The detected intent
            text: The original text
            
        Returns:
            A dictionary of extracted entities
        """
        entities = {}
        
        if intent == "weather_inquiry":
            # Try to extract location
            location_match = re.search(r"(in|at|for) ([\w\s]+)$", text.lower())
            if location_match:
                entities["location"] = location_match.group(2).strip()
        
        elif intent == "device_control":
            # Try to extract device and action
            if "turn on" in text or "switch on" in text:
                entities["action"] = "on"
            elif "turn off" in text or "switch off" in text:
                entities["action"] = "off"
                
            # Crude device extraction - get text after "turn on/off"
            device_match = re.search(r"(turn|switch) (on|off) (the )?([\w\s]+)", text.lower())
            if device_match:
                entities["device"] = device_match.group(4).strip()
        
        return entities


class ContextManager:
    """A class for managing conversational context."""
    
    def __init__(self):
        """Initialize with empty context values."""
        self.reset_context()
    
    def reset_context(self):
        """Reset the context to initial state."""
        self.current_context = {
            "last_intent": None,
            "entities": {},
            "conversation_history": [],
            "session_start_time": time.time()
        }
    
    def update_context(self, intent, entities, user_input):
        """
        Update the context with new information.
        
        Args:
            intent: The detected intent
            entities: Dictionary of extracted entities
            user_input: The original user input
        """
        # Store the current interaction
        self.current_context["last_intent"] = intent
        
        # Merge new entities with existing ones, with new values taking precedence
        self.current_context["entities"].update(entities)
        
        # Add to conversation history
        self.current_context["conversation_history"].append({
            "user_input": user_input,
            "intent": intent,
            "entities": entities.copy(),
            "timestamp": time.time()
        })
        
        # Trim history if it gets too long (keep last 10)
        if len(self.current_context["conversation_history"]) > 10:
            self.current_context["conversation_history"] = self.current_context["conversation_history"][-10:]
    
    def get_context(self):
        """Get the current context."""
        return self.current_context
    
    def get_last_intent(self):
        """Get the last detected intent."""
        return self.current_context["last_intent"]
    
    def get_entity(self, entity_name, default=None):
        """Get a specific entity value if it exists."""
        return self.current_context["entities"].get(entity_name, default)
    
    def get_conversation_duration(self):
        """Get the duration of the current conversation session in seconds."""
        start_time = self.current_context["session_start_time"]
        return time.time() - start_time


class DialogManager:
    """A class for managing dialog flow and generating responses."""
    
    def __init__(self):
        """Initialize with intent recognizer and context manager."""
        self.intent_recognizer = IntentRecognizer()
        self.context_manager = ContextManager()
        
    def process_input(self, user_input):
        """
        Process user input and generate a response.
        
        Args:
            user_input: The text input from the user
            
        Returns:
            A string response to the user
        """
        # Skip empty inputs
        if not user_input.strip():
            return "I didn't hear anything. Can you say that again?"
        
        # Detect intent and extract entities
        intent, entities = self.intent_recognizer.detect_intent(user_input)
        
        # Handle unknown intents using context
        if intent == "unknown_intent":
            last_intent = self.context_manager.get_last_intent()
            
            # If we have a previous intent, try to interpret the input in that context
            if last_intent == "weather_inquiry":
                # Check for time references (tomorrow, next week, etc.)
                if any(word in user_input.lower() for word in ["tomorrow", "next", "later", "weekend"]):
                    intent = "weather_inquiry"
                    entities["time"] = self._extract_time_reference(user_input)
                    entities["location"] = self.context_manager.get_entity("location", "current location")
            
            # Add more contextual handling for other intents as needed
        
        # Update context with new information
        self.context_manager.update_context(intent, entities, user_input)
        
        # Generate response based on intent and entities
        response = self.generate_response(intent, entities)
        
        return response
    
    def _extract_time_reference(self, text):
        """Extract time reference from text."""
        text = text.lower()
        if "tomorrow" in text:
            return "tomorrow"
        elif "weekend" in text:
            return "this weekend"
        elif "next week" in text:
            return "next week"
        elif "tonight" in text or "evening" in text:
            return "this evening"
        else:
            return "soon"  # Default fallback
    
    def generate_response(self, intent, entities):
        """
        Generate a response based on intent and entities.
        
        Args:
            intent: The detected intent
            entities: Dictionary of extracted entities
            
        Returns:
            A string response to the user
        """
        if intent == "greeting":
            responses = [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Greetings! How may I assist you?"
            ]
            return random.choice(responses)
            
        elif intent == "farewell":
            responses = [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye for now!"
            ]
            return random.choice(responses)
            
        elif intent == "weather_inquiry":
            location = entities.get("location", "current location")
            time_ref = entities.get("time", "today")
            
            # In a real system, you would call a weather API here
            weather_conditions = ["sunny", "partly cloudy", "rainy", "overcast", "clear", "stormy"]
            temperatures = list(range(65, 85))
            
            condition = random.choice(weather_conditions)
            temp = random.choice(temperatures)
            
            return f"The weather for {location} {time_ref} is {condition} with a high of {temp}°F."
            
        elif intent == "time_inquiry":
            current_time = time.strftime("%I:%M %p")
            return f"The current time is {current_time}."
            
        elif intent == "date_inquiry":
            current_date = time.strftime("%A, %B %d, %Y")
            return f"Today is {current_date}."
            
        elif intent == "device_control":
            device = entities.get("device", "unknown device")
            action = entities.get("action", "unknown action")
            
            # In a real system, you would control actual devices here
            return f"{device.capitalize()} has been turned {action}."
            
        elif intent == "timer_set":
            duration_text = entities.get("duration", "some time")
            seconds = entities.get("seconds", 60)  # Default to 60 seconds
            
            # In a real system, you would start an actual timer
            if seconds == 1:
                return f"Timer set for 1 second."
            else:
                return f"Timer set for {seconds} seconds."
            
        elif intent == "general_question":
            # In a real system, you would use a knowledge base or external API
            return "That's an interesting question. In a complete voice assistant, I would search for that information for you."
            
        else:  # unknown_intent
            responses = [
                "I'm not sure I understand. Could you rephrase that?",
                "I didn't quite get that. Can you say it differently?",
                "I'm still learning and didn't understand that request."
            ]
            return random.choice(responses)


def simulate_conversation():
    """Run a simulated conversation with the dialog manager."""
    dialog_manager = DialogManager()
    
    print("=== Voice Assistant Simulation ===")
    print("Type your messages and the assistant will respond.")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nAssistant: Goodbye! Have a nice day!")
            break
            
        response = dialog_manager.process_input(user_input)
        print(f"Assistant: {response}\n")


def simulate_vosk_integration():
    """
    Simulate the integration with Vosk by processing predefined transcripts.
    In a real implementation, this would use actual Vosk transcriptions.
    """
    print("=== Simulated Vosk Integration ===\n")
    print("This simulation processes text as if it came from Vosk speech recognition.\n")
    
    # Create our dialog manager
    dialog_manager = DialogManager()
    
    # Simulated speech recognition results
    simulated_transcripts = [
        {"text": "hello assistant"},
        {"text": "what's the weather like in boston"},
        {"text": ""},  # Simulate a failed recognition
        {"text": "will it rain tomorrow"},
        {"text": "set a timer for two minutes"},
        {"text": "thank you goodbye"}
    ]
    
    # Process each transcript
    for transcript in simulated_transcripts:
        user_text = transcript.get("text", "")
        
        if user_text:
            print(f"Speech recognized: \"{user_text}\"")
            response = dialog_manager.process_input(user_text)
            print(f"Assistant response: {response}\n")
        else:
            print("Speech recognition failed or no speech detected.")
            print("Assistant response: I didn't catch that. Could you try again?\n")


def run_tests():
    """Run unit tests for the speech understanding components."""
    # Test IntentRecognizer
    print("=== Testing IntentRecognizer ===")
    recognizer = IntentRecognizer()
    test_phrases = [
        "Hello there",
        "What's the weather like today",
        "What's the weather like in London",
        "What time is it",
        "Turn on the kitchen lights",
        "Set a timer for 5 minutes",
        "Who is the president"
    ]
    
    for phrase in test_phrases:
        intent, entities = recognizer.detect_intent(phrase)
        print(f"Phrase: \"{phrase}\"")
        print(f"Intent: {intent}")
        print(f"Entities: {entities}")
        print()
    
    # Test ContextManager
    print("=== Testing ContextManager ===")
    context_manager = ContextManager()
    
    # Process first utterance
    utterance1 = "What's the weather like in New York?"
    intent1, entities1 = recognizer.detect_intent(utterance1)
    context_manager.update_context(intent1, entities1, utterance1)
    
    print("After first utterance:")
    print(f"Last intent: {context_manager.get_last_intent()}")
    print(f"Location entity: {context_manager.get_entity('location')}")
    print()
    
    # Process second utterance
    utterance2 = "How about tomorrow?"
    intent2, entities2 = recognizer.detect_intent(utterance2)
    
    # This utterance might not have a clear intent, so use context
    if intent2 == "unknown_intent" and context_manager.get_last_intent() == "weather_inquiry":
        intent2 = "weather_inquiry"
        entities2["location"] = context_manager.get_entity("location", "current location")
        entities2["time"] = "tomorrow"
    
    context_manager.update_context(intent2, entities2, utterance2)
    
    print("After second utterance:")
    print(f"Last intent: {context_manager.get_last_intent()}")
    print(f"Location entity: {context_manager.get_entity('location')}")
    print(f"Time entity: {context_manager.get_entity('time')}")
    print()


if __name__ == "__main__":
    # Choose which simulation to run
    choice = input("Choose an option:\n1. Run tests\n2. Simulate conversation\n3. Simulate Vosk integration\n> ")
    
    if choice == "1":
        run_tests()
    elif choice == "2":
        simulate_conversation()
    elif choice == "3":
        simulate_vosk_integration()
    else:
        print("Invalid choice. Exiting.")
