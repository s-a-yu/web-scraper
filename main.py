import urllib.parse

import requests
from bs4 import BeautifulSoup
import random
import time
import json
import csv
from scipy.stats import spearmanr



# scrape top 10 results from yahoo
def scrape_yahoo(query):
    edited_url = '+'.join(query.split())
    url7 = f"http://search.yahoo.com/search?p=" + edited_url
    url14 = f"http://search.yahoo.com/search?p=" + edited_url + "&b=8"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # make 2 requests to yahoo (one only shows 7 results)
    response7 = requests.get(url7, headers=headers)
    response14 = requests.get(url14, headers=headers)

    if response7.status_code != 200:
        print(f"Failed to retrieve search results for query: {query}")
        return []
    if response14.status_code != 200:
        print(f"Failed to retrieve search results for query: {query}")
        return []

    soup7 = BeautifulSoup(response7.text, "html.parser")
    soup14 = BeautifulSoup(response14.text, "html.parser")

    results = []
    for link in soup7.find_all("a", attrs={"class": "d-ib fz-20 lh-26 td-hu tc va-bot mxw-100p"}):
        href = link['href']
        if "https://r.search.yahoo.com" in href and not href.startswith("/"):
            encoded_url = href.split("RU=")[1].split("/")[0]
            decoded_url = urllib.parse.unquote(encoded_url)
            results.append(decoded_url)
            if len(results) >= 10:
                break

    if len(results) < 10:
        for link in soup14.find_all("a", attrs={"class": "d-ib fz-20 lh-26 td-hu tc va-bot mxw-100p"}):
            href = link['href']
            if "https://r.search.yahoo.com" in href and not href.startswith("/"):
                encoded_url = href.split("RU=")[1].split("/")[0]
                decoded_url = urllib.parse.unquote(encoded_url)
                results.append(decoded_url)
                if len(results) >= 10:
                    break

    return results


# run the scraper over queries
def run_scraper(queries):
    search_results = {}

    for query in queries:
        print(f"Scraping results for query: {query}")
        results = scrape_yahoo(query)
        search_results[query] = results

        # random delay
        delay = random.randint(10, 50)
        print(f"Waiting for {delay} seconds to avoid getting blocked...")
        time.sleep(delay)

    # save results to json file
    with open("search_results.json", "w") as f:
        json.dump(search_results, f, indent=4)

    print("Scraping completed and results saved to search_results.json.")


queries = [
    "Some important facts on the respiratory system",
    "You want to text dirty with your boyfriend what should you say",
    "Can you give me example of anecdotes by the filipino writers",
    "How do you figure sq ft for a house",
    "What city is the iffel tower",
    "Hw big are sperm whales up to dinosaurs",
    "What is not part of a biology",
    "What is the radio code for a 2005 renault clio sport 182 cup",
    "How many troops are in a modern marine battalion",
    "More defines for respect",
    "Why your deserts so hot",
    "Are the decomposer that live in the ocean",
    "Site where vladimir lenin is kept",
    "Codes to get weapons in poptropica",
    "How many grammys does alicia keys have now",
    "What level does pineco evovle at",
    "How many toes does an ostrich have",
    "How does an iphone compare to a blackberry",
    "How did darius reorganize and improve the persian government",
    "What are lyrics of the star spangled banner",
    "What do the uniting church believe about the bible",
    "Number of babies a polar bear can have",
    "What is 4th Earl of Sandwich",
    "What do mediaval princesses wear",
    "What did Medea give Jason to prtect him self",
    "How many miles are in africa",
    "What did queen latifah influence",
    "What is a natuaral fathers rights",
    "What is excluded from OSHA",
    "How did your universe form",
    "5 pillars of faith are like",
    "What is ryan sheckler worth",
    "Where is the river murrays source",
    "Who is the leader of azerbaijan",
    "How many calories in one hot dog with bun",
    "Where hydroelectic energy id from",
    "How many voyages did christopher columbus make",
    "What is vanessa hudgens background",
    "What languages are spoken the united kingdom",
    "How many movies did Julie Andrews play in",
    "Something in a bathroom with a J",
    "What can nuclear energy be converted to",
    "Is WWE freaking fake",
    "How do you build a bridge out of popsical sticks",
    "The language of origin of the word karate",
    "The advantagous of being a doctor",
    "What are the typical daily temperature swings on mars",
    "What is the most feared gang diablos or bloodz or crips",
    "What is amy dumas full name",
    "Where can you get a groudon in soul silver",
    "What are the properties of C45 Steel",
    "Which president pardoned Ricard Nixon",
    "Boethius wrote or music of the university",
    "How many grams is in a cup of whole wheat pasta",
    "A list of the most famous baseball players",
    "The good side of corporal punishment",
    "What country do oats grow in",
    "How much does modified dirt track car cost",
    "What is the punishment for vandalsim in texas",
    "What city does shane dawson live",
    "What will happen if you overdose on aspirin",
    "How many calories in a cup if fresh strawberries",
    "Which sport is eminem 's favorite",
    "What is the principle component of air",
    "What is th relative location of Germany",
    "How do you feel a boob without henr noticing",
    "What city dose demi lovato live in",
    "What is hte climate in denmark",
    "What is strong emotion",
    "How does basketball related to science",
    "What was the colossus of rhodes a statue of",
    "What are the effects of a plant of mineral deficiency",
    "The scientific name of the windpipe",
    "Where does the lena river go into",
    "What is the tax called on export",
    "What are the two photosynthesis",
    "Que paso con diego rivera revolucion mexicana",
    "8 ounces is how many millilitres",
    "Where is the Dell inc HQ location",
    "What is th function for nucleus",
    "Best site to download aimbot for cod4",
    "What causes the soil to be red",
    "Where is vinson massif located in the antartica",
    "America and Italy dont have in common",
    "How many decimals are in a centimeter",
    "When is lil wayne real name",
    "What deraction is irleand",
    "In what year did clovis convert to Christianity",
    "Where was the pharos located",
    "Ingrediance in 7up",
    "What are the differences between butterflies and birds",
    "What party is dalton mcguinty part of",
    "Best carb for a 305",
    "What causes an ulcer",
    "Anecdote about twix",
    "What is the significance of fecalysis",
    "What are the two symbol of elivation on a map",
    "Why was hera 's symbol a pomegraete",
    "What important event happened in 1867",
    "Who did victoria marry and wen"
]

with open('/Users/steph/PycharmProjects/572_hw1/Google_Result2.json') as google_file:
    google_results = json.load(google_file)

with open('/Users/steph/PycharmProjects/572_hw1/search_results.json') as yahoo_file:
    yahoo_results = json.load(yahoo_file)

# compare links for each query and return matching pairs
def compare_search_results(google_data, yahoo_data):
    matches = {}

    # Iterate through each query in google_results
    for query in google_data:
        if query in yahoo_data:
            google_links = google_data[query]
            yahoo_links = yahoo_data[query]
            query_matches = []

            # Compare the links and find matching pairs
            for google_index, google_link in enumerate(google_links, start=1):
                if google_link in yahoo_links:
                    yahoo_index = yahoo_links.index(google_link) + 1
                    query_matches.append((google_index, yahoo_index))

            if query_matches:
                matches[query] = query_matches  # Store as list of tuples

    return matches


# calculate Spearman's coefficient
def calculate_spearman(query_matches):
    if len(query_matches) == 1:
        # Special case when there's only one pair
        google_rank, yahoo_rank = query_matches[0]
        return 1 if google_rank == yahoo_rank else 0

    google_ranks = [match[0] for match in query_matches]
    yahoo_ranks = [match[1] for match in query_matches]

    # Check if input arrays are constant
    if len(set(google_ranks)) == 1 or len(set(yahoo_ranks)) == 1:
        return 0  # Constant input case, correlation is undefined

    # Use scipy's spearmanr to calculate the correlation
    rho, _ = spearmanr(google_ranks, yahoo_ranks)

    return rho

def generate_csv(results, csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Query No.', 'Number of Matched Pairs', 'Percent Overlap', 'Spearman Coefficient'])

        total_matched = 0
        total_percent = 0
        total_spearman = 0
        num_queries = len(results)

        for idx, (query, matches) in enumerate(results.items(), start=1):
            num_matched = len(matches)
            percent_overlap = (num_matched / 10) * 100
            spearman_coefficient = calculate_spearman(matches)

            # Write the results to CSV
            writer.writerow([f"Query {idx}", num_matched, percent_overlap, spearman_coefficient])

            # Track totals for averages
            total_matched += num_matched
            total_percent += percent_overlap
            total_spearman += spearman_coefficient

        # Write averages at the end
        avg_matched = total_matched / num_queries
        avg_percent = total_percent / num_queries
        avg_spearman = total_spearman / num_queries

        writer.writerow(['Averages', avg_matched, avg_percent, avg_spearman])

if __name__ == "__main__":
    # run_scraper(queries)

    # Compare results
    matching_results = compare_search_results(google_results, yahoo_results)

    # Generate CSV output
    generate_csv(matching_results, '/Users/steph/PycharmProjects/572_hw1/search_comparison_results.csv')

    print("CSV file generated: search_comparison_results.csv")
