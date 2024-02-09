import threading
import subprocess
import os
import nltk

def run_script(script_file):
    subprocess.run(['python', script_file], check=True)

if __name__ == '__main__':
    # Paths to the Python scripts you want to run
    hackernews_script = 'C:\\Users\\Novo\\Noticias\\scripts\\hackernews_scraper.py'
    helpnetsecurity_script = 'C:\\Users\\Novo\\Noticias\\scripts\\helpnetsecurity_scrapper.py'
    cyware_script = 'C:\\Users\\Novo\\Noticias\\scripts\\cyware_scrapper.py'

    # Create threads for each script
    thread_hackernews = threading.Thread(target=run_script, args=(hackernews_script,))
    thread_helpnetsecurity = threading.Thread(target=run_script, args=(helpnetsecurity_script,))
    thread_cyware = threading.Thread(target=run_script, args=(cyware_script,))
    print("Scrapping Hackernews...")
    print("Scrapping Helpnetsecurity...")
    print("Scrapping Cyware...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the command prompt

    
    # Suppress NLTK messages
    nltk.download('punkt', quiet=True)
    
    # Start the threads
    thread_hackernews.start()
    thread_helpnetsecurity.start()
    thread_cyware.start()
    # Wait for both threads to finish
    thread_hackernews.join()
    thread_helpnetsecurity.join()
    thread_cyware.join()

    print("Good job soldier!")
