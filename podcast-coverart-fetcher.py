from pyPodcastParser.Podcast import Podcast
import requests
import urllib
import sys, getopt

def main(argv):
	url = ""
	try:
		opts, args = getopt.getopt(argv,"hu:",["url="])
	except getopt.GetoptError:
		print 'podcast-coverart-fetcher.py -u <rss_feed_url>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'podcast-coverart-fetcher.py -u <rss_feed_url>'
			sys.exit()
		elif opt in ("-u", "--url"):
			url = arg
	
	if url != "":
		# fetching and parsing the feed
		print url
		print 'fetching podcast feed...'
		response = requests.get(url)
		print 'parsing podcast feed...'
		podcast = Podcast(response.content)

		# downloading the coverart
		coverart_url = podcast.itune_image
		print coverart_url
		print 'downloading coverart image...'
		coverart = urllib.URLopener()
		filename = coverart_url.rsplit('/', 1)[-1]
		coverart.retrieve(coverart_url, filename)
		print 'coverart downloaded successfully: ' + filename
	else:
		print 'please provide a podcast rss feed URL.'
		print 'podcast-coverart-fetcher.py -u <rss_feed_url>'

if __name__ == "__main__":
	main(sys.argv[1:])