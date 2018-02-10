# The Grinder 3.11
# HTTP script recorded by TCPProxy at Feb 18, 2013 10:41:50 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

def createRequest(test, url, headers=None):
    """Create an instrumented HTTPRequest."""
    request = HTTPRequest(url=url)
    if headers: request.headers=headers
    test.record(request, HTTPRequest.getHttpMethodFilter())
    return request

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('Accept-Language', 'en-US,en;q=0.5'),
    NVPair('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0'),
    NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers0= \
  [ NVPair('Referer', 'http://216.121.120.116:8080/Chapter09-PerformanceJoined-war/faces/WineStoreJoined.jsp'), ]

url0 = 'http://216.121.120.116:8080'

request101 = createRequest(Test(101, 'GET WineStoreJoined.jsp'), url0)

request201 = createRequest(Test(201, 'POST WineStoreJoined.jsp'), url0, headers0)

request301 = createRequest(Test(301, 'POST WineStoreJoined.jsp'), url0, headers0)

request401 = createRequest(Test(401, 'POST WineStoreJoined.jsp'), url0, headers0)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET WineStoreJoined.jsp (request 101)."""
    result = request101.GET('/Chapter09-PerformanceJoined-war/faces/WineStoreJoined.jsp')
    self.token_j_id_id17 = \
      httpUtilities.valueFromHiddenInput('j_id_id17') # 'j_id_id17'
    self.token_javaxfacesViewState = \
      httpUtilities.valueFromHiddenInput('javax.faces.ViewState') # '-1131220347937159250:-474775219501021154...'

    return result

  def page2(self):
    """POST WineStoreJoined.jsp (request 201)."""
    result = request201.POST('/Chapter09-PerformanceJoined-war/faces/WineStoreJoined.jsp',
      ( NVPair('j_id_id17', self.token_j_id_id17),
        NVPair('j_id_id17:selectOneListbox1', '2653'),
        NVPair('j_id_id17:j_id_id40', '5'),
        NVPair('j_id_id17:j_id_id46', 'Add to Cart'),
        NVPair('javax.faces.ViewState', self.token_javaxfacesViewState), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_javaxfacesViewState = \
      httpUtilities.valueFromHiddenInput('javax.faces.ViewState') # '-1131220347937159250:-280954872357262463...'

    return result

  def page3(self):
    """POST WineStoreJoined.jsp (request 301)."""
    result = request301.POST('/Chapter09-PerformanceJoined-war/faces/WineStoreJoined.jsp',
      ( NVPair('j_id_id17', self.token_j_id_id17),
        NVPair('j_id_id17:selectOneListbox1', '2658'),
        NVPair('j_id_id17:j_id_id40', '2'),
        NVPair('j_id_id17:j_id_id46', 'Add to Cart'),
        NVPair('javax.faces.ViewState', self.token_javaxfacesViewState), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_javaxfacesViewState = \
      httpUtilities.valueFromHiddenInput('javax.faces.ViewState') # '-1131220347937159250:4029743844510937935'

    return result

  def page4(self):
    """POST WineStoreJoined.jsp (request 401)."""
    result = request401.POST('/Chapter09-PerformanceJoined-war/faces/WineStoreJoined.jsp',
      ( NVPair('j_id_id17', self.token_j_id_id17),
        NVPair('j_id_id17:selectOneListbox1', '2658'),
        NVPair('j_id_id17:j_id_id40', '2'),
        NVPair('j_id_id17:j_id_id51', 'Submit Order'),
        NVPair('javax.faces.ViewState', self.token_javaxfacesViewState), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_j_id_id15 = \
      httpUtilities.valueFromHiddenInput('j_id_id15') # 'j_id_id15'
    self.token_javaxfacesViewState = \
      httpUtilities.valueFromHiddenInput('javax.faces.ViewState') # '-1131220347937159250:854799551406467588'

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET WineStoreJoined.jsp (request 101)

    grinder.sleep(0)
    self.page2()      # POST WineStoreJoined.jsp (request 201)

    grinder.sleep(0)
    self.page3()      # POST WineStoreJoined.jsp (request 301)

    grinder.sleep(0)
    self.page4()      # POST WineStoreJoined.jsp (request 401)


# Instrument page methods.
#Test(100, 'Page 1').record(TestRunner.page1)
#Test(200, 'Page 2').record(TestRunner.page2)
#Test(300, 'Page 3').record(TestRunner.page3)
#Test(400, 'Page 4').record(TestRunner.page4)
