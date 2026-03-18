text = """
"Hello! Bonjour! ¡Hola! Hallo!
Welcome to our global community. Es ist wunderbar, Menschen aus der ganzen Welt hier zu treffen. C'est magnifique de rencontrer des gens du monde entier ici. ¡Es maravilloso conocer gente de todo el mundo!
Today, we will share ideas. Wir möchten gemeinsam lernen und wachsen. Nous voulons apprendre et grandir ensemble. Queremos aprender y crecer juntos.
Danke, merci, gracias, and thank you for being here."""

from main import select
filename = select(text, filename)
