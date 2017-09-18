from django.http import JsonResponse
from django.conf import settings
import random

BASE_IMG_PATH = settings.BASE_URL + "src/img/blog/"

def posts(request):
    titles = ["Four loko", "Fixie nostrud", "Master Cleanse", "Scenester hell", "Shabby chic", "Blue bottle",
              "Duis pitchfork", "Raclette portland", "Cardigan glossier", "Tumeric keffiyeh"]
    text = [
        "90's slow-carb twee everyday carry vegan aliquip, chambray affogato. Listicle enim hella, master cleanse cold-pressed YOLO hammock snackwave lumbersexual VHS. ",
        "Hexagon meditation elit, banh mi chambray sriracha qui tote bag. Poke delectus sustainable next level cred dolore mumblecore. Activated charcoal tbh hot chicken, pok pok yuccie man braid craft beer",
        "Duis pitchfork before they sold out yr. Yuccie deserunt delectus incididunt, raclette lumbersexual et VHS laborum freegan cronut you probably haven't heard of them tousled.",
        "Raclette portland tofu ugh, synth selfies labore vexillologist chambray. Esse chartreuse chia, squid hammock cold-pressed cray. Poutine kinfolk do consequat vaporware exercitation. ",
        "Truffaut irure echo park, wayfarers activated charcoal portland dolore culpa hammock irony mollit gluten-free plaid cliche. Tumeric keffiyeh sapiente meh, disrupt jianbing hot chicken deserunt letterpress succulents eiusmod hell of pork belly anim eu. ",
        "Banh mi kinfolk cillum +1 chia, copper mug fixie nostrud commodo hot chicken actually. Deep v four dollar toast DIY banh mi, reprehenderit labore occupy try-hard. ",
        "Taxidermy unicorn velit laborum, brooklyn you probably haven't heard of them aesthetic poke. Proident la croix VHS cupidatat anim swag franzen, disrupt yr pok pok freegan gastropub chambray."
    ]
    categories = ['News', 'Updates', 'Otro']

    out = []
    for i in range(random.randint(20, 100)):
        out.append({
            'id':i,
            'img': BASE_IMG_PATH + '00' + str(random.randint(1, 6)) + '.jpg',
            'title': random.choice(titles),
            'text': random.choice(text),
            'tags': [random.choice(categories) for _ in range(random.randint(1,2))]
        })
    return JsonResponse(out, safe=False)

def post(request, id):
    titles = ["Four loko", "Fixie nostrud", "Master Cleanse", "Scenester hell", "Shabby chic", "Blue bottle",
              "Duis pitchfork", "Raclette portland", "Cardigan glossier", "Tumeric keffiyeh"];
    text = [
        "<p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>" +
        "<p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.</p>" +
        "<p>Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>" +
        "<p>Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex</p>",
        "<p>But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness.</p>" +
        "<p>No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.</p>" +
        "<p>Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally</p>",
        "<p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>" +
        "<p>Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.</p>" +
        "<p>A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.</p>" +
        "<p>Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to</p>",
        "<p>One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.</p>" +
        "<p>He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections.</p>" +
        "<p>The bedding was hardly able to cover it and seemed ready to slide off any moment.</p>" +
        "<p>His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. \"What's happened to me? \" he thought. It wasn't a dream. His room, a proper human</p>"
    ]
    categories = ['News', 'Updates', 'Otro']

    out = {
        'title': random.choice(titles),
        'summary': random.choice(text),
        'img': BASE_IMG_PATH + '00' + str(random.randint(1, 6)) + '.jpg',
        'tags': [random.choice(categories) for _ in range(random.randint(1,2))],
        'info': 'Text'
    }

    return JsonResponse(out, safe=False)
