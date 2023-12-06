import discord
import os
from dotenv import load_dotenv
import random

load_dotenv()
bot = discord.Bot()


wrong_citations = ['„Frage nicht, was dein Land für dich tun kann, frage was du für dein Land tun kannst.“ - Kim Jong-il',
		   '„Dies ist mein Leib, der für euch hingegeben wird.“ - Gina Wild',
		   '„How much is the fish?“ - Karl Marx',
		   '„Heinrich, mir graut´s vor dir.“ - Thomas Mann',
		   '„Ein Experte ist ein Mann, der hinterher genau sagen kann, warum seine Prognose nicht gestimmt hat.“ - Peter Hartz',
		   '„Liebe deinen Nächsten wie dich selbst.“ - Kurt Cobain',
		   '„Handle nur nach derjenigen Maxime, durch die du zugleich wollen kannst, dass sie ein allgemeines Gesetz werde.“ - Silvio Berlusconi',
		   '„Die Proletarier haben nichts zu verlieren als ihre Ketten.“ - Heidi Klum',
		   '„Die Macht ist nicht etwas, was man erwirbt, wegnimmt, teilt, was man bewahrt oder verliert; die Macht ist etwas, was sich von unzähligen Punkten aus und im Spiel ungleicher und beweglicher Beziehungen vollzieht.“ - Darth Vader',
		   '„Niemand hat die Absicht, eine Mauer zu errichten.“ - Bob der Baumeister',
		   '„Verdammt sei der erste, der ein Stück Land mit einem Zaun umgab, und sagte: „Dies gehört mir.“ und verdammt seien die Leute, die einfältig genug waren, ihm zu glauben.“ - Napoleon I.',
		   '„There´s no business like show business.“ - Muammar al-Gaddafi',
		   '„Das Boot ist voll.“ - Noah, Sohn des Lamech (der mit der Arche, s. Bibel, Buch Genesis)',
		   '„Macht kaputt, was euch kaputt macht!“ - Axel Springer',
		   '„Je öfter eine Dummheit wiederholt wird, desto mehr bekommt sie den Anschein der Klugheit.“ - Lehman Brothers',
		   '„In diesem Fall ziehen Sie eine Maske schnell zu sich heran und platzieren diese fest auf Mund und Nase. Danach helfen Sie Kindern und hilfsbedürftigen Personen.“ - Batman zu Robin',
		   '„Was ist das? Das ist blaues Licht. Und was macht es? Es leuchtet blau.“ - Deutsche Hochschule der Polizei',
		   '„Dream a little dream of me.“ - Freddy Krueger',
		   '„Ich mache nie Voraussagen und werde das auch niemals tun.“ - Nostradamus',
		   '„I want you to want me. I need you to need me.“ - Angebot zur Nachfrage',
		   '„Wer kämpft, kann verlieren. Wer nicht kämpft, hat schon verloren.“ - Optimus Prime',
		   '„Köpfchen in das Wasser, Schwänzchen in die Höh.“ - CIA-Verhörmethode',
		   '„Jedes Publikum kriegt die Vorstellung, die es verdient.“ - Mario Barth',
		   '„Du riechst so gut.“ - Jean-Baptiste Grenouille',
		   '„Dieses Kribbeln im Bauch, das man nie mehr vergisst, als ob da im Magen der Teufel los ist.“ - Lieutenant Ellen Ripley',
		   '„Ich weiß was du letzten Sommer getan hast!“ - NSA',
		   '„Ich sehe was, was du nicht siehst.“ - NSA',
		   '„Geht in Ohr, bleibt im Kopf.“ - John F. Kennedy',
		   '„Deine Mudda.“ - Sigmund Freud',
		   '„Guten Freunden gibt man ein Küsschen.“ - Judas',
		   '„Hey, hey, hey! Hier kommt Alex. Vorgang auf, es ist eine Horrorschow!“ - Alexander Gauland',
		   '„Warum liegt hier überhaupt Stroh um?“ - Jesus von Nazareth',
		   '„Ach mein, dein. Das sind doch bürgerliche Kategorien.“ - Deutsche Bank',
		   '„Wer unter euch ohne Sünde ist der werfe den ersten Stein auf sie.“ - Ein Autonomer beim G20-Gipfel',
		   '„Das Ärgerliche am Ärger ist, dass man sich schadet, ohne anderen zu nützen.“ - Anakin Skywalker',
		   '„Erst das Essen, dann die Moral.“ - McDonalds',
		   '„Ach wie gut, dass niemand weiß, dass ich Rumpe,lstilzchen heiß.“ - Anonymous'
		   '„Ihr wollt meinen Schatz? Den könnt ihr haben. Sucht ihn doch! Irgendwo habe ich den größten Schatz der Welt versteckt.“ - Uli Hoeneß',
		   '„Vorwärts immer, rückwärts nimmer.“ - Supermario',
		   '„Ein Zauberer kommt nie zu spät, ebenso wenig zu früh, er kommt immer genau dann, wann er es beabsichtigt.“ - Motto der deutschen Bahn',
		   '„Und das ist erst die Spitze des Eisbergs.“ - Kapitän der Titanic',
		   '„Das Problem mit Zitaten im Internet ist, dass man nie weiß ob sie stimmen.“ - Julius Cesar',
		   '„Du willst zum Weibe gehen? Dann vergiss die Peitsche nicht.“ - Alice Schwarzer',
		   '„Ich wollte diesen Körper, und mir war egal was ich dafür tun musste.“ - Donald Trump',
		   '„Man ist, was man isst.“ - Hannibal Lecter',]


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "answer", description = "What do you get if you multiply six by nine?")
async def answer(ctx):
    await ctx.respond("42")

@bot.slash_command(name = "fzitat", description = "Ein zufälliges falsch zugeordnetes Zitat bitte!")
async def fzitat(ctx):
    await ctx.respond(wrong_citations[random.randint(0, len(wrong_citations) - 1)])

bot.run(os.getenv('OLYMP_TOKEN'))
