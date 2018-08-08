import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-inf", dest="infile", required=True, help="""The file to process""")
	args = parser.parse_args()
