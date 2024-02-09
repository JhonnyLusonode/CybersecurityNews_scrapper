import threading
import subprocess

def run_script(script_file):
    subprocess.run(['python', script_file], check=True)

if __name__ == '__main__':
    # Paths to the Python scripts you want to run
    hackernews_script = 'C:\\Users\\Novo\\Noticias\\scripts\\hackernews_scraper.py'
    helpnetsecurity_script = 'C:\\Users\\Novo\\Noticias\\scripts\\helpnetsecurity_scrapper.py'

    # Create threads for each script
    thread_hackernews = threading.Thread(target=run_script, args=(hackernews_script,))
    thread_helpnetsecurity = threading.Thread(target=run_script, args=(helpnetsecurity_script,))
    print("Scrapping Hackernews...")
    print("Scrapping Helpnetsecurity...")
    # Start the threads
    thread_hackernews.start()
    thread_helpnetsecurity.start()
    # Wait for both threads to finish
    thread_hackernews.join()
    thread_helpnetsecurity.join()

    print("Both scripts have finished execution.")
