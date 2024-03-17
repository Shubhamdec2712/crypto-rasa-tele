from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pkg_resources

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"
        
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []

class ActionUtterAskCryptocurrency(Action):
    def name(self) -> Text:
        return "utter_ask_cryptocurrency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_cryptocurrency")
        return []

class ActionUtterFirstCryptocurrency(Action):
    def name(self) -> Text:
        return "utter_first_cryptocurrency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_first_cryptocurrency")
        return []

class ActionUtterPopularCryptocurrencies(Action):
    def name(self) -> Text:
        return "utter_popular_cryptocurrencies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_popular_cryptocurrencies")
        return []

class ActionUtterDifferenceFromTraditionalMoney(Action):
    def name(self) -> Text:
        return "utter_difference_from_traditional_money"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_difference_from_traditional_money")
        return []

class ActionUtterEnsureSecurity(Action):
    def name(self) -> Text:
        return "utter_ensure_security"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ensure_security")
        return []

class ActionUtterAdvantagesOfCryptocurrency(Action):
    def name(self) -> Text:
        return "utter_advantages_of_cryptocurrency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_advantages_of_cryptocurrency")
        return []

class ActionUtterFutureOfFinance(Action):
    def name(self) -> Text:
        return "utter_future_of_finance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_future_of_finance")
        return []

class ActionUtterMiningProcess(Action):
    def name(self) -> Text:
        return "utter_mining_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_mining_process")
        return []

class ActionUtterValueDerivation(Action):
    def name(self) -> Text:
        return "utter_value_derivation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_value_derivation")
        return []

class ActionUtterAcquireCryptocurrency(Action):
    def name(self) -> Text:
        return "utter_acquire_cryptocurrency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_acquire_cryptocurrency")
        return []

class ActionUtterStablecoinsWork(Action):
    def name(self) -> Text:
        return "utter_stablecoins_work"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_stablecoins_work")
        return []

class ActionUtterCryptocurrencyUseCases(Action):
    def name(self) -> Text:
        return "utter_cryptocurrency_use_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cryptocurrency_use_cases")
        return []

class ActionUtterStoreCryptocurrency(Action):
    def name(self) -> Text:
        return "utter_store_cryptocurrency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_store_cryptocurrency")
        return []

class ActionUtterEverydayUse(Action):
    def name(self) -> Text:
        return "utter_everyday_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_everyday_use")
        return []

class ActionUtterKeyConcepts(Action):
    def name(self) -> Text:
        return "utter_key_concepts"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_key_concepts")
        return []

class ActionUtterSignificanceOfEncryption(Action):
    def name(self) -> Text:
        return "utter_significance_of_encryption"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Encryption plays a crucial role in cryptocurrency by ensuring the security of transactions and data transmission between wallets and public ledgers. It helps protect against hacking and unauthorized access.")
        return []

class ActionUtterFirstCryptocurrencyAndFounder(Action):
    def name(self) -> Text:
        return "utter_first_cryptocurrency_and_founder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Bitcoin, founded in 2009 by an individual or group using the pseudonym Satoshi Nakamoto, was the first cryptocurrency and remains the most commonly traded.")
        return []

class ActionUtterCryptocurrencyCreationProcess(Action):
    def name(self) -> Text:
        return "utter_cryptocurrency_creation_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Cryptocurrencies are created through a process called mining, which involves using computer power to solve complex mathematical problems that generate new coins. Alternatively, users can buy cryptocurrencies from brokers or exchanges.")
        return []

class ActionUtterWellKnownCryptocurrencies(Action):
    def name(self) -> Text:
        return "utter_well_known_cryptocurrencies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Besides Bitcoin, some well-known cryptocurrencies include Ethereum, Litecoin, and Ripple. Ethereum, for example, is a blockchain platform with its own cryptocurrency called Ether (ETH).")
        return []

class ActionUtterBuyingCryptocurrencySteps(Action):
    def name(self) -> Text:
        return "utter_buying_cryptocurrency_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The steps involved in buying cryptocurrency typically include choosing a platform (such as a broker or exchange), funding your account using fiat currency or other cryptocurrencies, and placing an order to buy the desired amount of cryptocurrency.")
        return []

class ActionUtterSecureCryptocurrencyStorage(Action):
    def name(self) -> Text:
        return "utter_secure_cryptocurrency_storage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Cryptocurrency can be stored securely in cryptographic wallets, which can be physical devices or online software. Wallets use encryption to protect private keys, and users can choose between hot wallets (online) and cold wallets (offline) for storage.")
        return []

class ActionUtterCryptocurrencyPurchaseExamples(Action):
    def name(self) -> Text:
        return "utter_cryptocurrency_purchase_examples"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Cryptocurrency can be used to purchase a wide variety of goods and services, including technology products, luxury items, cars, insurance premiums, and more. Some retailers and online platforms accept cryptocurrency as a form of payment.")
        return []

class ActionUtterRisksOfInvestingInCryptocurrency(Action):
    def name(self) -> Text:
        return "utter_risks_of_investing_in_cryptocurrency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Investing in cryptocurrency carries risks such as market volatility, lack of regulatory protection, potential for hacking or fraud, and uncertainty about the future value of the assets. It's essential for investors to research exchanges, diversify their investments, and be prepared for price fluctuations.")
        return []

class ActionUtterBitcoinLegalStatus(Action):
    def name(self) -> Text:
        return "utter_bitcoin_legal_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Bitcoin's legal status varies from country to country. While some countries allow its use, others have implemented regulations or outright bans.")
        return []

class ActionUtterCountriesWhereBitcoinLegal(Action):
    def name(self) -> Text:
        return "utter_countries_where_bitcoin_legal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Countries where Bitcoin is legal include the United States, Canada, the European Union, Australia, and France. These countries have regulations in place for taxation, anti-money laundering (AML), and counter-financing of terrorism (CFT).")
        return []

class ActionUtterUsBitcoinRegulation(Action):
    def name(self) -> Text:
        return "utter_us_bitcoin_regulation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("In the United States, Bitcoin is regulated by agencies like the Financial Crimes Enforcement Network (FinCEN) and the Internal Revenue Service (IRS). Bitcoin is considered property for taxation purposes, and entities involved in administering or exchanging Bitcoin must comply with money services business (MSB) regulations.")
        return []

class ActionUtterEuBitcoinStance(Action):
    def name(self) -> Text:
        return "utter_eu_bitcoin_stance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The European Union recognizes Bitcoin as a crypto-asset and has introduced legislation to regulate crypto-assets under the Markets in Cryptoassets (MiCA) Regulation. This legislation aims to provide regulatory clarity and protect consumers while preventing financial crimes.")
        return []

class ActionUtterCanadaBitcoinRegulation(Action):
    def name(self) -> Text:
        return "utter_canada_bitcoin_regulation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Canada treats Bitcoin as a commodity for taxation purposes, and cryptocurrency exchanges are considered money service businesses (MSBs) under anti-money laundering (AML) laws. They must register with the Financial Transactions and Reports Analysis Centre of Canada (FINTRAC) and comply with reporting requirements.")
        return []

class ActionUtterAustraliaBitcoinApproach(Action):
    def name(self) -> Text:
        return "utter_australia_bitcoin_approach"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("In Australia, Bitcoin is subject to capital gains tax when certain events trigger taxable events, such as trading, selling, or using Bitcoin for purchases. However, individuals holding Bitcoin strictly for personal use may not owe taxes in certain situations.")
        return []

class ActionUtterFranceBitcoinRegulation(Action):
    def name(self) -> Text:
        return "utter_france_bitcoin_regulation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("France regulates cryptocurrencies and crypto-assets under the Monetary and Financial Code (MFC). The government defines digital assets and regulates businesses involved in digital asset services, such as purchasing, selling, and providing exchange services.")
        return []

class ActionUtterBannedCountries(Action):
    def name(self) -> Text:
        return "utter_banned_countries"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Countries like Qatar, Saudi Arabia, and China have implemented absolute bans on Bitcoin and other cryptocurrencies due to concerns over volatility, illicit activities, and threats to their monetary systems.")
        return []

class ActionUtterReasonsForBanningBitcoin(Action):
    def name(self) -> Text:
        return "utter_reasons_for_banning_bitcoin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Countries may ban Bitcoin due to concerns about volatility, energy consumption, destabilization of monetary systems, and its potential use in illegal activities like money laundering and terrorism financing.")
        return []

class ActionUtterUsPotentialBitcoinIllegalization(Action):
    def name(self) -> Text:
        return "utter_us_potential_bitcoin_illegalization"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("While theoretically possible, it is unlikely that the United States would make Bitcoin illegal, as it would require legislative action and faces challenges in enforcement and practicality.")
        return []

class ActionUtterLegalConsequencesOfIllegalCryptocurrencyUse(Action):
    def name(self) -> Text:
        return "utter_legal_consequences_of_illegal_cryptocurrency_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Engaging in illegal activities using cryptocurrency can result in legal consequences, including fines, penalties, and imprisonment, depending on the severity of the offense and applicable laws.")
        return []

class ActionSpreadOfTechnologies(Action):
    def name(self) -> Text:
        return "action_spread_of_technologies"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="New technologies typically emerge in wealthier countries before spreading to less wealthy nations. This trend is influenced by historical innovation leadership and market profitability for companies introducing innovations.")
        return []

class ActionCryptocurrencyAdoption(Action):
    def name(self) -> Text:
        return "action_cryptocurrency_adoption"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Unlike many other technologies, cryptocurrency adoption does not offer advantages based on geography. Therefore, crypto adoption tends to spread more evenly around the world, regardless of a country's economic status.")
        return []

class ActionMetricsOfCryptoAdoption(Action):
    def name(self) -> Text:
        return "action_metrics_of_crypto_adoption"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Chainalysis tracks cryptocurrency adoption using metrics such as total cryptocurrency value on centralized exchanges, retail trading activity, peer-to-peer transaction volume, crypto value used in DeFi protocols, and retail activity in decentralized applications (dApps).")
        return []

class ActionWeighFindingsWithPPP(Action):
    def name(self) -> Text:
        return "action_weigh_findings_with_ppp"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Chainalysis uses PPP to better assess crypto adoption by considering the average purchasing power of citizens in each country. This helps identify countries where residents allocate a higher percentage of their net worth to cryptocurrency.")
        return []

class ActionCryptoInterestInVietnam(Action):
    def name(self) -> Text:
        return "action_crypto_interest_in_vietnam"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Vietnam's interest in cryptocurrency may be attributed to the success of play-to-earn (P2E) gaming and non-fungible tokens (NFTs), particularly exemplified by the popularity of the NFT-based P2E game 'Axie Infinity' developed by Sky Mavis.")
        return []

class ActionSurgeInDemandPhilippines(Action):
    def name(self) -> Text:
        return "action_surge_in_demand_philippines"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The Philippines has experienced a surge in demand for cryptocurrency due to the popularity of P2E games and NFTs, with estimates suggesting a significant portion of traffic on platforms like Axie Infinity originates from the country.")
        return []
    
class ActionProvideBitcoinEnergyInfo(Action):
    def name(self) -> Text:
        return "action_provide_bitcoin_energy_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Bitcoin mining consumes significant amounts of energy, with estimates suggesting an annual energy consumption comparable to medium-sized countries, leading to a large carbon footprint and electronic waste problems.")
        return []

class ActionProvideLedgerInfo(Action):
    def name(self) -> Text:
        return "action_provide_ledger_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Ledger was established in September. It encourages authors to digitally sign submitted papers, which are then timestamped into the Bitcoin blockchain, and include a personal Bitcoin address in their papers.")
        return []

class ActionProvideCryptocurrencyConcerns(Action):
    def name(self) -> Text:
        return "action_provide_cryptocurrency_concerns"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Nobel Prize winners and business executives have characterized cryptocurrencies as speculative bubbles and potential instruments for money laundering. Business magnate Bill Gates likened cryptocurrencies to the greater fool theory.")
        return []

class ActionProvideBrazilCryptocurrencyRegulation(Action):
    def name(self) -> Text:
        return "action_provide_brazil_cryptocurrency_regulation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Brazil has not enacted specific regulations for cryptocurrencies, but existing legal and regulatory structures provide guidance.")
        return []

class ActionProvideBrazilCryptoTaxTreatment(Action):
    def name(self) -> Text:
        return "action_provide_brazil_crypto_tax_treatment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Brazilian tax law does not have specific provisions for cryptocurrencies, but tax authorities require virtual currencies to be declared in income tax statements, with capital gains subject to income tax.")
        return []

class ActionProvideChinaBlockchainPolicy(Action):
    def name(self) -> Text:
        return "action_provide_china_blockchain_policy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The President of China called upon the country to embrace blockchain technology and increase investment and focus on its development. The People's Bank of China is expected to establish the first official digital currency, a government-backed digital fiat currency.")
        return []

class ActionProvideEURegulatoryDevelopments(Action):
    def name(self) -> Text:
        return "action_provide_eu_regulatory_developments"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The EU Parliament passed the Markets in Crypto Act (MiCA), establishing a unified legal framework to regulate cryptoassets within the European Union. Additionally, various EU regulatory bodies have issued policy recommendations and proposed actions regarding cryptocurrencies.")
        return []

class ActionProvideIndiaCryptocurrencyPolicy(Action):
    def name(self) -> Text:
        return "action_provide_india_cryptocurrency_policy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Arun Jaitley stated in his budget speech that the Indian government aims to discontinue the use of bitcoin and other virtual currencies for criminal activities. The Reserve Bank of India (RBI) announced a ban on the sale or purchase of cryptocurrency for entities regulated by the RBI. However, the Supreme Court of India revoked the RBI ban on cryptocurrency trade in March.")
        return []

class ActionProvideNigeriaCryptocurrencyRegulation(Action):
    def name(self) -> Text:
        return "action_provide_nigeria_cryptocurrency_regulation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("There is no definitive answer as the Central Bank of Nigeria (CBN) instructed commercial banks to desist from cryptocurrency transactions, but there was no outright ban on crypto use and activity. Cryptocurrencies are not considered legal tender according to existing laws, but there is no specific legal framework addressing them.")
        return []

class ActionProvideUSCryptocurrencyClassification(Action):
    def name(self) -> Text:
        return "action_provide_us_cryptocurrency_classification"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The US Treasury classified Bitcoin as a convertible decentralized virtual currency. The Commodity Futures Trading Commission (CFTC) classified Bitcoin as a commodity. The Internal Revenue Service (IRS) taxes Bitcoin as property, not as currency.")
        return []

class ActionProvideUSCryptocurrencyRegulation(Action):
    def name(self) -> Text:
        return "action_provide_us_cryptocurrency_regulation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Money services businesses, including cryptocurrency exchanges, are required to register with the US FinCEN as a money services business, design and enforce an anti-money laundering (AML) program, and keep appropriate records and make reports to FinCEN, including Suspicious Activity Reports (SARs) and Currency Transaction Reports (CTRs).")
        return []

class ActionFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'm sorry, I didn't understand that. Can you please rephrase?")
        return []
