"""Develop an interactive game with a mini plot twist."""

daytime = input("Choose daytime (night/day): ")
if daytime == "night":
    print("The night sky is adorned with a blanket of stars.")
else:
    print(
        "The day was filled with the warmth of the sun, illuminating\
        the world with vibrant colors."
    )

path = input("Choose your path (forest/lake): ")
if path == "forest":
    print("You walk into a forest and feel tranquil glow over the quiet landscape.")

    beast = input("Choose your beast (owl/wolf): ")
    if beast == "owl":
        print(
            "In the heart of the forest, an owl perched silently on a branch,\
             its keen eyes watching over the nocturnal world below."
        )
    else:
        print(
            "The lone wolf stood on the rocky outcrop, its howl echoing through\
            the mountains and asserting its presence in the wild."
        )
else:
    print("You jump into a lake and saw a hidden treasure chest!")

    beast = input("Choose your beast (starfish/snake): ")
    if beast == "starfish":
        print(
            "A starfish lays nestled, in the glittering jewels and gold coins,\
            as a silent witness to the mysteries of the deep."
        )
    else:
        print(
            " A snake lays poised, its eyes reflecting the hidden secrets of the hoard,\
            coiled around the gleaming gold coins and precious gems."
        )
