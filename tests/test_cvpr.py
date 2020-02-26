from tests.BaseRunner import BaseRunner


class TestCVPR(BaseRunner):

    def setUp(self):
        self.expected_venue = "CVPR"

        self.correct_strings = {
            "CVPR",
            "CVPR (1)",
            "CVPR (2)",
            "{IEEE} Computer Society Conference on Computer Vision and Pattern Recognition, {CVPR} 1988, 5-9 June, 1988, Ann Arbor, Michigan, {USA.}",
            "2018 {IEEE} Conference on Computer Vision and Pattern Recognition, {CVPR} 2018, Salt Lake City, UT, USA, June 18-22, 2018",
            "Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
        }

        self.wrong_strings = {
            "{IEEE} Conference on Computer Vision and Pattern Recognition Workshops, {CVPR} Workshops 2004, Washington, DC, USA, June 27 - July 2, 2004",
            "CVPR Workshop on Disguised Faces in the Wild",
        }
