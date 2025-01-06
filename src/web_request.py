import requests
from bs4 import BeautifulSoup


def get_span_labels_content(url):
  """
  Fetches an HTML page and extracts the content of all <span> tags.

  Args:
    url: The URL of the HTML page to fetch.

  Returns:
    A list containing the text content of all <span> tags on the page.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')
    span_tags = soup.find_all('span')
    span_contents = [span.get_text(strip=True) for span in span_tags]
    span_contents_concat = ' '.join(span_contents)
    return span_contents_concat

  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    return

print(get_span_labels_content("https://careers.tuigroup.com/en/digital-tech-data"))