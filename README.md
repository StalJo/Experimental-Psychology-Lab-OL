# PubMed Author Analyzer

This Python script provides a convenient way to search for scientific articles on PubMed based on a specific search term, extract author details from those articles, and then save this information into a CSV file. The script gathers data such as the author's name, their publication count, and their affiliations.

## Features

- **Search PubMed Articles**: Find articles using a specific search term.
- **Extract Author Details**: Collect names, publication counts, and affiliations of authors.
- **Save to CSV**: Outputs the collected data into a CSV file for easy analysis and sharing.

## Dependencies

- **Biopython**: Used for interacting with the PubMed database.
- **Python 3.x**: The script is written for Python 3.x.

To install Biopython, run the following command:

```bash
pip install biopython
```

## Setup

1. **Clone the Repository**: First, clone this repository to your local machine using `git clone`, or simply download the script.

2. **Set Up Biopython**: Make sure you have Biopython installed, as mentioned in the Dependencies section.

3. **Enter Your Email**: Open the script and locate the line `Entrez.email = "ENTER YOUR EMAIL"`. Replace `"ENTER YOUR EMAIL"` with your actual email address. This is required for using NCBI's E-utilities.

## Usage

1. **Set Search Term and Filename**: Open the script in a text editor. Find the lines at the end of the script:

```python
search_term = 'ENTER SEARCH TERM'
filename = 'ENTER FILENAME'
```

Replace `'ENTER SEARCH TERM'` with your desired search term for PubMed, and `'ENTER FILENAME'` with the desired output filename (without extension).

2. **Run the Script**: Save the script and run it in your terminal or command prompt:

```bash
python pubmed_author_analyzer.py
```

3. **Check Output**: Once the script completes its execution, it will save the authors' details into a CSV file named as per your input. The file will be located in the same directory as the script.

## Example

Let's say you want to search for articles related to "COVID-19 vaccines" and save the author details to "covid_vaccine_authors.csv":

```python
search_term = 'COVID-19 vaccines'
filename = 'covid_vaccine_authors'
```

## License

This script is released under the MIT License. See the LICENSE file for more details.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.
