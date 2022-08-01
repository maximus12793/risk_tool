
### Interesting libraries
* https://github.com/ssantoshp/Empyrial
* Zipline + Backtester
* Finmarketpy
* Pyfolio
* statsmodels
* Pynance
* Quandl
* Scipy
* Quantdsl
* pyFin
* vollib
* quantpy
* ffn
* tia
* pynance
* TA-lib
* algobroker
* qfrm
* ARCH
* dynts


enigma catalyst -> crypto?
https://www.lean.io/ ?
https://jesse.trade/ ?

https://financetrain.com/best-python-librariespackages-finance-financial-data-scientists
Keeps asking for ssh key password

### Extensions

-> text extraction from TDA or any arbitrary CSV tool.


### Authentication and Current Analysis
-> get visuals of current holdings either via
* https://github.com/timkpaine/tdameritrade/blob/main/general.ipynb
* https://developer.tdameritrade.com/content/authentication-faq
* https://tda-api.readthedocs.io/en/latest/client.html#account-info -> seems pretty ideal (https://github.com/alexgolec/tda-api)

NOTE: We must enforce ZERO TRADES restriction on the application.


### V0
* Collection positions in portfolio
* Produce weighting -> sector, % portfolio, etc.
* Use ML to produce an optimal weighting -> rebalance
* Tax tools?


https://github.com/timkpaine/tdameritrade/blob/main/general.ipynb


# Portfolio tools
https://github.com/tansey/pycfr
https://www.youtube.com/watch?v=7m4bnmSkjow
https://github.com/hudson-and-thames/mlfinlab
https://pyportfolioopt.readthedocs.io/en/latest/
https://github.com/dcajasn/Riskfolio-Lib


# General Items
https://github.com/EliteQuant/EliteQuant

Hudson & Thames https://hudsonthames.org/consulting/


The efficient frontier proposed by Markowitz in which we try to maximize the return with a certain risk, i.e. it focuses on containing the assigned risk.
On the other hand, there is Kelly's method proposed by John Kelly and Ed Thorpe that tries to maximise the expectation of the log utility of wealth, i.e. maximizing return is the focus.

https://blog.quantinsti.com/portfolio-management-strategy-python/


https://github.com/michaelchu/optopsy
https://www.nsrplatform.com/app/#!/
https://github.com/AsyncAlgoTrading/aat


# Rules
* We must define a maximum loss UPFRONT (before trade is placed)
* We cannot be overweight any single sector (concentration and correlation bad)
* Determine if options are too risky? (or have enough signal in data)