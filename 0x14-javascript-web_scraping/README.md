Project: 0x14 JavaScript - Web Scraping

This project involves the development of JavaScript scripts for web scraping, specifically targeting various tasks that interact with APIs. The scripts are designed to perform actions such as reading and writing to files, displaying status codes, fetching Star Wars movie details, counting character occurrences, and more.

Scripts Overview:

0-readme.js

Task: Read and print the content of a file.
Usage: ./0-readme.js <file-path>
Functionality: Reads the content of the specified file in utf-8. If an error occurs, it prints the error object.

1-writeme.js

Task: Write a string to a file.
Usage: ./1-writeme.js <file-path> <string-to-write>
Functionality: Writes the provided string to the specified file in utf-8. Prints the error object in case of any writing error.

2-statuscode.js

Task: Display the status code of a GET request.
Usage: ./2-statuscode.js <URL>
Functionality: Makes a GET request to the provided URL using the request module and prints the status code.

3-starwars_title.js

Task: Print the title of a Star Wars movie based on the given movie ID.
Usage: ./3-starwars_title.js <movie-ID>
Functionality: Uses the Star Wars API to fetch and print the title of the specified movie ID.

4-starwars_count.js

Task: Print the number of movies where the character "Wedge Antilles" is present.
Usage: ./4-starwars_count.js <Star-Wars-API-URL>
Functionality: Filters movies by character ID 18 (Wedge Antilles) and prints the count.

5-request_store.js

Task: Get the contents of a webpage and store it in a file.
Usage: ./5-request_store.js <URL> <file-path>
Functionality: Makes a request to the provided URL, retrieves the body response, and stores it in the specified file.

6-completed_tasks.js

Task: Compute the number of tasks completed by each user.
Usage: ./6-completed_tasks.js <todos-API-URL>
Functionality: Fetches todo data from the provided API URL and prints a JSON object with user IDs and the number of completed tasks.

100-starwars_characters.js

Task: Print all characters of a Star Wars movie based on the given movie ID.
Usage: ./100-starwars_characters.js <movie-ID>
Functionality: Uses the Star Wars API to fetch and print all character names for the specified movie ID.

101-starwars_characters.js

Task: Print all characters of a Star Wars movie in the order specified in the API response.
Usage: ./101-starwars_characters.js <movie-ID>
Functionality: Uses the Star Wars API to fetch and print all character names in the order specified in the API response.
