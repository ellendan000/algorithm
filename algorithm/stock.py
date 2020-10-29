#  总股本 = 股票面值 * 股份总额
#  发行1000万股，每股10元, 总股本1亿
def capitalization(faceValue, count): 
    return faceValue * count

#  市值 = 股价 * 总股本
def marketCapitalization(marketPrice, capitalization):
    return marketPrice * capitalization

#  市盈率(P/E) = 股价 / 每股收益（净利润）。适用于流通性好，盈利稳定的情况，周期行业不适用。
#  市盈率：为了获取1元净利润付出多少代价。或者，需要多少年才能回本。
#  静态市盈率：公司上一个年度净利润
#  滚动市盈率：最近4个季度财报的利润率
#  动态市盈率：预估下一个年度净利润
def priceEarningsRatio(marketPrice, earingPerShare):
    return marketPrice / earingPerShare

#  盈利收益率(E/P) = 每股收益（净利润） / 股价
#  市盈率的倒数。
#  盈利收益率：盈利收益率越高，代表公司的估值越低，公司越有可能被低估。
def earningPriceRatio(marketPrice, earingPerShare):
    return earingPerShare / marketPrice

#  市净率（P/B）= 股价 / 每股净资产
#  PB等于1，说明刚好以净资产价格买入股票。
def priceBookRatio(marketPrice, netbookValue):
    return marketPrice / netbookValue

#  净资产收益率（ROE）= 净利润 / 净资产
def returnOnEquity(netProfit, netbookValue):
    return netProfit / netbookValue

#  股息率 = 企业过去一年的现金分红（派息）/ 总市值， 或者 年度分红每股金额 / 股票价格。
#  
# def dividendYieldRatio()

#  分红率 = 股息 / 盈利
# def
# 
# 年复合收益率: （现有价值/基础价值）开根号 （年数） - 1
# 5年，1200 -> 2300，1200 * (1+x) 5 = 2300
# ((2300 / 1200) ** (1/5) - 1)
def compoundAnnualGrowthRate(marketPrice, originPrice, years):
    return ((marketPrice / originPrice) ** (1/years) - 1)


if __name__ == "__main__":
    print((2300 / 1200) ** (1/5) - 1)
    print( 1 / 0.064)
    print(3 ** (1/10) -1)