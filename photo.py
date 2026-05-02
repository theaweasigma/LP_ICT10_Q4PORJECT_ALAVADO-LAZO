from pyscript import document

GALLERY_ITEMS = [
    {
        "name": "Nathan Abaca",
        "caption": "boy tulog in CAT",
        "img": "nath.jpg",
        "alt": "Nathan"
    },
    {
        "name": "Anthea Alavado",
        "caption": "dance club bts",
        "img": "thea.jpg",
        "alt": "thea"
    },
    {
        "name": "Maiah Arenal",
        "caption": "foodie!!",
        "img": "maiah.jpg",
        "alt": "Maiah"
    },
    {
        "name": "Anxela Aventajado",
        "caption": "peace",
        "img": "anxela.jpg",
        "alt": "Anxela"
    },
    {
        "name": "Gab Buhain",
        "caption": "no piccie yet",
        "img": "gab.jpg",
        "alt": "Gab"
    },
    {
        "name": "Joo Carpio",
        "caption": "no piccie yet",
        "img": "joo.jpg",
        "alt": "Joo"
    },
    {
        "name": "Caiomey Cenon",
        "caption": "ezra duo",
        "img": "caiomey.jpg",
        "alt": "Caiomey"
    },
    {
        "name": "Athena Cruz",
        "caption": "athena tickled me after this - thea",
        "img": "athena.jpg",
        "alt": "Athena"
    }
    {
        "name": "Niko De Leon",
        "caption": "boy sass",
        "img": "niko.jpg",
        "alt": "Niko"
    },
    {
        "name": "Chelsea De Peralta",
        "caption": "cutes!",
        "img": "chelsea.jpg",
        "alt": "Chelsea"
    },
    {
        "name": "Jercey Del Barrio",
        "caption": "shrimp ahhh",
        "img": "nyerney.jpg",
        "alt": "Jercey"
    },
    {
        "name": "Sittie Dida-Agun",
        "caption": "math guild cutes!",
        "img": "sittie.jpg",
        "alt": "Sittie"
    },
    {
        "name": "Jarett Dumlao",
        "caption": "this might be a threat face",
        "img": "jarett.jpg",
        "alt": "Jarett"
    },
    {
        "name": "Jakob Estapia",
        "caption": "itchy face lol",
        "img": "jbe.jpg",
        "alt": "Jakob"
    },
    {
        "name": "Chloe Galope",
        "caption": "intrams photocard",
        "img": "chloe.jpg",
        "alt": "Chloe"
    },
    {
        "name": "Uriel Galura",
        "caption": "is this aegyo?",
        "img": "uriel.jpg",
        "alt": "Uriel"
    }
    {
        "name": "Aaron Guevarra",
        "caption": "malcolm in the middle",
        "img": "aaron.jpg",
        "alt": "Aaron"
    },
    {
        "name": "Gelo Gurango",
        "caption": "no piccie yet",
        "img": "gelo.jpg",
        "alt": "Gelo"
    },
    {
        "name": "Ezra Lazo",
        "caption": "caiomey duo",
        "img": "ezra.jpg",
        "alt": "Ezra"
    },
    {
        "name": "Jakob Liwag",
        "caption": "after intrams",
        "img": "jbl.jpg",
        "alt": "Jakob"
    },
    {
        "name": "Anika Magpantay",
        "caption": "intrams photocard",
        "img": "anika.jpg",
        "alt": "Anika"
    },
    {
        "name": "Kaila Moyaen",
        "caption": "snooping thea's ipad",
        "img": "kaila.jpg",
        "alt": "Kaila"
    },
    {
        "name": "Xander Panuncialman",
        "caption": "i took this when xander was my seatmate - thea",
        "img": "xander.jpg",
        "alt": "Xander"
    },
    {
        "name": "Sam Prowel",
        "caption": "intrams photocar",
        "img": "sam.jpg",
        "alt": "Sam"
    }
    {
        "name": "Pio Ramos",
        "caption": "accident or not??",
        "img": "piyoh.jpg",
        "alt": "Pio"
    },
    {
        "name": "Katelyn Sannino",
        "caption": "back seat shenanigans",
        "img": "katewin.jpg",
        "alt": "Katelyn"
    },
    {
        "name": "Andrei Tecson",
        "caption": "andrei",
        "img": "andrei.jpg",
        "alt": "Andrei"
    },
    {
        "name": "Hans Ulit",
        "caption": "boy kain",
        "img": "hans.jpg",
        "alt": "Hans"
    },
]


def make_card(item):
    card = document.createElement("div")
    card.classList.add("gallery-card")

    image = document.createElement("img")
    image.src = item["img"]
    image.alt = item["alt"]
    card.appendChild(image)

    body = document.createElement("div")
    body.classList.add("card-body")

    title = document.createElement("div")
    title.classList.add("card-title")
    title.innerText = item["name"]
    body.appendChild(title)

    caption = document.createElement("div")
    caption.classList.add("card-caption")
    caption.innerText = item["caption"]
    body.appendChild(caption)

    card.appendChild(body)
    return card


def render_gallery():
    gallery = document.getElementById("gallery-grid")
    if gallery is None:
        return

    for item in GALLERY_ITEMS:
        gallery.appendChild(make_card(item))


render_gallery()
