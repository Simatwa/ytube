import unittest
from os import remove
from ytube_api import Ytube, Auto
import ytube_api.models as models


class TestYtube(unittest.TestCase):

    def setUp(self):
        self.query = "happy birthday"
        self.ytube = Ytube()

    def test_queries_suggestion(self):
        self.assertIsInstance(self.ytube.suggest_queries(self.query), list)

    def test_search_video_by_title(self):
        s = self.ytube.search_video_by_title(self.query)
        self.assertIsInstance(s, models.SearchResults)

    def test_get_thumbail(self):
        item = self.ytube.search_video_by_title(self.query).items[0]

        self.assertIsInstance(self.ytube.get_thumbnail(item), bytes)

    def test_default_download_link(self):
        item = self.ytube.search_video_by_title(self.query).items[0]

        self.assertIsInstance(self.ytube.get_download_link(item), models.DownloadLink)

    def test_mp3_download_link(self):
        item = self.ytube.search_video_by_title(self.query).items[0]

        self.assertIsInstance(
            self.ytube.get_download_link(
                item,
                type="mp3",
            ),
            models.DownloadLink,
        )

    def test_mp4_download_link(self):
        item = self.ytube.search_video_by_title(self.query).items[0]

        self.assertIsInstance(
            self.ytube.get_download_link(
                item,
                type="mp4",
            ),
            models.DownloadLink,
        )

    def test_mp3_download(self):
        item = self.ytube.search_video_by_title(self.query).items[0]

        download_link = self.ytube.get_download_link(item, type="mp3", quality="128")
        saved_to = self.ytube.download(download_link, progress_bar=False)
        self.assertTrue(saved_to.exists() and saved_to.is_file())
        remove(saved_to)

    def test_mp4_download(self):
        item = self.ytube.search_video_by_title(self.query).items[0]

        download_link = self.ytube.get_download_link(item, type="mp4", quality="144")
        saved_to = self.ytube.download(download_link, progress_bar=False)
        self.assertTrue(saved_to.exists() and saved_to.is_file())
        remove(saved_to)

    def test_auto(self):
        saved_to = Auto(self.query)
        self.assertTrue(saved_to.exists() and saved_to.is_file())
        remove(saved_to)


if __name__ == "__main__":
    unittest.main()