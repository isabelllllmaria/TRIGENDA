cities = ["Madrid", "New York City", "Chicago", "Hong Kong", "Rome", "Sydney", "Santo Domingo", "London", "Paris", "Casablanca"]

def my_destination(city):
    print("function running")
    if city == "Madrid":
        return["Museo Nacional del Prado", "Puerta del Sol", "Plaza Mayor", "Plaza de Toros de Las Ventas"]
    elif city == "New York City":
        return["Statue of Liberty", "Hudson Yards", "Times Square", "Empire State Building", "SoHo", "World Trade Center", "Central Park", "Rockefeller Center"]
    elif city == "Chicago":
        return["Millennium Park", "Navy Pier", "Cloud Gate", "Willis Tower", "Grant Park", "Magnificent Mile"]
    elif city == "Hong Kong":
        return["Hong Kong Disneyland (great for kids)", "Ocean Park (great for teens)", "Tian Tan Buddha", "Avenue of Stars", "Sky 100 Hong Kong Observation Deck"]
    elif city == "Rome":
        return["Colosseum", "St. Peter's Basilica", "Vaitcan Museums", "Sistine Chapel", "Piazza Navona", "Pantheon"]
    elif city == "Sydney":
        return["Sydney Opera House", "Bondi Beach", "Darling Harbour", "Taronga Zoo", "Royal Botanic Gradens","Circular Quay"]
    elif city == "Santo Domingo":
        return["Alcazar de Colon", "Basilica Cathedral of Santa Maria la Menor", "National Pantheon of the Dominican Republic"]
    elif city == "London":
        return["Big Ben", "The Eye", "Tower of London", "Tower Bridge", "Buckingham Palace", "The Wax Museum"]
    elif city == "Paris":
        return["Eiffel Tower", "The Louvre", "Notre Dame", "Arc de Triomphe", "Palace of Versilles", "Disneyland Paris (great for kids)", "Ile Saint-Louis"]
    elif city == "Casablanca":
        return["Hassan II Mosque", "Casablanca Cathedral", "Mohammed V Square", "Mahkama du Pacha", "Parc de la Ligue Arabe"]
def SHOW_IMG(cities):
    print("function running")
    if cities == "Madrid":
        return("https://images.unsplash.com/photo-1543783207-ec64e4d95325?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80")
    elif cities == "New York City":
        return("https://cdn.vox-cdn.com/thumbor/1eri3Bs_TstzmQ4g10TDPzBAXRY=/0x0:2000x1125/1200x675/filters:focal(840x403:1160x723)/cdn.vox-cdn.com/uploads/chorus_image/image/62765805/171109_08_25_09_5DSR4771.0.jpg")
    elif cities == "Chicago":
        return("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80")
    elif cities == "Hong Kong":
        return("https://images.unsplash.com/photo-1536599018102-9f803c140fc1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80")
    elif cities == "Rome":
        return("https://images.unsplash.com/photo-1515542622106-78bda8ba0e5b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80")
    elif cities == "Sydney":
        return("https://lonelyplanetimages.imgix.net/mastheads/65830387.jpg?sharp=10&vib=20&w=1200")
    elif cities == "Santo Domingo":
        return("https://images.unsplash.com/photo-1524778880162-1b5dccfbdb0b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80")
    elif cities == "London":
        return("https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80")
    elif cities == "Paris":
        return("https://images.unsplash.com/photo-1550340499-a6c60fc8287c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80")
    elif cities == "Casablanca":
        return("https://s-ec.bstatic.com/data/xphoto/1182x887/170/17067601.jpg?size=S")
    
def my_restaurants(city):
    print("function running")
    if city == "Madrid":
        return["Los Montes de Galicia", "El Sur", "CEBO Madrid Restaurant", "Ramon Freixa Madrid"]
    elif city == "New York City":
        return["The Grill", "The Modern", "Marea", "Ocean Prime", "Los Tacos No.1"]
    elif city == "Chicago":
        return["Alinea", "Girl and the Goat","Carnitas Uruapan Restaurant", "Boka", "S.K.Y"]
    elif city == "Hong Kong":
        return["Yardbird", "Aulis", "Caprice", "The Chairman", "Belon", "Tim Ho Wan"]
    elif city == "Rome":
        return["La Pergola", "Pinsere", "Tonnarello", "Antico Arco", "Borghiciana Pastificio Artigianale"]
    elif city == "Sydney":
        return["O Bar and Dining", "Aria Restaurant Sydney", "William Blue Dinning", "Six Penny", "est."]
    elif city == "Santo Domingo":
        return["Filigrana", "Elizondo Restaurante", "La Cassina", "Factory Steak and Lounge", "Pearl Urban Lounge"]
    elif city == "London":
        return["The Ledbury", "Core by Clare Smyth", "Bar 61 Restaurant", "Sushi Tetsu", "Bright"]
    elif city == "Paris":
        return["El Cinq", "Touch in Paris", "Le Vent d'Amor", "Boutary", "Mokonuts"]
    elif city == "Casablanca":
        return["La Sqala", "Blend", "Restaurant Al-Mounia", "Le Raid", "Don Camillo"]
    
        

def my_currency(city):
    print("function running")
    if city == "Madrid":
        return"Euro(€): 1 Euro(€) = 1.11 USD($)"
    elif city == "New York City":
        return "US Dollar($)"
    elif city == "Chicago":
        return "US Dollar($)"
    elif city == "Hong Kong":
        return "Hong Kong Dollar($): 1 HKD($) = 0.13 USD($)"
    elif city == "Rome":
        return "Euro(€): 1 Euro(€) = 1.11 USD($)"
    elif city == "Sydney":
        return "Australian Dollar($): 1 AUD($) = 0.68 USD($)"
    elif city == "Santo Domingo":
        return "Dominican Peso($): 1 RD($) = 0,020 USD($)"
    elif city == "London":
        return "Pound Sterling(£): 1 GBP(£) = 1.21 USD($)"
    elif city == "Paris":
        return "Euro(€): 1 Euro(€) = 1.11 USD($)"
    elif city == "Casablanca":
        return "Moroccan Dirham: MAD = 0.10 USD($)"


def my_hotels(city):
    print("function running")
    if city == "Madrid":
        return["The Pavilions Madrid", "Ibis Madrid Aeropuerto Barajas", "Hotel Europa", "Melia Madrid Princesa", "Novotel Madrid Cetner"]
    elif city == "New York City":
        return["Artezen Hotel", "Hitlon Garden Inn Times Square", "WestHouse Hotel New York", "Hyatt Union Square New York"]
    elif city == "Chicago":
        return["Hampton Inn & Suites Chicago", "Hampton Inn Chicago McCormick Place", "Cambria Hotel Chicago Magnificent Mike", "The Talbott Hotel"]
    elif city == "Hong Kong":
        return["Regal Jowloon Hotel", "Royal Plaza Hotel", "Courtyard Hong Kong", "Harbour Grand Hong Kong"]
    elif city == "Rome":
        return["palazzo Baj Guest House in Trastevere", "Hotel Raffaello", "Hotel Italia", "Inn Urbe Colosseo"]
    elif city == "Sydney":
        return["Shangri-La Hotel Sydney", "Four Seasons Hotel Sydney", "Ovolo 1888 Darling Harbour", "The Grace Hotel Sydney", "Amora Hotel Jamison Sydney"]
    elif city =="Santo Domingo":
        return["Novus Plaza Hodelpa", "Barcelo Santo Domingo", "Catalonia Santo Domingo", "Sheraton Santo Domingo", "Boutique Hotel Palacio"]
    elif city == "London": 
        return["Park Grand London Kensington", " Travelodge London City Hotel", "The Tower Hotel", "Lincoln Plaza London, Curio Collection by Hilton"]
    elif city == "Paris":
        return["Hotel Cecilia Paris", "Hotel du Printemps", "Les Jardins de Mademoiselle", "Hotel de L'Union", "Hotel International"]
    elif city == "Casablanca":
        return["Le Casablanca Hotel", "Four Seasons Hotel Casablanca", "Sofitel Casablanca Tour Blanche", "MELLIBER Appart Hotel"]