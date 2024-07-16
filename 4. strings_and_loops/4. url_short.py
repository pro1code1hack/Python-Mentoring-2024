# Objective:: Develop a simple URL shortener. 
# The program will take a URL and provide a shortened version using slicing and concatenation.

# Input: Enter a URL: www.example.com
# Output: Shortened URL: www.exa...com


full_url = input ("Enter a URL: ")
start = full_url[:7]
end = full_url[-4:]
short_url = (f"{start}...{end}")
print(short_url)
