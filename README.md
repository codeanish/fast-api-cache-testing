# fast-api-cache-testing
Testing out using Redis to cache API data from a database

The goal here is to try using a cache in between the api and a slower service to understand the performance implications.

I used an external API whose results I would cache for faster response times. 

I was able to test out my API performance using curl and a timer as follows

`curl http://localhost:8000/zipcode/90210 -s -o /dev/null -w  "%{time_starttransfer}\n"`

Repeating the above command a couple of times would ensure that the data has made it into the cache and then returns much faster. This is a pretty big performance improvement where we're running into long running services. In my benchmarks, it was ~ 15x faster once it had been cached in redis vs outside of the cache. 