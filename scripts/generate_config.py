import os
import argparse
import json
import collections

def autogen_snippet_config(dirname):
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


def snippets_to_fileparts(snippet_config):
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

def main(root_path):	
	return autogen_snippet_config(root_path)
# end def

def cli():
	parser = argparse.ArgumentParser(description='Generate jupyter-multimenu snippet config file')
	parser.add_argument('--path', help="Path to the root directory of the scripts", type=str, required=False, default='.')
	pars = vars(parser.parse_args())

	snippets = main(pars['path'])
	print(json.dumps(snippets, indent=2))
# end def


if __name__ == '__main__':
	cli()
# end if



