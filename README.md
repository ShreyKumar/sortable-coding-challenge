# Sortable Coding Challenge

# Link to Github Repository
https://github.com/ShreyKumar/sortable-coding-challenge

# About me
I'm a 4th year Computer Science Student at the University of Toronto expected to graduate in November 2018 (likely to be shifted earlier). I have a lot of academic and industry experience in a variety of fields including full stack web development. I'm described by many people from my previous <a href="http://shreykumar.com/#testimonials">internships</a> as someone who can fit in well in a company atmosphere while staying productive.
<br><br> Be sure to visit my <a href="http://shreykumar.com/">website</a> or LinkedIn 
<a href="https://www.linkedin.com/in/shreykumar/">profile</a> for more information! 

# How to run
<code>$ python3 main.py</code>

You should get this output if everything runs smoothly:<br>
<code>$ python3 main.py</code><br>
<code>Working...</code><br>
<code>Writing to results.txt...</code><br>
<code>Done!</code>

# My Approah
I've made many attempts of using object-oriented programming to approach this problem, but realized that it would make the problem too complicated and simplified it down to this approach.<br>
The most effecient way of doing this is putting all the products inside a giant Array and using a divide and conquer algorithm to search through all the products and match it to its respective listing. I used a HashMap to map each Product's name to its listing. I found using a HashMap to be the easiest way to store the data because each product's listing can be accessed in O(1) worst case which would be a better alternative than traversing through another Array because it would be more innefficient.<br><br>

Essentially, 
1. <code>main.py</code> reads all the product information in <code>products.txt</code> and correctly parses them as Python Dictionaries, storing them in the <code>products</code> Array and creates an empty field in the <code>products_table</code> HashMap with its respective <code>product_name</code> attribute.
2. <code>main.py</code> then reads all the listing information in <code>listings.txt</code> and gets an array of <code>Product</code> from <code>find_products</code> which matches the listing.
3. For Every found product, it finds its respective entry in <code>products_table</code> and stores the listing.
4. Finally, it re-arranges all the data inside <code>products_table</code> and writes it to <code>results.txt</code> one JSON object per line.
