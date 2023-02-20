import webbrowser
import time

# Open the text file containing the URLs
with open('urls.txt', 'r') as f:
    urls = f.readlines()

    # Open up to 30 tabs in groups of 5
    for i in range(0, len(urls), 5):
        if i >= 25:
            break

        # Process the next group of up to 5 URLs
        urls_to_open = urls[i:i+5]
        for url in urls_to_open:
            # Strip any whitespace from the beginning or end of the URL
            url = url.strip()

            # Try to open the URL in a web browser
            try:
                webbrowser.open(url)
            except Exception as e:
                print("Error opening URL:", url)
                print("Exception:", e)
                continue

        # Wait for the tabs to finish loading
        time.sleep(5)
