import json
import mimetypes
import traceback
from datetime import timedelta

import mock
from freezegun import freeze_time
from openprocurement.api.utils import get_now
from six import text_type

from uuid import UUID
from hashlib import md5
from webtest import TestApp, TestRequest, forms
from openprocurement.api.constants import VERSION
from webtest.compat import to_bytes

from tests.base.constants import API_HOST, MOCK_DATETIME


class PrefixedRequestClass(TestRequest):
    @classmethod
    def blank(cls, path, *args, **kwargs):
        path = '/api/%s%s' % (VERSION, path)
        return TestRequest.blank(path, *args, **kwargs)


class DumpsWebTestApp(TestApp):
    RequestClass = PrefixedRequestClass

    hostname = API_HOST
    indent = 2
    ensure_ascii = False

    def do_request(self, req, status=None, expect_errors=None):
        req.headers.environ["HTTP_HOST"] = self.hostname
        self.write_request(req)
        resp = super(DumpsWebTestApp, self).do_request(req, status=status, expect_errors=expect_errors)
        self.write_response(resp)
        return resp

    def write_request(self, req):
        if hasattr(self, 'file_obj') and not self.file_obj.closed:
            self.file_obj.write(req.as_bytes(True))
            self.file_obj.write("\n")
            if req.body:
                try:
                    obj = json.loads(req.body)
                except ValueError:
                    self.file_obj.write('DATA:\n' + req.body)
                else:
                    self.file_obj.write('DATA:\n' + json.dumps(
                        obj, indent=self.indent, ensure_ascii=self.ensure_ascii
                    ).encode('utf8'))
                self.file_obj.write("\n")
            self.file_obj.write("\n")

    def write_response(self, resp):
        if hasattr(self, 'file_obj') and not self.file_obj.closed:
            headers = [
                (n.title(), v)
                for n, v in resp.headerlist
                if n.lower() != 'content-length'
            ]
            headers.sort()
            self.file_obj.write(str('Response: %s\n%s\n') % (
                resp.status,
                str('\n').join([str('%s: %s') % (n, v) for n, v in headers]),
            ))
            if resp.testbody:
                try:
                    obj = json.loads(resp.testbody)
                except ValueError:
                    pass
                else:
                    self.file_obj.write(json.dumps(
                        obj, indent=self.indent, ensure_ascii=self.ensure_ascii
                    ).encode('utf8'))
                    self.file_obj.write("\n")
            self.file_obj.write("\n")


    def encode_multipart(self, params, files):
        """
        Encodes a set of parameters (typically a name/value list) and
        a set of files (a list of (name, filename, file_body, mimetype)) into a
        typical POST body, returning the (content_type, body).

        """
        boundary = 'BOUNDARY'
        lines = []

        def _append_file(file_info):
            key, filename, value, fcontent = self._get_file_info(file_info)
            if isinstance(key, text_type):
                try:
                    key = key.encode('ascii')
                except:  # pragma: no cover
                    raise  # file name must be ascii
            if isinstance(filename, text_type):
                try:
                    filename = filename.encode('utf8')
                except:  # pragma: no cover
                    raise  # file name must be ascii or utf8
            if not fcontent:
                fcontent = mimetypes.guess_type(filename.decode('utf8'))[0]
            fcontent = to_bytes(fcontent)
            fcontent = fcontent or b'application/octet-stream'
            lines.extend([
                b'--' + boundary,
                b'Content-Disposition: form-data; ' +
                b'name="' + key + b'"; filename="' + filename + b'"',
                b'Content-Type: ' + fcontent, b'', value])

        for key, value in params:
            if isinstance(key, text_type):
                try:
                    key = key.encode('ascii')
                except:  # pragma: no cover
                    raise  # field name are always ascii
            if isinstance(value, forms.File):
                if value.value:
                    _append_file([key] + list(value.value))
            elif isinstance(value, forms.Upload):
                file_info = [key, value.filename]
                if value.content is not None:
                    file_info.append(value.content)
                    if value.content_type is not None:
                        file_info.append(value.content_type)
                _append_file(file_info)
            else:
                if isinstance(value, text_type):
                    value = value.encode('utf8')
                lines.extend([
                    b'--' + boundary,
                    b'Content-Disposition: form-data; name="' + key + b'"',
                    b'', value])

        for file_info in files:
            _append_file(file_info)

        lines.extend([b'--' + boundary + b'--', b''])
        body = b'\r\n'.join(lines)
        boundary = boundary.decode('ascii')
        content_type = 'multipart/form-data; boundary=%s' % boundary
        return content_type, body


class MockWebTestMixin(object):
    uuid_patch = None
    uuid_counters = None
    freezer = None
    tick_delta = None

    whitelist = ('/openprocurement/', '/tests/')
    blacklist = ('/tests/base/tests.py',)

    def setUpMock(self):
        self.uuid_patch = mock.patch('uuid.UUID', side_effect=self.uuid)
        self.uuid_patch.start()
        self.freezer = freeze_time(MOCK_DATETIME)
        self.freezer.start()

    def tearDownMock(self):
        self.freezer.stop()
        self.uuid_patch.stop()

    def uuid(self, version=None, **kwargs):
        stack = self.stack()
        hex = md5(str(stack)).hexdigest()
        count = self.count(hex)
        hash = md5(hex + str(count)).digest()
        return UUID(bytes=hash[:16], version=version)

    def stack(self):
        def trim_path(path):
            for whitelist_item in self.whitelist:
                pos = path.find(whitelist_item)
                if pos > -1:
                    return path[pos:]
        stack = traceback.extract_stack()
        return [(trim_path(item[0]), item[2], item[3]) for item in stack if all([
            any([path in item[0] for path in self.whitelist]),
            all([path not in item[0] for path in self.blacklist])
        ])]

    def count(self, name):
        if self.uuid_counters is None:
            self.uuid_counters = dict()
        if name not in self.uuid_counters:
            self.uuid_counters[name] = 0
        self.uuid_counters[name] += 1
        return self.uuid_counters[name]

    def tick(self, delta=timedelta(seconds=1)):
        if not self.tick_delta:
            self.tick_delta = timedelta(seconds=0)
        self.tick_delta += delta
        freeze = get_now() + self.tick_delta
        self.freezer.stop()
        self.freezer = freeze_time(freeze.isoformat())
        self.freezer.start()
