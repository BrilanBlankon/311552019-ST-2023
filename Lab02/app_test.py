import unittest
from unittest.mock import Mock,patch
import app

class ApplicationTest(unittest.TestCase):
    
    @patch('app.Application.get_names')
    def setUp(self,mock_get_names):
        mock_get_names.return_value = (["William", "Oliver", "Henry", "Liam"], ["William", "Oliver", "Henry"])
        self.app = app.Application()
    
    @patch('app.MailSystem.write')
    @patch('app.MailSystem.send')
    def test_app(self, mock_send, mock_write):

        self.assertEqual(next_persion := self.app.select_next_person(), "Liam")
        print(f"{next_persion} selected")

        def fake_mail(name):
            return f"Congrats, {name}!"
        def send(name, context):
            print(context)
        mock_write.side_effect = fake_mail
        mock_send.side_effect = send
        self.app.notify_selected()
        self.assertEqual(mock_write.call_count, 4)
        self.assertEqual(mock_send.call_count, 4)
        print('\n')
        print(mock_write.call_args_list)     
        print(mock_send.call_args_list)   

if __name__ == "__main__":
    unittest.main()