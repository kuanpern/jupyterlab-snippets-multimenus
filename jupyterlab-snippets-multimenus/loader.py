import os
import json
import collections

from pathlib import PurePath
from jupyter_core.paths import jupyter_path
import tornado

import logging
logger = logging.getLogger(__name__)


class SnippetsLoader:
    def __init__(self):
        self.snippet_config_paths = jupyter_path("multimenus_snippets_config")
        self.snippet_paths        = jupyter_path("multimenus_snippets")
    # end def

    def autogen_snippet_config(self, dirname):
        '''Generate snippet config file by files in source directory'''
        
        def nested_dd():
            return collections.defaultdict(nested_dd)
        # end def
        def recurse(d):
            result = []
            for key in sorted(d.keys()):
                if len(d[key]) == 0:
                    result.append(key)
                else:
                    result.append([key, recurse(d[key])])
                # end if
            # end for
            return result
        # end def

        f = []
        for (dirpath, dirnames, filenames) in os.walk(dirname):
            f.extend([dirpath+os.sep+filename for filename in filenames])
        # end for
        g = [dirname.join(filename.split(dirname)[1:]) for filename in f]

        z = nested_dd()
        for path in g:
            cols = path.split(os.sep)[1:]
            w = z[cols[0]]
            for col in cols[1:]:
                w = w[col]
            # end for
        # end for
        z = recurse(z)

        return json.loads(json.dumps(z))
    # end def

    def snippets_to_fileparts(self, snippet_config):
        def recurse(inlist):
            assert isinstance(inlist, (list, tuple)), 'input must be a list or tuple'
            results = []
            if all(isinstance(_, str) for _ in inlist):
                results = [[_] for _ in inlist]
                return results

            if len(inlist) == 2:
                if type(inlist[0]) == str:
                    return recurse([inlist])
                # end if
            # end if

            for item in inlist:
                if isinstance(item, (list, tuple)) and (len(item) == 2):
                    if isinstance(item[0], str):
                        vals = [[item[0]] + _ for _ in recurse(item[1])]
                        results.extend(vals)
                        continue
                    else:
                        raise ValueError('unparseable: %s' % str(item))
                    # end if
                if isinstance(item, str):
                    results.append([item])
                    continue
                raise ValueError('unparseable: %s' % str(item))
            return results
        # end def
        
        results = []
        for key, val in snippet_config:
            results.append([key, recurse(val)])
        # end for
        return results
    # end def

    def collect_snippets(self):

        # use snippet config if there is any
        snippet_config = []
        for root_path in self.snippet_config_paths:
            _filename = os.sep.join([root_path, 'snippet_config.json'])
            if os.path.isfile(_filename):
                with open(_filename, 'r') as fin:
                    _config = json.load(fin)
                    snippet_config.extend(_config)
                # end with
            # end if
        # end for
        if len(snippet_config) != 0:
            snippets = self.snippets_to_fileparts(snippet_config)
            return snippets
        # end if

        # fallback if snippet config not defined
        snippets = []
        for root_path in self.snippet_paths:
            snippet_config = self.autogen_snippet_config(root_path)
            _snippets = self.snippets_to_fileparts(snippet_config)
            snippets.extend(_snippets)
        # end for

        return snippets
    # end def


    def get_snippet_content(self, snippet):
        try:
            for root_path in self.snippet_paths:
                path = os.path.join(root_path, *snippet)

                # Prevent access to the entire file system when the path contains '..'
                accessible = os.path.abspath(path).startswith(root_path)
                if not accessible:
                    print(f'jupyterlab-snippets: {path} not accessible from {root_path}')

                if accessible and os.path.isfile(path):
                    with open(path) as f:
                        return f.read()
        except:
            raise tornado.web.HTTPError(status_code=500)

        print(f'jupyterlab-snippets: {snippet} not found in {self.snippet_paths}')
        raise tornado.web.HTTPError(status_code=404)
