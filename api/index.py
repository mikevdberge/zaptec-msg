from http.server import BaseHTTPRequestHandler
import logging
from .misc import mc_nbfx_decoder, to_under
logger = logging.getLogger(__name__)


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        #        self.wfile.write('Hello, world!'.encode('utf-8'))
        data = b'@\x06string\x083http://schemas.microsoft.com/2003/10/Serialization/\x98\xa5{"DeviceId":"ZAP000000","DeviceType":4,"ChargerId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","StateId":523,"Timestamp":"2023-07-28T09:07:19.23","ValueAsString":"0.000"}\x01'
        data = b'@\x06string\x083http://schemas.microsoft.com/2003/10/Serialization/\x9a\x87\x01{"DeviceId":"ZAP000000","DeviceType":4,"ChargerId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","StateId":554,"Timestamp":"2023-08-03T00:00:00.0617Z","ValueAsString":"OCMF|{\\"FV\\":\\"1.0\\",\\"GI\\":\\"ZAPTEC GO\\",\\"GS\\":\\"ZAP000000\\",\\"GV\\":\\"2.1.0.4\\",\\"PG\\":\\"F1\\",\\"RD\\":[{\\"TM\\":\\"2023-08-03T00:00:00,000+00:00 R\\",\\"RV\\":179.715,\\"RI\\":\\"1-0:1.8.0\\",\\"RU\\":\\"kWh\\",\\"RT\\":\\"AC\\",\\"ST\\":\\"G\\"}]}"}\x01'

        out = mc_nbfx_decoder(data)
        logger.info('Started' + out)
        #self.wfile.write(out.encode('utf-8'))
        self.wfile.write(out)

        return