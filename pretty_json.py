import requests

def main():
    word = "baby"
    url = f"https://api.datamuse.com/words?rel_jjb={word}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails

        data = response.json()

        # Extract adjectives (up to 15 for readability)
        adjectives = [item["word"] for item in data[:15]]  

        if adjectives:
            print(f'Adjectives for the word "{word}": {", ".join(adjectives)}')
        else:
            print(f'No adjectives found for "{word}".')

    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == '__main__':
    main()
