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

## Version structure
Currently, the version is in the form of `x.y.z`.
- If any update is not backwards compatible and users need to modify code to make the upgrade work, `x` will be upped. `y` and `z` will be reset, e.g., `1.2.3` -> `2.0.0`
- If one or more new venues are added, `y` will be upped. `x` will not change and `z` will be reset, e.g., `1.2.3` -> `1.3.0`.
- If an update only applies fixes because some BibTex strings were missed, `z` will be upped. `x` and `y` will not change, e.g., `1.2.3` -> `1.2.4`.

Please note that any of `x`, `y`, and `z` can go beyond 9, i.e., `1.10.1610` is a perfectly fine version.

## Project Structure
The file `venue_mapper.py` contains the `VenueMapper` class.
This class contains the `venues` dictionary which contains the matching rules.

There are currently five matching types: `EXACT`, `STARTS_WITH`, `ENDS_WITH`, `CONTAINS`, `REGEX`

All tests are located in the `tests` folder. Each test is named `test_<acronym of venue>.py` for clarity.
We use the `BaseRunner` class to make each test as simple as possible. We believe each test is self-explanatory.

## What's up with these five matching types?
Initially, this project used regex rules for all matches, including exact matches.
After some micro benchmarks, we found that moving to this type of matching, and caching already seen strings led to a 6-8x speedup depending on the computer.
