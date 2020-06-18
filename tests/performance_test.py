import orjson
import ast
import datetime
import time
from venue_mapper.venue_mapper import VenueMapper


class PerformanceTest(object):

    def iterload_file_lines(self, file):
        for line in file.readlines():
            try:
                json_object = orjson.loads(line)
                yield json_object
            except Exception as e:
                try:
                    json_object = ast.literal_eval(line)
                    yield json_object
                except Exception as e2:
                    print("Could not parse line. Errors: {0} and: {1}".format(e, e2))
                    continue

    def test(self):
        venue_mapper = VenueMapper()
        start = time.time()
        import yappi
        yappi.set_clock_type("cpu")
        yappi.start()
        with open("test-files/s2-corpus-057", "r", encoding="ISO-8859-1") as json_file:
            # The json files contain stacked json objects, which is bad practice. It should be wrapped in a JSON array.
            # Libraries will throw errors if you attempt to load the file, so now we lazy load each object.
            publication_iterator = self.iterload_file_lines(json_file)
            for publication in publication_iterator:
                if publication is None:  # Corrupt JSON line possibly. Skip it.
                    continue

                if "venue" not in publication:  # While parsing we sometimes get KeyError: 'venue'...
                    continue

                # Try to match the publication to a venue we are interested in.
                # Wrap in str() as it sometimes is an int (???)
                venue_string = str(publication['venue'])
                if len(venue_string) == 0:
                    continue
                venue = venue_mapper.get_abbreviation(venue_string)
        yappi.stop()
        yappi.get_func_stats().save("venue_map_trace_{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                    type='callgrind')
        print(time.time() - start)


if __name__ == '__main__':
    performance_test = PerformanceTest()
    performance_test.test()
    # Old: 444.something
    # New: 99.76612067222595
