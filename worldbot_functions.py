


import random
import string
import nltk

#Dictionary of countries-capitals found in Asia as Key-Value pairs
countries_asia={"Here is a list of countries in Asia:\n\nAfghanistan":"Kabul",
                " Armenia":"Yerevan", " Azerbaijan":"Baku", " Bahrain":"Manama", " Bangladesh":"Dhaka", " Bhutan":"Thimphu",
                " Brunei":"Bandar Seri Begawan", " Cambodia":"Phnom Penh"," China":"Beijing", " Cyprus": "Nicosia",
                " India":"New Delhi"," Indonesia":"Jakarta", " Iran":"Tehran", " Iraq":"Baghdad",
                " Israel":"Jerusalem"," Japan":"Tokyo",
                " Jordan":"Amman"," Kazakhstan":"Nur-Sultan", " Kuwait":"Kuwait City", " Kyrgyzstan":"Bishkek", 
                " Laos":"Vientiane", " Lebanon":"Beirut"," Malaysia":"Kuala Lumpur", 
                " Maldives":"Male"," Mongolia":"Ulaanbaatar", " Myanmar (formerly Burma)":"Naypyidaw",
                " Nepal":"Kathmandu", " North Korea":"Pyongyang", " Oman":"Muscat", " Pakistan":"Islamabad", 
                " Palestine":"Jerusalem", " Philippines":"Manila", " Qatar":"Doha",
                " Russia":"Moscow", " Saudi Arabia":"Riyadh", " Singapore":"Singapore", " South Korea":"Seoul",
                " Sri Lanka":"Sri Jayawardenepura Kotte", " Syria":"Damascus",
                " Taiwan":"Taipei", " Tajikistan":"Dushanbe", " Thailand":"Bangkok"," Timor-Leste":"Dili",
                " Turkey":"Ankara", " Turkmenistan":"Ashgabat", " United Arab Emirates (UAE)":"Abu Dhabi",
                " Uzbekistan":"Tashkent"," Vietnam":"Hanoi"," Yemen":"Sana'a",
                "\n\nType a country to learn its capital (remember to use capital letter)":""
               } 

#Dictionary of countries-capitals found in Europe as Key-Value pairs
countries_europe={"Here is a list of countries in Europe:\n\nAlbania":"Tirana"," Andorra":"Andorra la Vella",
                     " Austria":"Vienna", " Azerbaijan":"Baku", " Belarus":"Minsk"," Belgium":"Brussels", 
                     " Bosnia and Herzegovina":"Sarajevo"," Bulgaria":"Sofia", " Croatia":"Zagreb", " Cyprus":"Nicosia",
                     " Czechia":"Prague", " Denmark":"Copenhagen", " Estonia":"Tallinn",
                     " Finland":"Helsinki", " France":"Paris"," Georgia":"Tbilisi"," Germany":"Berlin",
                     " Greece":"Athens"," Hungary":"Budapest", " Iceland":"Reykjavik", " Ireland":"Dublin",
                     " Italy":"Rome", " Kazakhstan":"Nur-Sultan", " Kosovo":"Pristina", " Latvia":"Riga",
                     " Liechtenstein":"Vaduz", " Lithuania":"Vilnius", " Luxembourg":"Luxembourg",
                     " Malta":"Valletta", " Moldova":"Chisinau",
                     " Monaco":"Monaco", " Montenegro":"Podgorica", " Netherlands":"Amsterdam",
                     " North Macedonia (formerly Macedonia)":"Skopje",
                     " Norway":"Oslo", " Poland":"Warsaw", " Portugal":"Lisbon", " Romania":"Bucharest",
                     " Russia":"Moscow", " San Marino":"San Marino", " Serbia":"Belgrade", " Slovakia":"Bratislava",
                     " Slovenia":"Ljubljana", " Spain":"Madrid", " Sweden":"Stockholm", " Switzerland":"Bern",
                     " Turkey":"Ankara", " Ukraine":"Kyiv", " United Kingdom (UK)":"London", 
                     " Vatican City (Holy See)":"Vatican City",
                  "\n\nType a country to learn its capital (remember to use capital letter)":""
                 }




#Dictionary of countries-capitals found in Africa as Key-Value pairs
countries_africa={"Here is a list of countries in Africa:\n\nAlgeria":"Algiers",
                     " Angola":"Luanda", " Benin":"Porto-Novo", " Botswana":"Gaborone", " Burkina Faso":"Ouagadougou",
                     " Burundi":"Gitega",
                     " Cabo Verde":"Praia", " Cameroon":"Yaounde", " Central African Republic (CAR)":"Bangui",
                     " Chad":"N'Djamena"," Comoros":"Moroni", " Democratic Republic of the Congo":"Kinshasa",
                     " Republic of the Congo":"Brazzaville", " Cote d'Ivoire":"Yamoussoukro",
                     " Djibouti":"Djibouti (city)", " Egypt":"Cairo", " Equatorial Guinea":"Malabo (de jure)",
                     " Eritrea":"Asmara",
                     " Eswatini (formerly Swaziland)":"Mbabane (administrative) Lobamba (legislative, royal)",
                     " Ethiopia":"Addis Ababa",
                     " Gabon":"Libreville", " Gambia":"Banjul", " Ghana":"Accra", " Guinea":"Conakry",
                     " Guinea-Bissau":"Bissau", " Kenya":"Nairobi", " Lesotho":"Maseru",
                     " Liberia":"Monrovia", " Libya":"Tripoli", " Madagascar":"Antananarivo", " Malawi":"Lilongwe",
                     " Mali":"Bamako", " Mauritania":"Nouakchott",
                     " Mauritius":"Port Louis", " Morocco":"Rabat",
                     " Mozambique":"Maputo", " Namibia":"Windhoek", " Niger":"Niamey", " Nigeria":"Abuja",
                     " Rwanda":"Kigali", " Sao Tome and Principe":"São Tomé",
                     " Senegal":"Dakar", " Seychelles":"Victoria", " Sierra Leone":"Freetown",
                     " Somalia":"Mogadishu", " South Africa":"Pretoria (administrative), Cape Town (legislative)",
                     " South Sudan":"Juba", " Sudan":"Khartoum", " Tanzania":"Dodoma", " Togo":"Lomé",
                     " Tunisia":"Tunis", " Uganda":"Kampala", " Zambia":"Lusaka"," Zimbabwe":"Harare",
                     "\n\nType a country to learn its capital (remember to use capital letter)":""
                    }



#Dictionary of countries-capitals found in North America as Key-Value pairs
countries_north_america={"Here is a list of countries in North America:\n\nAntigua and Barbuda":"Saint John's", 
                            " Bahamas":"Nassau", " Barbados":"Bridgetown", " Belize":"Belmopan", " Canada":"Ottawa",
                         " Costa Rica":"San Jose", " Cuba":"Havana", " Dominica":"Roseau",
                         " Dominican Republic":"Santo Domingo", " El Salvador":"San Salvador",
                         " Grenada":"Saint George's", " Guatemala":"Guatemala City", " Haiti":"Port-au-Prince",
                         " Honduras":"Tegucigalpa", " Jamaica":"Kingston"," Mexico":"Mexico City",
                         " Nicaragua":"Managua", " Panama":"Panama City"," Saint Kitts and Nevis":"Basseterre",
                         " Saint Lucia":"Castries", " Saint Vincent and the Grenadines":"Kingstown",
                         " Trinidad and Tobago":"Port of Spain", " United States of America (USA)":"Washington, D.C",
                         "\n\nType a country to learn its capital (remember to use capital letter)":""
                        }
#Dictionary of countries-capitals found in Oceania as Key-Value pairs
countries_oceania= {"Here is a list of countries in Oceania:\n\nAustralia":"Canberra"," Fiji": "Suva", " Kiribati":"Tarawa",
                       " Marshall Islands": "Majuro", " Micronesia": "Palikir", " Nauru":"Yaren District",
                       " New Zealand":"Wellington", " Palau": "Ngerulmud", " Papua New Guinea":"Port Moresby",
                       " Samoa": "Apia", " Solomon Islands": "Honiara"," Tonga":"Nuku'alofa", 
                       " Tuvalu":"Funafuti", " Vanuatu":"Port Vila",
                    "\n\nType a country to learn its capital (remember to use capital letter)":""
                   }
                 
#Dictionary of countries-capitals found in South America as Key-Value pairs
countries_south_america={ "Here is a list of countries in South America:\n\nArgentina":"Buenos Aires",
                         "Bolivia":"Sucre","Brazil":"Brasilia", "Chile":"Santiago",
                         "Colombia":"Bogotá", "Ecuador":"Quito", "Guyana":"Georgetown", "Paraguay":"Asunción",
                         "Peru":"Lima", "Suriname":"Paramaribo", "Uruguay":"Montevideo","Venezuela":"Caracas",
                         "\n\nType a country to learn its capital (remember to use capital letter)":""
                        }
#message to appear after each capital is output
continue_message="\n\nType 'quit' to end WorldBot or type another continent/country to explore"

#Most of these functions were following the principle from A3 chatbot, but with some alterations of my own. 

def start():
    """message bot sends as starting function"""
    
    print("Welcome to the World Bot!")
    print("Type a continent you want to explore: Asia, Africa, Europe," 
          " North America, South America, Oceania")
    

def get_input():
    """ask user for an input message"""
    
    msg = input("")
    out_msg = False
    
    return msg, out_msg


def end_chat(input_list):
    """identify if user says 'quit' in input and end chat"""
    
    if "quit" in input_list:
        output = "Bye"
        chat = False
    else:
        output = None
        chat = True
        
    return output, chat


def return_country(out_msg,input_string):
    """generic responses for the chatbot to return the list
    of the countries found in the specific continent"""
        
    #searched how to input dictionary without brackets
    if not out_msg and "Asia" in input_string:
        out_msg= ",".join(countries_asia.keys()) 
        
    elif not out_msg and "Africa" in input_string:
        out_msg= ",".join(countries_africa.keys())
        
    elif not out_msg and "Europe" in input_string:
        out_msg= ",".join(countries_europe.keys())
        
    elif not out_msg and "North America" in input_string:
        out_msg= ",".join(countries_north_america.keys())
        
    elif not out_msg and "South America" in input_string:
        out_msg= ",".join(countries_south_america.keys())
        
    elif not out_msg and "Oceania" in input_string:
        out_msg= ",".join(countries_oceania.keys())
    
    return out_msg


#I had a very hard time trying to get the input message from the user, to output just the value from the dictionaries without having to do a bunch of elifs. I was unable to work my way through this. (Switch doesn't work for python)

def capitals_south_america(out_msg,input_string):
    """" generic response for the chatbot to return capitals of
    countries in South America"""  
    
    if not out_msg and "Argentina" in input_string:
        out_msg=countries_south_america["Here is a list of countries in South America:\n\nArgentina"]+ continue_message   
        
    elif not out_msg and "Bolivia" in input_string:
        out_msg=countries_south_america["Bolivia"]+ continue_message   
        
    elif not out_msg and "Brazil" in input_string:
        out_msg=countries_south_america["Brazil"]+ continue_message  
        
    elif not out_msg and "Chile" in input_string:
        out_msg=countries_south_america["Chile"]+ continue_message  
        
    elif not out_msg and "Colombia" in input_string:
        out_msg=countries_south_america["Colombia"] + continue_message
        
    elif not out_msg and "Ecuador" in input_string:
        out_msg=countries_south_america["Ecuador"]+ continue_message  
        
    elif not out_msg and "Guyana" in input_string:
        out_msg=countries_south_america["Guyana"] + continue_message  
        
    elif not out_msg and "Paraguay" in input_string:
        out_msg=countries_south_america["Paraguay"] + continue_message 
        
    elif not out_msg and "Peru" in input_string:
        out_msg=countries_south_america["Peru"]+ continue_message  
        
    elif not out_msg and "Suriname" in input_string:
        out_msg=countries_south_america["Suriname"] + continue_message
        
    elif not out_msg and "Uruguay" in input_string:
        out_msg=countries_south_america["Uruguay"]+ continue_message  
        
    elif not out_msg and "Venezuela" in input_string:
        out_msg=countries_south_america["Venezuela"]+ continue_message
        
    return out_msg
                                        
def capitals_oceania(out_msg,input_string):
    """" generic response for the chatbot to return capitals of
    countries in Oceania"""  
    
    if not out_msg and "Australia" in input_string:
        out_msg=countries_oceania["Here is a list of countries in Oceania:\n\nAustralia"]+ continue_message  
        
    elif not out_msg and "Fiji" in input_string:
        out_msg=countries_oceania[" Fiji"]+ continue_message
        
    elif not out_msg and "Kiribati" in input_string:
        out_msg=countries_oceania[" Kiribati"]+ continue_message  
        
    elif not out_msg and "Marshall Islands" in input_string:
        out_msg=countries_oceania[" Marshall Islands"]+ continue_message 
        
    elif not out_msg and "Micronesia" in input_string:
        out_msg=countries_oceania[" Micronesia"] + continue_message  
        
    elif not out_msg and "Nauru" in input_string:
        out_msg=countries_oceania[" Nauru"]+ continue_message 
        
    elif not out_msg and "New Zealand" in input_string:
        out_msg=countries_oceania[" New Zealand"] + continue_message 
        
    elif not out_msg and "Palau" in input_string:
        out_msg=countries_oceania[" Palau"] + continue_message 
        
    elif not out_msg and "Papua New Guinea" in input_string:
        out_msg=countries_oceania[" Papua New Guinea"]+ continue_message  
        
    elif not out_msg and "Samoa" in input_string:
        out_msg=countries_oceania[" Samoa"] + continue_message   
        
    elif not out_msg and "Solomon Islands" in input_string:
        out_msg=countries_oceania[" Solomon Islands"]+ continue_message
        
    elif not out_msg and "Tonga" in input_string:
        out_msg=countries_oceania[" Tonga"]+ continue_message 
        
    elif not out_msg and "Tuvalu" in input_string:
        out_msg=countries_oceania[" Tuvalu"]+ continue_message  
        
    elif not out_msg and "Vanuatu" in input_string:
        out_msg=countries_oceania[" Vanuatu"]+ continue_message
        
    return out_msg

def capitals_europe(out_msg, input_string):
    """" generic response for the chatbot to return capitals of
    countries in Europe"""
    
    if not out_msg and "Albania" in input_string:
        out_msg=countries_europe["Here is a list of countries in Europe:\n\nAlbania"] + continue_message
        
    elif not out_msg and "Andorra" in input_string:
        out_msg=countries_europe[" Andorra"] + continue_message
        
    elif not out_msg and "Armenia" in input_string:
        out_msg=countries_europe[" Armenia"] + continue_message
        
    elif not out_msg and "Austria" in input_string:
        out_msg=countries_europe[" Austria"] + continue_message
        
    elif not out_msg and "Azerbaijan" in input_string:
        out_msg=countries_europe[" Azerbaijan"] + continue_message 
        
    elif not out_msg and "Belarus" in input_string:
        out_msg=countries_europe[" Belarus"] + continue_message
        
    elif not out_msg and "Belgium" in input_string:
        out_msg=countries_europe[" Belgium"] + continue_message
        
    elif not out_msg and "Bosnia and Herzegovina" in input_string:
        out_msg=countries_europe[" Bosnia and Herzegovina"] + continue_message
        
    elif not out_msg and "Andorra" in input_string:
        out_msg=countries_europe[" Andorra"] + continue_message
        
    elif not out_msg and "Bulgaria" in input_string:
        out_msg=countries_europe[" Bulgaria"] + continue_message
        
    elif not out_msg and "Croatia" in input_string:
        out_msg=countries_europe[" Croatia"] + continue_message
        
    elif not out_msg and "Cyprus" in input_string:
        out_msg=countries_europe[" Cyprus"] + continue_message
        
    elif not out_msg and "Czechia" in input_string:
        out_msg=countries_europe[" Czechia"] + continue_message
        
    elif not out_msg and "Denmark" in input_string:
        out_msg=countries_europe[" Denmark"] + continue_message
        
    elif not out_msg and "Estonia" in input_string:
        out_msg=countries_europe[" Estonia"] + continue_message
        
    elif not out_msg and "Finland" in input_string:
        out_msg=countries_europe[" Finland"] + continue_message
        
    elif not out_msg and "France" in input_string:
        out_msg=countries_europe[" France"] + continue_message
        
    elif not out_msg and "Georgia" in input_string:
        out_msg=countries_europe[" Georgia"] + continue_message
        
    elif not out_msg and "Germany" in input_string:
        out_msg=countries_europe[" Germany"] + continue_message
        
    elif not out_msg and "Greece" in input_string:
        out_msg=countries_europe[" Greece"] + continue_message
        
    elif not out_msg and "Hungary" in input_string:
        out_msg=countries_europe[" Hungary"] + continue_message
        
    elif not out_msg and "Iceland" in input_string:
        out_msg=countries_europe[" Iceland"] + continue_message
        
    elif not out_msg and "Ireland" in input_string:
        out_msg=countries_europe[" Ireland"] + continue_message
        
    elif not out_msg and "Italy" in input_string:
        out_msg=countries_europe[" Italy"] + continue_message
        
    elif not out_msg and "Kazakhstan" in input_string:
        out_msg=countries_europe[" Kazakhstan"] + continue_message
        
    elif not out_msg and "Kosovo" in input_string:
        out_msg=countries_europe[" Kosovo"] + continue_message
        
    elif not out_msg and "Latvia" in input_string:
        out_msg=countries_europe[" Latvia"] + continue_message 
        
    elif not out_msg and "Liechtenstein" in input_string:
        out_msg=countries_europe[" Liechtenstein"] + continue_message 
        
    elif not out_msg and "Lithuania" in input_string:
        out_msg=countries_europe[" Lithuania"] + continue_message
        
    elif not out_msg and "Luxembourg" in input_string:
        out_msg=countries_europe[" Luxembourg"] + continue_message 
        
    elif not out_msg and "Malta" in input_string:
        out_msg=countries_europe[" Malta"] + continue_message
        
    elif not out_msg and "Malta" in input_string:
        out_msg=countries_europe[" Malta"] + continue_message 
        
    elif not out_msg and "Malta" in input_string:
        out_msg=countries_europe[" Malta"] + continue_message 
        
    elif not out_msg and "Moldova" in input_string:
        out_msg=countries_europe[" Moldova"] + continue_message 
        
    elif not out_msg and "Moldova" in input_string:
        out_msg=countries_europe[" Moldova"] + continue_message 
        
    elif not out_msg and "Montenegro" in input_string:
        out_msg=countries_europe[" Montenegro"] + continue_message
        
    elif not out_msg and "Netherlands" in input_string:
        out_msg=countries_europe[" Netherlands"] + continue_message  
        
    elif not out_msg and "North Macedonia (formerly Macedonia)" in input_string:
        out_msg=countries_europe[" North Macedonia (formerly Macedonia)"] + continue_message   
        
    elif not out_msg and "Norway" in input_string:
        out_msg=countries_europe[" Norway"] + continue_message 
        
    elif not out_msg and "Poland" in input_string:
        out_msg=countries_europe[" Poland"] + continue_message  
        
    elif not out_msg and "Portugal" in input_string:
        out_msg=countries_europe[" Portugal"] + continue_message 
        
    elif not out_msg and "Romania" in input_string:
        out_msg=countries_europe[" Romania"] + continue_message   
        
    elif not out_msg and "Russia" in input_string:
        out_msg=countries_europe[" Russia"] + continue_message    
        
    elif not out_msg and "San Marino" in input_string:
        out_msg=countries_europe[" San Marino"] + continue_message 
        
    elif not out_msg and "Slovakia" in input_string:
        out_msg=countries_europe[" Slovakia"] + continue_message 
        
    elif not out_msg and "Slovenia" in input_string:
        out_msg=countries_europe[" Slovenia"] + continue_message 
        
    elif not out_msg and "Spain" in input_string:
        out_msg=countries_europe[" Spain"] + continue_message    
        
    elif not out_msg and "Sweden" in input_string:
        out_msg=countries_europe[" Sweden"] + continue_message   
        
    elif not out_msg and "Switzerland" in input_string:
        out_msg=countries_europe[" Switzerland"] + continue_message 
        
    elif not out_msg and "Turkey" in input_string:
        out_msg=countries_europe[" Turkey"] + continue_message   
        
    elif not out_msg and "Ukraine" in input_string:
        out_msg=countries_europe[" Ukraine"] + continue_message  
        
    elif not out_msg and "Vatican City (Holy See)" in input_string:
        out_msg=countries_europe[" Vatican City (Holy See)"] + continue_message 
        
    elif not out_msg and "United Kingdom" in input_string:
        out_msg=countries_europe[" United Kingdom (UK)"] + continue_message 

    return out_msg

def capitals_asia(out_msg, input_string):
    """" generic response for the chatbot to return capitals of
    countries in Asia"""
    
    if not out_msg and "Albania" in input_string:
        out_msg=countries_asia["Here is a list of countries in Europe:\n\nAlbania"] + continue_message
        
    elif not out_msg and "Armenia" in input_string:
        out_msg=countries_asia[" Armenia"] + continue_message
    
    elif not out_msg and "Azerbaijan" in input_string:
        out_msg=countries_asia[" Azerbaijan"] + continue_message
    
    elif not out_msg and "Bahrain" in input_string:
        out_msg=countries_asia[" Bahrain"] + continue_message
    
    elif not out_msg and "Bangladesh" in input_string:
        out_msg=countries_asia[" Bangladesh"] + continue_message 
    
    elif not out_msg and "Bhutan" in input_string:
        out_msg=countries_asia[" Bhutan"] + continue_message
    
    elif not out_msg and "Cambodia" in input_string:
        out_msg=countries_asia[" Cambodia"] + continue_message
    
    elif not out_msg and "China" in input_string:
        out_msg=countries_asia[" China"] + continue_message
    
    elif not out_msg and "Cyprus" in input_string:
        out_msg=countries_asia[" Cyprus"] + continue_message
    
    elif not out_msg and "Bulgaria" in input_string:
        out_msg=countries_asia[" Bulgaria"] + continue_message
    
    elif not out_msg and "Cyprus" in input_string:
        out_msg=countries_asia[" Cyprus"] + continue_message
    
    elif not out_msg and "India" in input_string:
        out_msg=countries_asia[" India"] + continue_message
    
    elif not out_msg and "Iran" in input_string:
        out_msg=countries_asia[" Iran"] + continue_message
    
    elif not out_msg and "Iraq" in input_string:
        out_msg=countries_asia[" Iraq"] + continue_message
    
    elif not out_msg and "Israel" in input_string:
        out_msg=countries_asia[" Israel"] + continue_message
    
    elif not out_msg and "Japan" in input_string:
        out_msg=countries_asia[" Japan"] + continue_message
    
    elif not out_msg and "Jordan" in input_string:
        out_msg=countries_asia[" Jordan"] + continue_message
    
    elif not out_msg and "Kazakhstan" in input_string:
        out_msg=countries_asia[" Kazakhstan"] + continue_message
    
    elif not out_msg and "Kuwait" in input_string:
        out_msg=countries_asia[" Kuwait"] + continue_message
    
    elif not out_msg and "Kyrgyzstan" in input_string:
        out_msg=countries_asia[" Kyrgyzstan"] + continue_message
    
    elif not out_msg and "Laos" in input_string:
        out_msg=countries_asia[" Laos"] + continue_message
    
    elif not out_msg and "Lebanon" in input_string:
        out_msg=countries_asia[" Lebanon"] + continue_message
    
    elif not out_msg and "Malaysia" in input_string:
        out_msg=countries_asia[" Malaysia"] + continue_message
    
    elif not out_msg and "Maldives" in input_string:
        out_msg=countries_asia[" Maldives"] + continue_message
    
    elif not out_msg and "Mongolia" in input_string:
        out_msg=countries_asia[" Mongolia"] + continue_message
    
    elif not out_msg and "Myanmar (formerly Burma)" in input_string:
        out_msg=countries_asia[" Myanmar (formerly Burma)"] + continue_message
    
    elif not out_msg and "Nepal" in input_string:
        out_msg=countries_asia[" Nepal"] + continue_message    
    
    elif not out_msg and "North Korea" in input_string:
        out_msg=countries_asia[" North Korea"] + continue_message    
    
    elif not out_msg and "Oman" in input_string:
        out_msg=countries_asia[" Oman"] + continue_message
    
    elif not out_msg and "Pakistan" in input_string:
        out_msg=countries_asia[" Pakistan"] + continue_message       
    
    elif not out_msg and "Palestine" in input_string:
        out_msg=countries_asia[" Palestine"] + continue_message    
    
    elif not out_msg and "Philippines" in input_string:
        out_msg=countries_asia[" Philippines"] + continue_message    
    
    elif not out_msg and "Qatar" in input_string:
        out_msg=countries_asia[" Qatar"] + continue_message               
    
    elif not out_msg and "Russia" in input_string:
        out_msg=countries_asia[" Russia"] + continue_message    
    
    elif not out_msg and "Saudi Arabia" in input_string:
        out_msg=countries_asia[" Saudi Arabia"] + continue_message    
    
    elif not out_msg and "Singapore" in input_string:
        out_msg=countries_asia[" Singapore"] + continue_message    
    
    elif not out_msg and "South Korea" in input_string:
        out_msg=countries_asia[" South Korea"] + continue_message    
    
    elif not out_msg and "Sri Lanka" in input_string:
        out_msg=countries_asia[" Sri Lanka"] + continue_message    
    
    elif not out_msg and "Syria" in input_string:
        out_msg=countries_asia[" Syria"] + continue_message    
    
    elif not out_msg and "Taiwan" in input_string:
        out_msg=countries_asia[" Taiwan"] + continue_message    
    
    elif not out_msg and "Tajikistan" in input_string:
        out_msg=countries_asia[" Tajikistan"] + continue_message    
    
    elif not out_msg and "Thailand" in input_string:
        out_msg=countries_asia[" Thailand"] + continue_message    
    
    elif not out_msg and "Timor-Leste" in input_string:
        out_msg=countries_asia[" Timor-Leste"] + continue_message    
    
    elif not out_msg and "Turkey" in input_string:
        out_msg=countries_asia[" Turkey"] + continue_message    
    
    elif not out_msg and "Turkmenistan" in input_string:
        out_msg=countries_asia[" Turkmenistan"] + continue_message    
    
    elif not out_msg and "United Arab Emirates (UAE)" in input_string:
        out_msg=countries_asia[" United Arab Emirates (UAE)"] + continue_message    
    
    elif not out_msg and "Uzbekistan" in input_string:
        out_msg=countries_asia[" Uzbekistan"] + continue_message    
    
    elif not out_msg and "Vietnam" in input_string:
        out_msg=countries_asia[" Vietnam"] + continue_message    
    
    elif not out_msg and "Yemen" in input_string:
        out_msg=countries_asia[" Yemen"] + continue_message 

    return out_msg

def capitals_africa(out_msg,input_string):
    """" generic response for the chatbot to return capitals of
    countries in Africa"""
    
    if not out_msg and "Algeria" in input_string:
        out_msg=countries_africa["Here is a list of countries in Africa:\n\nAlgeria"] + continue_message 
    
    elif not out_msg and "Angola" in input_string:
        out_msg=countries_africa[" Angola"] + continue_message 
    
    elif not out_msg and "Benin" in input_string:
        out_msg=countries_africa[" Benin"] + continue_message 
    
    elif not out_msg and "Botswana" in input_string:
        out_msg=countries_africa[" Botswana"] + continue_message 
    
    elif not out_msg and "Burkina Faso" in input_string:
        out_msg=countries_africa[" Burkina Faso"] + continue_message 
    
    elif not out_msg and "Burundi" in input_string:
        out_msg=countries_africa[" Burundi"] + continue_message 
    
    elif not out_msg and "Cabo Verde" in input_string:
        out_msg=countries_africa[" Cabo Verde"] + continue_message 
    
    elif not out_msg and "Cameroon" in input_string:
        out_msg=countries_africa[" Cameroon"] + continue_message 
    
    elif not out_msg and "Central African Republic (CAR)" in input_string:
        out_msg=countries_africa[" Central African Republic (CAR)"] + continue_message 
    
    elif not out_msg and "Chad" in input_string:
        out_msg=countries_africa[" Chad"] + continue_message 
    
    elif not out_msg and "Comoros" in input_string:
        out_msg=countries_africa[" Comoros"] + continue_message 
    
    elif not out_msg and "Democratic Republic of the Congo" in input_string:
        out_msg=countries_africa[" Democratic Republic of the Congo"] + continue_message 
    
    elif not out_msg and "Republic of the Congo" in input_string:
        out_msg=countries_africa[" Republic of the Congo"] + continue_message 
    
    elif not out_msg and "Cote d'Ivoire" in input_string:
        out_msg=countries_africa[" Cote d'Ivoire"] + continue_message 
    
    elif not out_msg and "Djibouti" in input_string:
        out_msg=countries_africa[" Djibouti"] + continue_message 
    
    elif not out_msg and "Egypt" in input_string:
        out_msg=countries_africa[" Egypt"] + continue_message 
    
    elif not out_msg and "Equatorial Guinea" in input_string:
        out_msg=countries_africa[" Equatorial Guinea"] + continue_message 
    
    elif not out_msg and "Eritrea" in input_string:
        out_msg=countries_africa[" Eritrea"] + continue_message 
    
    elif not out_msg and "Eswatini" in input_string:
        out_msg=countries_africa[" Eswatini (formerly Swaziland)"] + continue_message 
    
    elif not out_msg and "Ethiopia" in input_string:
        out_msg=countries_africa[" Ethiopia"] + continue_message 
    
    elif not out_msg and "Gabon" in input_string:
        out_msg=countries_africa[" Gabon"] + continue_message 
    
    elif not out_msg and "Gambia" in input_string:
        out_msg=countries_africa[" Gambia"] + continue_message 
    
    elif not out_msg and "Ghana" in input_string:
        out_msg=countries_africa[" Ghana"] + continue_message 
    
    elif not out_msg and "Guinea-Bissau" in input_string:
        out_msg=countries_africa[" Guinea-Bissau"] + continue_message 
    
    elif not out_msg and "Kenya" in input_string:
        out_msg=countries_africa[" Kenya"] + continue_message 
    
    elif not out_msg and "Lesotho" in input_string:
        out_msg=countries_africa[" Lesotho"] + continue_message 
    
    elif not out_msg and "Liberia" in input_string:
        out_msg=countries_africa[" Liberia"] + continue_message 
    
    elif not out_msg and "Libya" in input_string:
        out_msg=countries_africa[" Libya"] + continue_message 
    
    elif not out_msg and "Madagascar" in input_string:
        out_msg=countries_africa[" Madagascar"] + continue_message 
    
    elif not out_msg and "Malawi" in input_string:
        out_msg=countries_africa[" Malawi"] + continue_message 
    
    elif not out_msg and "Mali" in input_string:
        out_msg=countries_africa[" Mali"] + continue_message 
    
    elif not out_msg and "Mauritania" in input_string:
        out_msg=countries_africa[" Mauritania"] + continue_message 
    
    elif not out_msg and "Mauritius" in input_string:
        out_msg=countries_africa[" Mauritius"] + continue_message 
    
    elif not out_msg and "Morocco" in input_string:
        out_msg=countries_africa[" Morocco"] + continue_message 
    
    elif not out_msg and "Mozambique" in input_string:
        out_msg=countries_africa[" Mozambique"] + continue_message 
    
    elif not out_msg and "Mauritania" in input_string:
        out_msg=countries_africa[" Mauritania"] + continue_message 
    
    elif not out_msg and "Namibia" in input_string:
        out_msg=countries_africa[" Namibia"] + continue_message 
    
    elif not out_msg and "Niger" in input_string:
        out_msg=countries_africa[" Niger"] + continue_message 
    
    elif not out_msg and "Nigeria" in input_string:
        out_msg=countries_africa["Nigeria"] + continue_message 
    
    elif not out_msg and "Rwanda" in input_string:
        out_msg=countries_africa[" Rwanda"] + continue_message    
    
    elif not out_msg and "Sao Tome and Principe" in input_string:
        out_msg=countries_africa[" Sao Tome and Principe"] + continue_message 
    
    elif not out_msg and "Senegal" in input_string:
        out_msg=countries_africa[" Senegal"] + continue_message 
    
    elif not out_msg and "Seychelles" in input_string:
        out_msg=countries_africa[" Seychelles"] + continue_message 
    
    elif not out_msg and "Sierra Leone" in input_string:
        out_msg=countries_africa[" Sierra Leone"] + continue_message  
    
    elif not out_msg and "Somalia" in input_string:
        out_msg=countries_africa[" Somalia"] + continue_message    
    
    elif not out_msg and "South Africa" in input_string:
        out_msg=countries_africa[" South Africa"] + continue_message 
    
    elif not out_msg and "South Sudan" in input_string:
        out_msg=countries_africa[" South Sudan"] + continue_message 
    
    elif not out_msg and "Sudan" in input_string:
        out_msg=countries_africa[" Sudan"] + continue_message 
    
    elif not out_msg and "Tanzania" in input_string:
        out_msg=countries_africa[" Tanzania"] + continue_message        
    
    elif not out_msg and "Togo" in input_string:
        out_msg=countries_africa[" Togo"] + continue_message    
    
    elif not out_msg and "Tunisia" in input_string:
        out_msg=countries_africa[" Tunisia"] + continue_message 
    
    elif not out_msg and "Uganda" in input_string:
        out_msg=countries_africa[" Uganda"] + continue_message 
    
    elif not out_msg and "Zambia" in input_string:
        out_msg=countries_africa[" Zambia"] + continue_message 
    
    elif not out_msg and "Zimbabwe" in input_string:
        out_msg=countries_africa[" Zimbabwe"] + continue_message  
    
    return out_msg

def activate_worldbot():
    """Main function to run our chatbot."""
    start()
    chat = True
  

    while chat:
        
        input_string, out_msg= get_input()
        
       # Check for an end msg 
        out_msg, chat = end_chat(input_string)
       
        # specify what to return
        #returns list of countries in the specified continent
        out_msg =return_country(out_msg=out_msg, input_string=input_string)
        #returns capital of country user input from South America
        out_msg=capitals_south_america(out_msg=out_msg, input_string=input_string)
        #returns capital of country user input from Oceania
        out_msg=capitals_oceania(out_msg=out_msg, input_string=input_string)
        #returns capital of country user input from Europe
        out_msg=capitals_europe(out_msg=out_msg, input_string=input_string)
        #returns capital of country user input from Asia
        out_msg=capitals_asia(out_msg=out_msg, input_string=input_string)
        #returns capital of country user input from Africa
        out_msg=capitals_africa(out_msg=out_msg, input_string=input_string)
     
         
        print(out_msg)

        

