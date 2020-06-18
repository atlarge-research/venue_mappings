# Venue mappings
![Venue Mapper](https://github.com/atlarge-research/venue_mappings/workflows/Venue%20Mapper/badge.svg)

Venue mappings is a library project developed by [Laurens Versluis](https://github.com/lfdversluis/) to map venue BibTex strings found in sources such as [DBLP](dblp.uni-trier.de/) and [Google Scholar](scholar.google.com/) to the acronym of the venue.

For example the strings `FGCS`, `Future Generation Comp. Syst.` and `Future Generation Computer Systems` can be found in BibTex entries and other corpuses. The venue mapper maps these strings to their corresponding acronym -  `FGCS`.
Article meta-data stored in, e.g., a database then becomes easier to query, as well as sanitizing and making uniform your BibTex entries.  

## Usage
```
from venue_mapper.venue_mapper import VenueMapper
venue_mapper = VenueMapper()
acronym = venue_mapper.get_abbreviation("FGCS")
```

## Scope
Currently, this repository contains venues from the systems community.
Naturally, we encourage additions through pull-requests.

## Project Structure
The file `venue_map.py` contains the `VenueMapper` class.
This class contains the `venues` dictionary which contains the matching rules.

There are currently five matching types: `EXACT`, `STARTS_WITH`, `ENDS_WITH`, `CONTAINS`, `REGEX`

All tests are located in the `tests` folder. Each test is named `test_<acronym of venue>.py` for clarity.
We use the `BaseRunner` class to make each test as simple as possible. We believe each test is self-explanatory.

## What's up with these five matching types?
Initially, this project used regex rules for all matches, including exact matches.
After some micro benchmarks, we found that moving to this type of matching, and caching already seen strings led to a 6-8x speedup depending on the computer.
