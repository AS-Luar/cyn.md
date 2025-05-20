#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Integrated Voice Assistant Solution

This module provides a complete integration of the speech recognition and understanding 
components developed in previous modules. It demonstrates a modular, threaded architecture
for processing audio input, recognizing speech, and responding to user intents.
"""

import threading
import queue
import pyaudio
import time
import numpy as np
import os
import json
import re
import random
from vosk import Model, KaldiRecognizer


class ThreadedAudioProcessor:
    """Audio processing component that runs in a background thread."""
    
    def __init__(self, sample_rate=16000, frames_per_buffer=8000, channels=1):
        """Initialize the audio processor.
        
        Args:
            sample_rate: Audio sample rate in Hz
            frames_per_buffer: Number of frames per buffer
            channels: Number of audio channels (1 for mono, 2 for stereo)
        """
        # Audio parameters
        self.sample_rate = sample_rate
        self.frames_per_buffer = frames_per_buffer
        self.channels = channels
        
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        
        # Create audio frames queue
        self.audio_queue = queue.Queue()
        
        # Thread control
        self.is_running = False
        self.thread = None
        
    def start_processing(self):
        """Start the audio processing in a background thread"""
        if self.is_running:
            print("Audio processor is already running")
            return
            
        self.is_running = True
        self.thread = threading.Thread(target=self.process_audio_thread)
        self.thread.daemon = True
        self.thread.start()
        print("Audio processing started")
        
    def process_audio_thread(self):
        """Main audio processing loop that runs in a background thread"""
        try:
            # Open audio stream
            stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=self.channels,
                rate=self.sample_rate,
                input=True,
                frames_per_buffer=self.frames_per_buffer
            )
            
            print("Audio stream opened")
            
            # Process audio while running
            while self.is_running:
                try:
                    # Read audio frame
                    data = stream.read(self.frames_per_buffer, exception_on_overflow=False)
                    
                    # Optional: apply preprocessing here (noise reduction, normalization, etc.)
                    
                    # Add frame to queue
                    self.audio_queue.put(data)
                except Exception as e:
                    print(f"Error capturing audio: {e}")
                    time.sleep(0.1)  # Prevent tight loop if errors occur
            
            # Clean up
            stream.stop_stream()
            stream.close()
            print("Audio stream closed")
            
        except Exception as e:
            print(f"Error in audio processing thread: {e}")
            self.is_running = False
    
    def stop_processing(self):
        """Stop the audio processing thread"""
        if not self.is_running:
            print("Audio processor is not running")
            return
            
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=2.0)  # Wait for thread to finish
        
        # Clear the queue
        while not self.audio_queue.empty():
            try:
                self.audio_queue.get_nowait()
            except queue.Empty:
                break
                
        print("Audio processing stopped")
    
    def get_audio_queue(self):
        """Get the queue containing audio frames"""
        return self.audio_queue
    
    def get_sample_rate(self):
        """Get the audio sample rate"""
        return self.sample_rate
    
    def cleanup(self):
        """Clean up resources"""
        self.stop_processing()
        self.audio.terminate()


class ThreadedRecognition:
    """Speech recognition component using Vosk that runs in a background thread."""
    
    def __init__(self, audio_queue, model_path):
        """Initialize the speech recognizer.
        
        Args:
            audio_queue: Queue containing audio frames
            model_path: Path to the Vosk model directory
        """
        # Audio queue
        self.audio_queue = audio_queue
        
        # Model path
        self.model_path = model_path
        
        # Output queue for recognized text
        self.text_queue = queue.Queue()
        
        # Thread control
        self.is_running = False
        self.thread = None
        
        # Recognition state
        self.model = None
        self.recognizer = None
        self.last_partial = ""
    
    def initialize(self, sample_rate=16000):
        """Initialize the Vosk model and recognizer.
        
        Args:
            sample_rate: Sample rate of the audio
        """
        print(f"Loading speech recognition model from {self.model_path}...")
        
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model path not found: {self.model_path}")
        
        self.model = Model(self.model_path)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)
        
        print("Speech recognition model loaded")
    
    def start_recognition(self, sample_rate=16000):
        """Start the recognition process in a background thread.
        
        Args:
            sample_rate: Sample rate of the audio
        """
        if self.is_running:
            print("Recognition is already running")
            return
        
        # Initialize model if needed
        if not self.model or not self.recognizer:
            self.initialize(sample_rate)
        
        self.is_running = True
        self.thread = threading.Thread(target=self.recognition_thread)
        self.thread.daemon = True
        self.thread.start()
        print("Speech recognition started")
    
    def recognition_thread(self):
        """Main recognition loop that runs in a background thread"""
        try:
            while self.is_running:
                try:
                    # Get audio data from queue with timeout
                    audio_data = self.audio_queue.get(timeout=0.5)
                    
                    # Process with Vosk
                    if self.recognizer.AcceptWaveform(audio_data):
                        # Final result
                        result = json.loads(self.recognizer.Result())
                        text = result.get("text", "").strip()
                        
                        if text:  # Only if we have text
                            print(f"Recognized: {text}")
                            self.text_queue.put({"type": "final", "text": text})
                            self.last_partial = ""
                    else:
                        # Partial result
                        result = json.loads(self.recognizer.PartialResult())
                        partial = result.get("partial", "").strip()
                        
                        if partial and partial != self.last_partial:
                            print(f"Partial: {partial}", end="\r")
                            self.last_partial = partial
                            self.text_queue.put({"type": "partial", "text": partial})
                    
                    # Mark as done
                    self.audio_queue.task_done()
                    
                except queue.Empty:
                    # No audio data available, continue
                    pass
                    
                except Exception as e:
                    print(f"Error in recognition: {e}")
                    time.sleep(0.1)
            
        except Exception as e:
            print(f"Error in recognition thread: {e}")
            self.is_running = False
    
    def stop_recognition(self):
        """Stop the recognition thread"""
        if not self.is_running:
            print("Recognition is not running")
            return
        
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=2.0)
        
        print("Speech recognition stopped")
    
    def get_text_queue(self):
        """Get the queue containing recognized text"""
        return self.text_queue


class ThreadedUnderstanding:
    """Natural language understanding component that runs in a background thread."""
    
    def __init__(self, text_queue):
        """Initialize the understanding component.
        
        Args:
            text_queue: Queue containing recognized text
        """
        # Text queue
        self.text_queue = text_queue
        
        # Output queue for intents and entities
        self.intent_queue = queue.Queue()
        
        # Thread control
        self.is_running = False
        self.thread = None
        
        # Intent patterns
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
        
        # Context storage
        self.context = {
            "last_intent": None,
            "entities": {},
            "conversation_history": [],
            "session_start_time": time.time()
        }
    
    def start_understanding(self):
        """Start the understanding process in a background thread"""
        if self.is_running:
            print("Understanding is already running")
            return
        
        self.is_running = True
        self.thread = threading.Thread(target=self.understanding_thread)
        self.thread.daemon = True
        self.thread.start()
        print("Speech understanding started")
    
    def understanding_thread(self):
        """Main understanding loop that runs in a background thread"""
        try:
            while self.is_running:
                try:
                    # Get text from queue with timeout
                    text_data = self.text_queue.get(timeout=0.5)
                    
                    # We only process final results
                    if text_data["type"] == "final":
                        text = text_data["text"]
                        
                        # Process text to get intent and entities
                        intent, entities = self.detect_intent(text)
                        
                        # Apply context to handle follow-ups
                        intent, entities = self.apply_context(intent, entities, text)
                        
                        # Update context
                        self.update_context(intent, entities, text)
                        
                        # Add to intent queue
                        self.intent_queue.put({
                            "intent": intent,
                            "entities": entities,
                            "text": text
                        })
                        
                        print(f"Intent: {intent}, Entities: {entities}")
                    
                    # Mark as done
                    self.text_queue.task_done()
                    
                except queue.Empty:
                    # No text available
                    pass
                
                except Exception as e:
                    print(f"Error in understanding: {e}")
                    time.sleep(0.1)
            
        except Exception as e:
            print(f"Error in understanding thread: {e}")
            self.is_running = False
    
    def detect_intent(self, text):
        """Detect the intent from the text.
        
        Args:
            text: Text to process
            
        Returns:
            Tuple of (intent, entities)
        """
        # Convert to lowercase
        text = text.lower()
        
        # Check each intent pattern
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    # Extract entities
                    entities = {}
                    for group_name in match.groupdict():
                        entities[group_name] = match.group(group_name)
                    
                    # Additional entity processing
                    if intent == "weather_inquiry" and "location" not in entities:
                        location_match = re.search(r"in (?P<location>[\w\s]+)$", text)
                        if location_match:
                            entities["location"] = location_match.group("location").strip()
                    
                    return intent, entities
        
        # No match found
        return "unknown", {}
    
    def apply_context(self, intent, entities, text):
        """Apply conversation context to handle ambiguous queries.
        
        Args:
            intent: Detected intent
            entities: Detected entities
            text: Original text
            
        Returns:
            Possibly updated (intent, entities) tuple
        """
        # If unknown intent, try to use context
        if intent == "unknown":
            last_intent = self.context["last_intent"]
            
            # Handle follow-up questions
            if last_intent == "weather_inquiry":
                if any(word in text.lower() for word in ["tomorrow", "later", "weekend"]):
                    # Follow-up about weather
                    intent = "weather_inquiry"
                    entities["location"] = self.context["entities"].get("location", "current location")
                    
                    # Extract time reference
                    if "tomorrow" in text.lower():
                        entities["time"] = "tomorrow"
                    elif "weekend" in text.lower():
                        entities["time"] = "this weekend"
                    else:
                        entities["time"] = "later"
        
        return intent, entities
    
    def update_context(self, intent, entities, text):
        """Update the conversation context.
        
        Args:
            intent: Detected intent
            entities: Detected entities
            text: Original text
        """
        # Update last intent
        self.context["last_intent"] = intent
        
        # Update entities (keeping existing ones)
        for key, value in entities.items():
            self.context["entities"][key] = value
        
        # Add to history
        self.context["conversation_history"].append({
            "text": text,
            "intent": intent,
            "entities": entities.copy(),
            "timestamp": time.time()
        })
        
        # Limit history size
        if len(self.context["conversation_history"]) > 10:
            self.context["conversation_history"] = self.context["conversation_history"][-10:]
    
    def stop_understanding(self):
        """Stop the understanding thread"""
        if not self.is_running:
            print("Understanding is not running")
            return
        
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=2.0)
        
        print("Speech understanding stopped")
    
    def get_intent_queue(self):
        """Get the queue containing detected intents"""
        return self.intent_queue


class ResponseManager:
    """Generates responses based on intents and entities."""
    
    def __init__(self):
        """Initialize response templates."""
        self.response_templates = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Greetings! How may I assist you?"
            ],
            "farewell": [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye for now!"
            ],
            "weather_inquiry": [
                "The weather in {location} is {condition} with a temperature of {temp}°F.",
                "In {location}, it's {condition} and {temp}°F.",
                "The forecast for {location} shows {condition} conditions and {temp}°F."
            ],
            "time_inquiry": [
                "The current time is {time}.",
                "It's {time} right now.",
                "The time is {time}."
            ],
            "date_inquiry": [
                "Today is {date}.",
                "The date is {date}.",
                "It's {date} today."
            ],
            "device_control": [
                "I've turned {action} the {device}.",
                "The {device} is now {action}.",
                "{device} turned {action}."
            ],
            "timer_set": [
                "I've set a timer for {duration}.",
                "Timer set for {duration}.",
                "Your timer is set and will go off in {duration}."
            ],
            "unknown": [
                "I'm not sure I understand. Can you rephrase that?",
                "I don't know how to help with that yet.",
                "I didn't quite catch that. What would you like me to do?"
            ]
        }
    
    def generate_response(self, intent, entities):
        """Generate a response based on intent and entities.
        
        Args:
            intent: Detected intent
            entities: Detected entities
            
        Returns:
            Response text
        """
        # Use unknown intent if we don't have templates
        if intent not in self.response_templates:
            intent = "unknown"
        
        # Get random template
        templates = self.response_templates[intent]
        template = random.choice(templates)
        
        # Add mock data for specific intents
        if intent == "weather_inquiry":
            entities["location"] = entities.get("location", "current location")
            entities["time"] = entities.get("time", "today")
            entities["condition"] = random.choice(["sunny", "cloudy", "rainy", "overcast", "clear"])
            entities["temp"] = random.randint(65, 85)
        
        elif intent == "time_inquiry":
            entities["time"] = time.strftime("%I:%M %p")
        
        elif intent == "date_inquiry":
            entities["date"] = time.strftime("%A, %B %d, %Y")
        
        elif intent == "timer_set":
            duration = entities.get("duration", "a short time")
            entities["duration"] = duration
        
        # Format the template with entities
        try:
            return template.format(**entities)
        except KeyError:
            # Fall back if missing required entities
            return "I need more information to help with that."


class ActionExecutor:
    """Executes actions based on intents and entities."""
    
    def execute_action(self, intent, entities):
        """Execute actions based on intent.
        
        Args:
            intent: Detected intent
            entities: Detected entities
            
        Returns:
            True if action executed, False otherwise
        """
        # Handle device control
        if intent == "device_control":
            device = entities.get("device", "unknown device")
            action = entities.get("action", "unknown action")
            print(f"[Action] Controlling device: {device} -> {action}")
            return True
        
        # Handle weather inquiry
        elif intent == "weather_inquiry":
            location = entities.get("location", "current location")
            time = entities.get("time", "today")
            print(f"[Action] Getting weather for {location} {time}")
            return True
        
        # Handle timer
        elif intent == "timer_set":
            duration = entities.get("duration", "unknown duration")
            print(f"[Action] Setting timer for {duration}")
            return True
        
        # No action for other intents
        return False


class VoiceAssistant:
    """Main voice assistant class that integrates all components."""
    
    def __init__(self, model_path):
        """Initialize the voice assistant.
        
        Args:
            model_path: Path to the Vosk model directory
        """
        # Store model path
        self.model_path = model_path
        
        # Create components
        self.audio_processor = ThreadedAudioProcessor()
        self.recognizer = ThreadedRecognition(self.audio_processor.get_audio_queue(), model_path)
        self.understanding = ThreadedUnderstanding(self.recognizer.get_text_queue())
        self.response_manager = ResponseManager()
        self.action_executor = ActionExecutor()
        
        # Thread control
        self.is_running = False
        self.response_thread = None
    
    def start(self):
        """Start the voice assistant."""
        if self.is_running:
            print("Voice assistant is already running")
            return
        
        print("Starting voice assistant...")
        
        # Start audio processing
        self.audio_processor.start_processing()
        
        # Start speech recognition
        self.recognizer.start_recognition(self.audio_processor.get_sample_rate())
        
        # Start understanding
        self.understanding.start_understanding()
        
        # Start response thread
        self.is_running = True
        self.response_thread = threading.Thread(target=self.response_thread)
        self.response_thread.daemon = True
        self.response_thread.start()
        
        print("Voice assistant started and listening")
    
    def response_thread(self):
        """Thread that generates responses and executes actions."""
        try:
            intent_queue = self.understanding.get_intent_queue()
            
            while self.is_running:
                try:
                    # Get intent data with timeout
                    intent_data = intent_queue.get(timeout=0.5)
                    
                    # Extract intent and entities
                    intent = intent_data["intent"]
                    entities = intent_data["entities"]
                    
                    # Execute action
                    self.action_executor.execute_action(intent, entities)
                    
                    # Generate and output response
                    response = self.response_manager.generate_response(intent, entities)
                    print(f"\nAssistant: {response}")
                    
                    # Mark as done
                    intent_queue.task_done()
                    
                except queue.Empty:
                    # No intent data available
                    pass
                
                except Exception as e:
                    print(f"Error in response thread: {e}")
                    time.sleep(0.1)
            
        except Exception as e:
            print(f"Error in response thread: {e}")
            self.is_running = False
    
    def stop(self):
        """Stop the voice assistant."""
        if not self.is_running:
            print("Voice assistant is not running")
            return
        
        print("Stopping voice assistant...")
        self.is_running = False
        
        # Stop components in reverse order
        self.understanding.stop_understanding()
        self.recognizer.stop_recognition()
        self.audio_processor.stop_processing()
        
        # Wait for response thread
        if self.response_thread:
            self.response_thread.join(timeout=2.0)
        
        print("Voice assistant stopped")


def main():
    """Main function to run the integrated voice assistant."""
    # Set the path to your Vosk model
    model_path = "/home/luar/AI/voice_assistant/vosk-model-small-en-us-0.15"
    
    # Check if model exists
    if not os.path.exists(model_path):
        print(f"Error: Model directory not found at {model_path}")
        print("Please download a model from https://alphacephei.com/vosk/models")
        return
    
    # Create and start the voice assistant
    assistant = VoiceAssistant(model_path)
    
    try:
        # Start the assistant
        assistant.start()
        
        print("\nVoice Assistant is running. You can speak now.")
        print("Press Ctrl+C to exit.")
        
        # Keep the main thread alive
        while True:
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nStopping voice assistant (keyboard interrupt)...")
    
    finally:
        # Stop the assistant
        assistant.stop()


if __name__ == "__main__":
    main()
