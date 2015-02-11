import cnfg
import unittest
import mock


class TestContentsOf(unittest.TestCase):
    """
    Test the cnfg.contents_of function, mocking out codecs.open.
    (The tests are very tightly bound to the implementation.)
    """

    @mock.patch('codecs.open')
    def test_calls_codecs_open(self, mock_codecs_open):
        result = cnfg.contents_of('/a/path')
        mock_codecs_open.assert_called_once_with('/a/path', 'r', 'utf-8')

    def test_returns_file_contents(self):
        # Is there a way to achieve this without `with`, but instead
        # with a decorator as above?
        with mock.patch('codecs.open', mock.mock_open(read_data='content')):
            result = cnfg.contents_of('/a/path')
        self.assertEqual(result, 'content')


class TestLoad(unittest.TestCase):
    """
    Test the cnfg.load function, mocking out three system-related calls.
    (The tests are very tightly bound to the implementation.)
    """

    def setUp(self):
        # Can this be done with less code, perhaps with decorators?
        patch_os_path_join = mock.patch('os.path.join')
        self.addCleanup(patch_os_path_join.stop)
        self.mock_os_path_join = patch_os_path_join.start()
        self.mock_os_path_join.return_value = '~/a_file'

        patch_os_path_expanduser = mock.patch('os.path.expanduser')
        self.addCleanup(patch_os_path_expanduser.stop)
        self.mock_os_path_expanduser = patch_os_path_expanduser.start()
        self.mock_os_path_expanduser.return_value = '/home/a_user/a_file'

        patch_contents_of = mock.patch('cnfg.contents_of')
        self.addCleanup(patch_contents_of.stop)
        self.mock_contents_of = patch_contents_of.start()
        self.mock_contents_of.return_value = "{'a': 1,}"

        self.result = cnfg.load('a_file')

    def test_calls_os_path_join(self):
        self.mock_os_path_join.assert_called_once_with('~', 'a_file')

    def test_calls_os_path_expanduser(self):
        self.mock_os_path_expanduser.assert_called_once_with('~/a_file')

    def test_calls_contents_of(self):
        self.mock_contents_of.assert_called_once_with('/home/a_user/a_file')

    def test_evals_file_contents(self):
        self.assertEqual(self.result, {'a': 1,})


if __name__ == '__main__':
    unittest.main()
