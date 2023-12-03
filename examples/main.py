from earnings import *

# Earnings
e = Earnings("NVDA")
e.getQuotes()
e.getCompanyInfo()
e.getExpectedPriceAction()
e.getNextEarningsDate()

# Calendar
c = Calendar()
c.getEarningsByDay(datetime.date(year=2023, month=11, day=9))
c.getConfirmedUpcomingEarningsBySector(sector=Sector.XLC)

# Ticker
t = Ticker("MSFT")

# Portfolio
p = Portfolio()
p.importTickers("../portfolios/1.pff")
