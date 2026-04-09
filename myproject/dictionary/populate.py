import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from dictionary.models import Dictionary

words = [
    ("bake", "paistaa (uunissa)"),
    ("boil", "keittää"),
    ("fry", "paistaa (pannulla)"),
    ("grill", "grillata"),
    ("marinate", "marinoida"),
    ("simmer", "hauduttaa"),
    ("chop", "hienontaa"),
    ("mince", "jauhaa hienoksi"),
    ("dice", "leikata kuutioiksi"),
    ("sauté", "kuullottaa"),
    ("knead", "vaivata (taikinaa)"),
    ("whisk", "vatkata"),
    ("season", "maustaa"),
    ("garnish", "koristella (ruokaa)"),
    ("braise", "pata-hauduuttaa"),
    ("blanch", "blansoida"),
    ("caramelize", "karamellisoida"),
    ("deglaze", "irrottaa paistoliemi"),
    ("fold", "kääntää (taikina)"),
    ("poach", "keittää varovasti"),
]

added = 0
for word, definition in words:
    obj, created = Dictionary.objects.get_or_create(word=word, defaults={"definition": definition})
    if created:
        added += 1
        print(f"Added: {word} = {definition}")
    else:
        print(f"Skipped (already exists): {word}")

print(f"\nDone. {added} new word(s) added.")
