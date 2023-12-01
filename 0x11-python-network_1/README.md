0x11. Python - Network #1
This repository contains Python scripts that utilize the urllib and requests packages for network-related tasks.

Scripts
0-hbtn_status.py
Description: Fetches the status of "https://alx-intranet.hbtn.io/status" using urllib. The script uses a with statement and displays the type, content, and utf8 content of the response body.
1-hbtn_header.py
Description: Takes a URL as an argument, sends a request, and displays the value of the X-Request-Id variable found in the header of the response. The script uses urllib and sys.
2-post_email.py
Description: Takes a URL and an email as arguments, sends a POST request with the email as a parameter, and displays the body of the response. The script uses urllib and sys.
3-error_code.py
Description: Takes a URL, sends a request, and displays the body of the response. It manages urllib.error.HTTPError exceptions and prints "Error code: " followed by the HTTP status code if an error occurs.
4-hbtn_status.py
Description: Fetches the status of "https://alx-intranet.hbtn.io/status" using the requests package. The script displays the type and content of the response body.
5-hbtn_header.py
Description: Takes a URL as an argument, sends a request, and displays the value of the X-Request-Id variable in the response header. The script uses requests and sys.
6-post_email.py
Description: Takes a URL and an email as arguments, sends a POST request with the email as a parameter, and displays the body of the response. The script uses requests and sys.
7-error_code.py
Description: Takes a URL, sends a request, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints "Error code: " followed by the value of the HTTP status code. The script uses requests and sys.
8-json_api.py
Description: Takes a letter and sends a POST request to "http://0.0.0.0:5000/search_user" with the letter as a parameter. The script displays the id and name if the JSON is properly formatted and not empty. It handles cases where the JSON is invalid or empty. The script uses requests and sys.
10-my_github.py
Description: Takes GitHub credentials (username and personal access token) as arguments and uses the GitHub API to display the user's id. The script uses Basic Authentication with the personal access token.
11-pinterest.py
Description: An advanced script that takes repository and owner names as arguments and uses the GitHub API to list the 10 most recent commits. The script uses the requests package and Basic Authentication.
