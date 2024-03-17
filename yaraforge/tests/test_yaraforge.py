import unittest
from unittest.mock import patch, MagicMock
from yaraforge.plugin import YaraForgePlugin


class TestYaraForgePlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = YaraForgePlugin()

    @patch('yaraforge.plugin.initialize_logger')
    @patch('yaraforge.plugin.get_global_logger')
    def test_init(self, mock_logger, mock_init_logger):
        mock_logger.return_value = MagicMock()
        self.plugin.init()
        mock_init_logger.assert_called_once()
        mock_logger.assert_called_once()

    @patch('yaraforge.plugin.get_global_logger')
    def test_term(self, mock_logger):
        mock_logger.return_value = MagicMock()
        self.plugin.term()
        mock_logger.assert_called_once()

    @patch('yaraforge.plugin.get_global_logger')
    @patch('yaraforge.plugin.binascii.hexlify')
    @patch('yaraforge.plugin.idautils.GetInputFileMD5')
    @patch('yaraforge.plugin.explore_netnodes')
    @patch('yaraforge.plugin.make_dirs')
    @patch('yaraforge.plugin.DumpMaker')
    @patch('yaraforge.plugin.InstructionMaker')
    @patch('yaraforge.plugin.YaraMaker')
    @patch('yaraforge.plugin.DumpAsker')
    def test_run(self, mock_asker, mock_yara, mock_inst, mock_dump, mock_dirs, mock_netnodes, mock_md5, mock_hex,
                 mock_logger):
        mock_logger.return_value = MagicMock()
        mock_hex.return_value = MagicMock()
        mock_md5.return_value = MagicMock()
        mock_netnodes.return_value = MagicMock()
        mock_dirs.return_value = MagicMock()
        mock_dump.return_value = MagicMock()
        mock_inst.return_value = MagicMock()
        mock_yara.return_value = MagicMock()
        mock_asker.return_value = MagicMock()
        self.plugin.run(0)
        mock_logger.assert_called_once()
        mock_hex.assert_called_once()
        mock_md5.assert_called_once()
        mock_netnodes.assert_called_once()
        mock_dirs.assert_called_once()
        mock_dump.assert_called_once()
        mock_inst.assert_called_once()
        mock_yara.assert_called_once()
        mock_asker.assert_called_once()


if __name__ == '__main__':
    unittest.main()
