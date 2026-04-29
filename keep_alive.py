#!/usr/bin/env python
"""
Keep Alive Server Manager - Automatically restarts the backend if it crashes
Usage: python keep_alive.py
"""

import subprocess
import time
import os
import signal
import sys
from pathlib import Path

class ServerManager:
    def __init__(self):
        self.process = None
        self.backend_dir = Path(__file__).parent / "backend"
        self.running = True
        
    def signal_handler(self, sig, frame):
        """Handle Ctrl+C gracefully"""
        print("\n✓ Stopping server manager...")
        self.stop()
        sys.exit(0)
    
    def start_server(self):
        """Start the backend server"""
        try:
            print(f"\n{'='*50}")
            print("🚀 Starting MediScan Backend Server...")
            print(f"{'='*50}\n")
            
            self.process = subprocess.Popen(
                ["python", "app.py"],
                cwd=self.backend_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Read output line by line
            for line in iter(self.process.stdout.readline, ''):
                if line:
                    print(line.rstrip())
                    
        except Exception as e:
            print(f"❌ Error starting server: {e}")
    
    def stop(self):
        """Stop the server gracefully"""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except:
                self.process.kill()
            self.running = False
    
    def run(self):
        """Main loop - restarts server if it crashes"""
        signal.signal(signal.SIGINT, self.signal_handler)
        
        while self.running:
            try:
                self.start_server()
                
                # If process ended, it crashed
                if self.process and self.process.returncode is not None:
                    print("\n⚠️  Server crashed or stopped")
                    print("🔄 Restarting in 5 seconds...\n")
                    time.sleep(5)
                    
            except KeyboardInterrupt:
                print("\n✓ Server manager stopped")
                self.running = False
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                print("🔄 Restarting in 5 seconds...\n")
                time.sleep(5)

if __name__ == "__main__":
    manager = ServerManager()
    manager.run()
