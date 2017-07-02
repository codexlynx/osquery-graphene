#osquery.io wrapper
import fabric.api as fabric
import pprint
import json

OSQUERY_PATH = 'docker run kolide/osquery osqueryi' #Using docker for dev reasons

class Instance(object):

    def local(self, cmd):
        out = fabric.local(cmd, capture=True)
        return out

class OSQuery(Instance):

    def run(self, query):
        cmd = '%s --json "%s;"' % (OSQUERY_PATH, query)
        out = self.local(cmd)
        data = json.loads(out)
        return data
